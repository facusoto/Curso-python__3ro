from datetime import datetime

# my_date = datetime.datetime.now()
# print(my_date)

# my_day = datetime.date.today()
# print(my_day)
# print(f'Year: {my_day.year}')
# print(f'Month: {my_day.month}')
# print(f'Day: {my_day.day}')

#

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_str}')

my_str = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {my_str}')

my_str = my_datetime.strftime('Estamos en el año %Y')
print(f'Formato Random: {my_str}')
