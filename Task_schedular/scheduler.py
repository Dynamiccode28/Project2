import heapq

class TaskScheduler:
    def __init__(self):
        self._queue = []

    def add_task(self, task):
        heapq.heappush(self._queue, task)

    def get_next_task(self):
        if self._queue:
            return heapq.heappop(self._queue)
        return None

    def has_tasks(self):
        return len(self._queue) > 0
