from to_qr import generate_event, save_qr
from datetime import datetime as date


if __name__ == "__main__":
    event = generate_event(
        "Term",
        dt = date.today(),
        expiration_date = 90, #in days
        alarm = True,
        # location = "United States"
    )
    
    save_qr(event, "WithAlarm")

    
