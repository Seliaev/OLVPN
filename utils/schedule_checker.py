import schedule
from time import sleep

def schedule_checker():
    # проверка наличия запланированных задач и выполнения их в соответствии с расписанием.
    while True:
        schedule.run_pending()
        sleep(1)