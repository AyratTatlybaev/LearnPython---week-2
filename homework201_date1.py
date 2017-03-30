import datetime 
#текущая дата 
date_now = datetime.datetime.now()

print('Текушая дата и время: '+ date_now.strftime('%Y/%m/%d %H:%M:%S'))
#
print('Один день назад : '+ date_now.replace(day=date_now.day-1).strftime('%Y/%m/%d %H:%M:%S'))
#
print('Месяц назад : '+ date_now.replace(month=date_now.month-1).strftime('%Y/%m/%d %H:%M:%S'))