from datetime import datetime, timedelta, time
def get_dates(days=7):
    dates=[]
    for i in range(days):
        date=datetime.now()+timedelta(days=i)
        dates.append(date.strftime("%d.%m.%Y"))
    return dates

def get_times(start=10,end=23,step=1):
    times=[]
    current=datetime.now().replace(minute=0,second=0,microsecond=0)

    while current.hour <= end:
        times.append(current.strftime("%H:%M"))
        current += timedelta(hours=step)

    return times


if __name__ == '__main__':
    print(get_times())