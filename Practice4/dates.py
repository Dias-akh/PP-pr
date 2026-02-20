#1
import datetime
current=datetime.datetime.now()
five_days=datetime.timedelta(days=5) #!
result=current-five_days
print("Result 1: ")
print(result.strftime("%Y-%m-%d-%A"))

#2
import datetime
today=datetime.datetime.now()
turn=datetime.timedelta(days=1)
yesterday=today-turn
tomorrow=today+turn
print("Result 2: ")
print("Yesterday:",yesterday.strftime("%m-%d-%A"))
print("Today",today.strftime("%m-%d-%A"))
print("Tomorrow",tomorrow.strftime("%m-%d-%A"))

#3
import datetime
dt = datetime.datetime.now()
dt_no_microseconds = dt.replace(microsecond=0)
print("Result 3: ")
print("Original:", dt)
print("Without micrseconds:", dt_no_microseconds)

#4
import datetime
date1 = datetime.datetime(2026, 2, 19, 12, 0, 0)
date2 = datetime.datetime(2026, 2, 18, 12, 0, 0)
difference = date1 - date2
seconds_diff = difference.total_seconds()
print("Result 4: ")
print(f"difference on seconds: {seconds_diff}")

