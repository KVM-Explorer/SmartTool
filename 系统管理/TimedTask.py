import time
import schedule


def job():
    print("I am working")


def schedule_task(job, task_time: str):
    schedule.every().day.at(task_time).do(job)
    while True:
        schedule.run_pending();
        time.sleep(1)


if __name__ == "__main__":
    schedule_task(job, "10:25")
