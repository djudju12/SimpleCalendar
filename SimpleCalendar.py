import calendar
from datetime import datetime
import re
import sys
UNDERLINE = '\033[4;37m'
RESET = '\033[0m'
SPLITTER = '/'

def main():
    try:
        if len(sys.argv) == 2:
            dt = sys.argv[1]
            date = list(map(int, dt.split(SPLITTER)))
            if len(date) == 2:
                m, y = date
                d = None
            elif len(date) == 3:
                d, m, y = date
            else:
                print('invalid argument')
        else:
            d, m, y = None, None, None
        cal = give_me_calendar(y, m)
        print(give_pretty_calendar(cal, d))
    except Exception as e:
        return print(f'probably not a valida date => {dt}\nUse => DD/MM/YYYY')

def valid_date(date: str):
    return True

def give_me_today():
    return datetime.now()

def give_me_calendar(year: int = None, month: int = None):
    if not year:
        year = give_me_today().year
    if not month:
        month = give_me_today().month

    t = calendar.TextCalendar().formatmonth(year, month)
    return t

def give_pretty_calendar(cal: str = None, today: int = None) -> str:
    if not cal:
        cal = give_me_calendar()
    if not today:
        today: str = str(give_me_today().day)

    today = str(today)
    today_n: str = UNDERLINE + today + RESET
    return re.sub(r'(?<![0-9])(' + today + r')(?!\d)', today_n, cal)

if __name__ == '__main__':
    main()