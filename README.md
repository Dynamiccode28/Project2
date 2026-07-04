# Priority-Based Task Scheduling & Execution Monitoring System

## Overview

The **Priority-Based Task Scheduling & Execution Monitoring System** is a Python-based simulation of how operating systems and backend services schedule, execute, and monitor tasks. The project demonstrates priority scheduling using a **min-heap priority queue**, runtime monitoring, exception handling, and execution analytics.

Each task is scheduled according to its priority, executed sequentially, monitored for runtime performance, and analyzed upon completion.

---

## Features

- Priority-based task scheduling using a min-heap
- Simulated task execution
- Runtime monitoring and execution time measurement
- Slow task detection using configurable thresholds
- Failure simulation with exception handling
- Execution analytics and summary reporting
- Modular and object-oriented implementation

---

## Project Structure

```text
PriorityTaskScheduler/
│
├── main.py                 # Application entry point
├── scheduler.py            # Task scheduling logic
├── task.py                 # Task model
├── monitor.py              # Runtime monitoring
├── utils.py                # Helper functions
└── README.md               # Project documentation
```

---

## Task Model

Each task contains the following attributes:

| Attribute | Description |
|-----------|-------------|
| `task_id` | Unique task identifier |
| `priority` | Lower value indicates higher scheduling priority |
| `execution_time` | Simulated execution duration |
| `failure_probability` | Probability of runtime failure (optional) |

---

## System Workflow

The application follows a priority-driven execution pipeline.

```text
        Task Creation
              │
              ▼
 Priority Queue (Min Heap)
              │
              ▼
      Task Scheduler
              │
              ▼
     Execution Engine
              │
              ▼
     Runtime Monitoring
              │
              ▼
     Execution Summary
```

---

## Processing Pipeline

1. Tasks are created with their execution attributes.
2. Tasks are inserted into a priority queue implemented using a min-heap.
3. The scheduler always selects the task with the highest priority.
4. Task execution is simulated using configurable execution times.
5. Runtime monitoring records execution duration and detects slow-running tasks.
6. Runtime exceptions are handled gracefully to prevent scheduler interruption.
7. A final execution summary is generated after all tasks have been processed.

---

## Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Data Structures | Heap (Priority Queue) |
| Standard Library | `heapq`, `time`, `random` |
| Programming Concepts | Object-Oriented Programming, Exception Handling |

---

## Build Concepts Demonstrated

This project demonstrates several important software engineering concepts:

- Priority Queue (Min Heap)
- Task Scheduling
- Runtime Monitoring
- Execution Time Analysis
- Failure Simulation
- Exception Handling
- Object-Oriented Design

---

## Running the Project

### Clone the Repository

```bash
git clone https://github.com/Dynamiccode28/Project2.git
```

### Run the Application

```bash
python main.py
```

---

## Sample Output

```text
Executing Task T1 (Priority: 1)
Task T1 completed in 2.01 seconds

Executing Task T3 (Priority: 2)
Task T3 exceeded the execution threshold.

Executing Task T2 (Priority: 3)
Task T2 failed due to a simulated runtime error.

========== Execution Summary ==========

Task T1
Status : SUCCESS
Execution Time : 2.01 seconds

Task T3
Status : SLOW
Execution Time : 4.12 seconds

Task T2
Status : FAILED
```

---

## Learning Outcomes

This project demonstrates practical understanding of:

- Priority-based scheduling algorithms
- Heap-based data structures
- Object-oriented programming in Python
- Runtime monitoring techniques
- Exception handling
- Performance analysis

---

