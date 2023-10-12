from datetime import datetime, timedelta


cur_date_time = datetime.now()
print(cur_date_time)

# Date formatting 2023/09/21
formatted_date = cur_date_time.strftime('%Y=%m=%d %H-%M')
print(formatted_date)

future_date = cur_date_time - timedelta(days=10)
print(future_date)