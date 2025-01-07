from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)

def calculate_future_date():
    days = int(input"Enter the number of days to add to the current date: "))
    future_date = timedelta(days=days) + datetime.now()
    print(future_date.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()
calculate_future_date()