from week import Week, WeekType
import datetime
import calendar

if __name__ == "__main__":
    start = datetime.date(2024, 9, 9)
    delta = datetime.timedelta(7)
    end = datetime.date(2024, 11, 25)

    print(start + delta)
    print(end)
    print((end - start).days / 7)
    