CREATE TABLE IF NOT EXISTS "users" (
	"cust_id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"email"	INTEGER NOT NULL UNIQUE,
	"phone_number"	INTEGER,
	"name"	TEXT,
	"password"	TEXT NOT NULL DEFAULT 00000000,
	"user_type"	INTEGER NOT NULL DEFAULT 4,
	FOREIGN KEY("user_type") REFERENCES "user_type"("type")
);

CREATE TABLE IF NOT EXISTS "user_type" (
	"type"	INTEGER NOT NULL UNIQUE,
	"description"	TEXT,
	PRIMARY KEY("type")
);

CREATE TABLE IF NOT EXISTS "orders" (
	"order_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"cust_id"	INTEGER NOT NULL,
	"bike_id"	INTEGER NOT NULL,
	"start_datetime"	TEXT NOT NULL,
	"end_datetime"	INTEGER,
	"amount"	REAL DEFAULT 0,
	FOREIGN KEY("bike_id") REFERENCES "bikes"("bike_id"),
	FOREIGN KEY("cust_id") REFERENCES "users"("cust_id")
);

CREATE TABLE IF NOT EXISTS "bikes" (
	"bike_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"status"	TEXT NOT NULL,
	"bike_station"	INTEGER,
	"defect_id"	INTEGER
);

CREATE TABLE IF NOT EXISTS "bike_stations" (
	"station_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"post_code"	TEXT,
	"loc_lat"	INTEGER NOT NULL,
	"loc_long"	INTEGER NOT NULL,
	"bike_rack_number"	INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "defect_report" (
	"report_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"cust_id"	INTEGER NOT NULL,
	"category"	INTEGER NOT NULL,
	"details"	BLOB,
	"report_datetime"	TEXT NOT NULL,
	"status"	TEXT NOT NULL,
	FOREIGN KEY("cust_id") REFERENCES "users"("cust_id")
);
