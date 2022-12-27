import qrcode
import datetime
from datetime import datetime as date

def generate_link(text: str, dates: tuple, **parametrs):
    global link
    link = "https://www.google.com/calendar/event?action=TEMPLATE"

    def add(sub: str, data):
        global link
        link += f"&{sub}={data}"

    text = text.replace(' ', "%20")
    dates = f"{dates[0]}/{dates[1]}"

    add("text", text)
    add("dates", dates)

    for key in parametrs:
        data = str(parametrs[key]).replace(' ', "%20")
        add(key, data)

    return link


def generate_event(text: str, dt: date, expiration_date: int, alarm = False, **parametrs):
    start = date_to_int(dt)
    dt += datetime.timedelta(days = expiration_date)
    end = date_to_int(dt)

    event = \
f"""BEGIN:VCALENDAR
BEGIN:VEVENT
"""

    data = \
f"""
UID:
DTSTART:{start}
DTEND:{end}
SUMMARY:{text}
"""

    for key in parametrs:
        d = str(parametrs[key]) + "\n"
        data += f"{key.upper()}: {d}"
    event += data

    if alarm:
        event += \
            """BEGIN:VALARM
TRIGGER:-PT24H
REPEAT:1
DURATION:PT15M
ACTION:DISPLAY
DESCRIPTION:Reminder
END:VALARM
"""

    event += \
"""END:VEVENT
END:VCALENDAR"""

    return event


def save_qr(data: str, name: str = "qr"):
    img = qrcode.make(data)
    img.save(f'{name}.png')

def date_to_int(d: date):
    days = str(d.day) if d.day >= 10 else "0" + str(d.day)
    months = str(d.month) if d.month >= 10 else "0" + str(d.month)
    
    return int(str(d.year) + months + days)
