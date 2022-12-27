from event import Event
from datetime import datetime as date


if __name__ == "__main__":
    event = Event(
        header = "Term",
        start_date = date.today(),
        term = 90, #in days
        alarm = True,

        # Parametrs:
        location = "United States"
    )

    event.save("NewEvent")
    
