from dataclasses import dataclass, field
from typing import Callable

@dataclass(order=True)
class Task:
    priority: int
    task_id: int = field(compare=False)
    action: Callable = field(compare=False)
    expected_time: float = field(compare=False)

    def run(self):
        self.action()
