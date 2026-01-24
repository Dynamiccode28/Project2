# 🧠 Priority-Based Task Scheduling & Execution Monitoring System

A Python-based simulation of how operating systems and backend services schedule, execute, and monitor tasks using **priority scheduling** and **runtime monitoring**.

This project demonstrates core concepts such as:
- Priority queues (min-heaps)
- Task execution simulation
- Runtime monitoring
- Failure handling
- Execution analytics

---

## 📌 Project Overview

The **Priority-Based Task Scheduling & Execution Monitoring System** simulates a task scheduler that executes tasks based on priority while monitoring their execution behavior.

Each task is:
- Scheduled using a **priority queue**
- Executed in priority order
- Monitored for slow execution
- Handled safely if failures occur

---

## ⚙️ High-Level Workflow

1. **Task Definition**
   Each task contains:
   - `task_id` – unique identifier
   - `priority` – lower value means higher priority
   - `execution_time` – simulated runtime
   - `failure_probability` *(optional)* – chance of failure during execution

2. **Task Scheduling**
   - Tasks are inserted into a **min-heap priority queue**
   - Scheduler always picks the highest-priority task

3. **Task Execution**
   - Execution time is simulated using sleep
   - Random failures may occur based on probability

4. **Execution Monitoring**
   - Tracks start & end time
   - Detects slow tasks using predefined thresholds
   - Handles runtime errors using exception handling

5. **Execution Summary**
   - Displays execution status of each task
   - Shows runtime details and failures

---

## 🏗️ System Architecture

```
Task Creator
     ↓
Priority Queue (Min Heap)
     ↓
Task Scheduler
     ↓
Execution Engine
     ↓
Runtime Monitor
     ↓
Execution Summary
```

---

## 🧪 Features

- ✅ Priority-based scheduling
- ⏱ Runtime tracking
- ⚠️ Slow task detection
- ❌ Failure simulation & handling
- 📊 Final execution report

---

## 🛠️ Technologies Used

- Python 3
- `heapq` for priority queue
- `time` for execution simulation
- `random` for failure simulation
- Exception handling

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd priority-task-scheduler
   ```

2. Run the program:
   ```bash
   python main.py
   ```

---

## 📈 Sample Output

```
Executing Task T1 (Priority: 1)
Task T1 completed in 2.01 seconds

Executing Task T3 (Priority: 2)
⚠ Task T3 marked as slow

Executing Task T2 (Priority: 3)
❌ Task T2 failed due to runtime error

===== Execution Summary =====
Task T1 : SUCCESS | Time: 2.01s
Task T3 : SLOW    | Time: 4.12s
Task T2 : FAILED
```

---


