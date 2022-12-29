from event import Event
from datetime import datetime as date


if __name__ == "__main__":
    event = Event(
        header = "Term",
        start_date = date.today(),
        term = 90, #in days
        alarm = True,

        # Parametrs:
        location = "United States",
        alarm_repetition = 3, 
        alarm_text = "The expiration date has passed",
    )

    event.save("NewEvent")
    
