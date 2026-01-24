def print_report(records):
    print("\nExecution Report")
    print("-" * 40)
    for r in records:
        print(
            f"Task {r['task_id']} | "
            f"Time: {r['execution_time']:.2f}s | "
            f"Status: {r['status']}"
        )
