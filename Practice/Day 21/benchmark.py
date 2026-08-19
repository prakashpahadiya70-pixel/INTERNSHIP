import asyncio
import time
import requests
import statistics

SYNC_URL = "http://127.0.0.1:8000/sync"
ASYNC_URL = "http://127.0.0.1:8000/async"

NUMBER_OF_REQUESTS = 50


def sync_request():
    response = requests.get(SYNC_URL)
    return response.status_code


async def async_request(session):
    loop = asyncio.get_running_loop()

    response = await loop.run_in_executor(
        None,
        requests.get,
        ASYNC_URL
    )

    return response.status_code


def benchmark_sync():
    start = time.perf_counter()

    results = []

    for _ in range(NUMBER_OF_REQUESTS):
        results.append(sync_request())

    total_time = time.perf_counter() - start

    return total_time, results


async def benchmark_async():
    start = time.perf_counter()

    tasks = [
        async_request(None)
        for _ in range(NUMBER_OF_REQUESTS)
    ]

    results = await asyncio.gather(*tasks)

    total_time = time.perf_counter() - start

    return total_time, results


print("=" * 55)
print("DAY 21 CONCURRENT API PERFORMANCE BENCHMARK")
print("=" * 55)

print(f"\nNumber of Requests: {NUMBER_OF_REQUESTS}")

print("\nTesting Synchronous API...")
sync_total, sync_results = benchmark_sync()

print("Testing Asynchronous API...")
async_total, async_results = asyncio.run(benchmark_async())


print("\n" + "=" * 55)
print("PERFORMANCE RESULTS")
print("=" * 55)

print(f"\nSynchronous API:")
print(f"Total Time: {sync_total:.4f} seconds")
print(f"Average Time: {sync_total / NUMBER_OF_REQUESTS:.4f} seconds")
print(f"Successful Requests: {sync_results.count(200)}")


print(f"\nAsynchronous API:")
print(f"Total Time: {async_total:.4f} seconds")
print(f"Average Time: {async_total / NUMBER_OF_REQUESTS:.4f} seconds")
print(f"Successful Requests: {async_results.count(200)}")


improvement = (
    (sync_total - async_total)
    / sync_total
) * 100


print("\n" + "=" * 55)
print("PERFORMANCE COMPARISON")
print("=" * 55)

print(f"\nPerformance Improvement: {improvement:.2f}%")

if improvement > 0:
    print("Result: Asynchronous API performed faster.")
else:
    print("Result: No performance improvement observed.")


print("=" * 55)