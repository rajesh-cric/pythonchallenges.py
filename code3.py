
from datetime import datetime,timedelta
today=datetime.now()
print('Today is:'+str(today))
one_day=timedelta(days=1)
yesterday=today-one_day
print('Ýesterday is:'+str(yesterday))
date=input("enter a date (dd/mm/yyyy): ")
one_date=datetime.strptime(date,'%d/%m/%Y')
one_week=timedelta(days=7)
next_week=one_date+one_week
print('the date one week from the date entered:'+str(next_week))