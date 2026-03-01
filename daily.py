from datetime import datetime
import time

RUN_TIME = "20:37"


def run_task() -> None:
    print("gm ya'll!")


last_run_date = None

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if current_time == RUN_TIME and last_run_date != now.date():
        run_task()
        last_run_date = now.date()

    time.sleep(1)
