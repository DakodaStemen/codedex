# main.py

import datetime, bday_messages

today = datetime.date.today()

next_bday = datetime.date(2025, 9, 10)

days_away = next_bday - today

print(days_away)