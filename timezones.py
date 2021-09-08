from datetime import datetime
import pytz

montevideo_timezone = pytz.timezone("America/Montevideo")
montevideo_date = datetime.now(montevideo_timezone)
print("Montevideo:\t" + montevideo_date.strftime('%d/%m/%Y - %H:%M:%S'))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("Mexico:\t" + montevideo_date.strftime('%d/%m/%Y - %H:%M:%S'))