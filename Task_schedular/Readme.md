📌 Project Overview
The Priority-Based Task Scheduling & Execution Monitoring System is a Python application that simulates how operating systems and backend services manage tasks using priority scheduling and runtime monitoring.

⚙️ High-Level Workflow

Tasks are defined with:
Task ID
Priority
Execution duration (simulated)
Failure probability (optional)
Tasks are inserted into a priority queue (min-heap)
Scheduler pulls tasks in priority order

Execution monitor:
Tracks runtime
Detects slow tasks using thresholds
Handles failures using exception handling
Final execution summary is printed