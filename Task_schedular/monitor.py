class Monitor:
    def __init__(self, slow_threshold=2.0):
        self.slow_threshold = slow_threshold
        self.records = []

    def record(self, task_id, exec_time, status):
        self.records.append({
            "task_id": task_id,
            "execution_time": exec_time,
            "status": status
        })

    def summary(self):
        return self.records
