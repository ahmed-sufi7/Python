import time
from plyer import notification

while True:
    print("Please drink some water!")
    notification.notify(title="Please drink some water", message="Its time to drink some water")
    time.sleep(60*60)
