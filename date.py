import calendar

# 获取当前年份和月份
year = 2024
month = 6
day = 1

a = calendar.month(year,month,w=2,l=1)
b = calendar.monthcalendar(year,month)
c = calendar.monthrange(year,month)
d = calendar.prmonth(year,month,w=2,l=1)
e = calendar.month(year,month,w=2,l=1)
f = calendar.weekday(year,month,day)
print(a)
print(b)
print(c)
print(d)
print(e)  
print(f)
