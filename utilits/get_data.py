from datetime import datetime, timedelta

def get_dates(days=7):
    dates=[]
    for i in range(days):
        date=datetime.now()+timedelta(days=i)
        dates.append(date.strftime("%d.%m.%Y"))
    return dates