import asyncio
import time
import pandas as pd
import aiofiles
from typing import Callable, Union
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor


@dataclass
class Request:
    path: str
    request_id: int


class SimpleFastAPI:
    def __init__(self):
        self.routes = {}
        self.loop = asyncio.get_event_loop()
        self.executor = ThreadPoolExecutor(max_workers=2)  # Thread pool for sync tasks

    def add_route(self, path: str, endpoint: Callable):
        self.routes[path] = endpoint

    async def handle_request(self, request: Request):
        endpoint = self.routes.get(request.path)
        if not endpoint:
            return {"error": f"No route for {request.path}"}

        print(f"Processing request {request.request_id} for {request.path}")

        if asyncio.iscoroutinefunction(endpoint):
            result = await endpoint(request)
        else:
            # Offload sync endpoint to thread pool to avoid blocking
            result = await self.loop.run_in_executor(self.executor, endpoint, request)

        print(f"Completed request {request.request_id} for {request.path}")
        return result

    async def process_requests(self, requests):
        tasks = [self.handle_request(req) for req in requests]
        results = await asyncio.gather(*tasks)
        return results


# Endpoints
def sync_compute(request: Request):
    start_time = time.time()
    df = pd.DataFrame({"col": range(1000000)})
    result = df["col"].sum()
    time_taken = time.time() - start_time
    return {"result": int(result), "time_taken": time_taken, "request_id": request.request_id}


def sync_blocking(request: Request):
    time.sleep(2)
    return {"message": "Blocking sync task completed", "request_id": request.request_id}


async def async_io(request: Request):
    async with aiofiles.open("sample.txt", mode="r") as f:
        content = await f.read()
    return {"content": content[:100], "request_id": request.request_id}


async def async_sleep(request: Request):
    await asyncio.sleep(1)
    return {"message": "Async sleep completed", "request_id": request.request_id}


# Setup app
app = SimpleFastAPI()
app.add_route("/sync/compute", sync_compute)
app.add_route("/sync/blocking", sync_blocking)
app.add_route("/async/io", async_io)
app.add_route("/async/sleep", async_sleep)

# Simulate requests
requests = [
    Request("/async/sleep", 1),
    Request("/sync/blocking", 2),
    Request("/async/io", 3),
    Request("/sync/compute", 4),
]


# Run
async def main():
    print("Starting request processing...")
    start_time = time.time()
    results = await app.process_requests(requests)
    print(f"\nResults: {results}")
    print(f"Total time: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("Hello, this is a test file for async I/O.")
    asyncio.run(main())
