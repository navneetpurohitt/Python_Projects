import asyncio
"""
This script demonstrates the use of `async` and `await` in Python for asynchronous programming.
Key Concepts:
1. `async`:
    - Used to define an asynchronous function.
    - An asynchronous function returns a coroutine object when called.
    - Allows the function to be paused and resumed later.
2. `await`:
    - Used to pause the execution of an asynchronous function until the awaited coroutine completes.
    - Must be used inside an `async` function.
    - Enables non-blocking behavior, allowing other tasks to run while waiting for the result.
Usage in the script:
- The `validate_data` function is defined as asynchronous using `async`. It simulates a time-consuming operation using `await asyncio.sleep(1)`.
- The `main` function creates multiple asynchronous tasks using `validate_data` and gathers their results using `await asyncio.gather(*tasks)`.
- This approach allows concurrent execution of tasks, improving efficiency when dealing with I/O-bound operations or tasks that involve waiting.
Note:
- The `asyncio.run(main())` function is used to execute the asynchronous `main` function.
"""

async def validate_data(data):
    await asyncio.sleep(1)  # Simulate an async operation
    if isinstance(data, str) and data.isalnum():
        return f"Validation successful for: {data}"
    else:
        return f"Validation failed for: {data}"

async def main():
    data_list = ["Python123", "HelloWorld!", "ValidData", 12345]
    tasks = [validate_data(data) for data in data_list]
    print(tasks)
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
    
    