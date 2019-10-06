import pandas as pd
import numpy as np
import matplotlib.dates as mydates
import matplotlib.cbook as cbook
import datetime
import matplotlib.pyplot as plt

#mydateparser = lambda x: pd.datetime.strptime(x, "%Y %m %d %H:%M:%S")
#mydateparser = lambda x: pd.datetime.strptime(x, "%Y %m %d %H:%M:%S")
#df = pd.read_csv("bike_activity.csv", sep=',', names=['date', 'bike_rent'], parse_dates=['date'], date_parser=mydateparser)
#df = pd.read_csv("bike_activity.csv", sep=',', names=['date', 'bike_rent'], parse_dates=['date'])

date1= datetime.date(2000,1,1)
date2= datetime.date(2011,1,1)
delta = datetime.timedelta(days=365)
dates= mydates.drange(date1,date2,delta)

numbers = np.random.randint(1,100,12)

data ={'apples':10, 'oragnes':15, 'lemons':5}
names= list(data.keys())
values= list(data.values())

fig, ax = plt.subplots()
ax.plot(dates,numbers,label="rent bikes")
#ax[0].plot(names,values)
#ax[1].scatter(names,values)
#ax.bar(names,values)
fig.suptitle('Rent bikes')

years= mydates.YearLocator()
months= mydates.MonthLocator()
years_fmt= mydates.DateFormatter('%Y')

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)

datemin= date1
datemax= date2
ax.set_xlim(datemin,datemax)

ax.format_xdata= mydates.DateFormatter('%Y-%m-%d')
ax.format_ydata= lambda x: '$%3.2f' % x
ax.grid(True)

ax.set_xlabel('year')
ax.set_ylabel('rent car')

#fig.autofmt_xdate()
plt.show()
