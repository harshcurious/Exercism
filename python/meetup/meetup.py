from datetime import date
import calendar


MeetupDayException = "MeetupDayException"


def meetup(year, month, week, day_of_week):
    def search(year, month, start, end, day):
        for i in range(start, end+1):
            if date(year, month, i).weekday() == day:
                return date(year, month, i)
        raise Exception(MeetupDayException)

    days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
            'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    if week == "teenth":
        # Look for the day_of_week between 13 and 19 (inclusive)
        return search(year, month, 13, 19, days[day_of_week])
    elif week == "1st":
        # Look for the day_of_week between 1 and 7 (inclusive)
        return search(year, month, 1, 7, days[day_of_week])
    elif week == "2nd":
        # Look for the day_of_week between 8 and 14 (inclusive)
        return search(year, month, 8, 14, days[day_of_week])
    elif week == "3rd":
        # Look for the day_of_week between 15 and 21 (inclusive)
        return search(year, month, 15, 21, days[day_of_week])
    elif week == "4th":
        # Look for the day_of_week between 22 and 28 (inclusive)
        return search(year, month, 22, 28, days[day_of_week])
    elif week == "5th":
        # Look for the day_of_week between 29 and 31 (inclusive)
        return search(year, month, 29, 31, days[day_of_week])
    elif week == "last":
        # Look for the day_of_week between length_of_month-6 and length_of_month (inclusive)
        temp, length_of_month = calendar.monthrange(year, month)
        return search(year, month, length_of_month-6, length_of_month, days[day_of_week])
