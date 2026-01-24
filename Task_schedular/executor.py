import time

class TaskExecutor:
    def __init__(self, monitor):
        self.monitor = monitor

    def execute(self, task):
        start = time.time()
        status = "SUCCESS"

        try:
            task.run()
        except Exception:
            status = "FAILED"

        end = time.time()
        exec_time = end - start

        if exec_time > self.monitor.slow_threshold:
            status = "SLOW"

        self.monitor.record(task.task_id, exec_time, status)
