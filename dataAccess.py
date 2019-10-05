import sqlite3
import numpy as np
from . import app  
from flask import g

PRJ_DB = "bikeRenting.db"

def get_db():
    db=getattr(g,"_bikedb",None)
    if db is None:
        db= g._bikedb= sqlite3.connect(PRJ_DB)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db=getattr(g,'_bikedb',None)
    if db is not None:
        db.close

#Registration
def doRegistration(user_type,email,phone_no,name,password):
    try:
        cur= get_db().cursor()
        cur.execute("INSERT INTO users (email,phone_number,name,password,user_type) VALUES (?,?,?,?,?)", (email,phone_no,name,password,user_type))
        get_db().commit()
        return True
    except:
        print("doRegistration error")
        get_db().rollback()
        return False

#Login
def doLogin(email,password):
    try:
        cur= get_db().cursor()
        cur.execute("SELECT user_type, password FROM users WHERE email = ?", [email])
        row= cur.fetchone()
        user_type= row[0]
        secret= row[1]
        if password == secret:
            session_ran = np.random.random(3)
            session_no=""
            for unit in session_ran:
                session_no= session_no + str(unit)
            return (True, user_type, session_no)
        else:
            return (False,-1,"")
    except:
        print("doLogin error")
        return (False,-1,"")    

print(__name__)
if __name__ == "__main__":
    doRegistration(1,"test@gmail.com","11111111","P","22222222")