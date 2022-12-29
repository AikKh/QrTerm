import qrcode
import datetime
from datetime import datetime as date


class Event:

    Begin = """BEGIN:VCALENDAR
BEGIN:VEVENT
%s
END:VEVENT
END:VCALENDAR"""

    UID = """UID:
DTSTART:%s
DTEND:%s
SUMMARY:%s
"""

    Alarm = """BEGIN:VALARM
TRIGGER:-PT24H
REPEAT:%s
DURATION:PT15M
ACTION:DISPLAY
DESCRIPTION:%s
END:VALARM
"""

    def __init__(self, header: str, start_date: date, term: int, alarm = False, **params):
        self._header = header

        self._start = Event.date_to_int(start_date)
        self._end = Event.date_to_int(start_date + datetime.timedelta(days = term))

        self._alarm = alarm
        self._params = params


    def get_string(self):
        uid = Event.UID % (self._start, self._end, self._header)

        for key in self._params:
            d = str(self._params[key]) + "\n"
            uid += f"{key.upper()}:{d}"

        if (self._alarm):
            uid += (Event.Alarm % (self._params.get("alarm_repetition", '1'), 
                                   self._params.get("alarm_text", "Defaulf description")))

        return Event.Begin % uid


    def save(self, name: str):
        "Save event as QR code"
        name = self._header if not name else name
        
        img = qrcode.make(self.get_string())
        img.save(f'{name}.png')


    def add_param(self, key: str, value):
        self._params[key] = value
        

    @staticmethod
    def date_to_int(d: date):
        days = str(d.day) if d.day >= 10 else "0" + str(d.day)
        months = str(d.month) if d.month >= 10 else "0" + str(d.month)
        
        return int(str(d.year) + months + days)

    

