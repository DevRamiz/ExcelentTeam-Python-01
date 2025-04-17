
import datetime
import random

def no_vinnigrete(start, end):
    start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
    delta = (end_date - start_date).days
    chosen_date = start_date + datetime.timedelta(days=random.randint(0, delta))

    if chosen_date.weekday() == 0:  # Monday
        print("Ain't gettin' no vinaigrette today :(")
    else:
        print(f"Ain't gettin' no vinaigrette on {chosen_date.strftime('%A')} :(")

