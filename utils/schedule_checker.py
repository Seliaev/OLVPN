import schedule
from time import sleep

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)