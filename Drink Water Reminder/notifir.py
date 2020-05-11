import time
import os
from plyer import notification

base=os.getcwd()
path=os.path.join(base,'bottel.ico')
print(path)

while True:
    notification.notify('Drink Water',message="You Should drink water now.",timeout=3,app_icon=path)
    time.sleep(60*60)