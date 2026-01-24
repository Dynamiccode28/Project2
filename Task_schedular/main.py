import time
from task import Task
from scheduler import TaskScheduler
from executor import TaskExecutor
from monitor import Monitor
from logger_util import print_report


# Sample task functions
def fast_task():
    time.sleep(0.5)

def slow_task():
    time.sleep(3)

def failing_task():
    raise RuntimeError("Task failed")


def main():
    scheduler = TaskScheduler()
    monitor = Monitor(slow_threshold=2.0)
    executor = TaskExecutor(monitor)

    tasks = [
        Task(priority=2, task_id=1, action=fast_task, expected_time=0.5),
        Task(priority=1, task_id=2, action=slow_task, expected_time=3),
        Task(priority=3, task_id=3, action=failing_task, expected_time=1),
    ]

    for task in tasks:
        scheduler.add_task(task)

    while scheduler.has_tasks():
        task = scheduler.get_next_task()
        executor.execute(task)

    print_report(monitor.summary())


if __name__ == "__main__":
    main()
