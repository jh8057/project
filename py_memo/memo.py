import datetime

dt = datetime.datetime.today()

today_year = str(dt.year)
today_month = str(dt.month)
today_day = str(dt.day)
today_hour = str(dt.hour)
today_minute = str(dt.minute)
today_second = str(dt.second)
today = str(dt)
today1 = today.replace('-','')
today2 = today1.replace(':','-')


print(today[:19])
print(today2[:17])

f = open("UZ in {}{}{}_{}-{}-{}.txt".format(today_year,today_month,today_day,today_hour,today_minute,today_second),'w')
#f = open("UZ in {}.txt".format(today[:19]),'w')

data = str(dt)
f.write(data)
f.close()