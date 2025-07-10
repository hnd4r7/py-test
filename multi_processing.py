from fastapi import FastAPI
from joblib import Parallel, delayed, Memory
import asyncio
from concurrent.futures import ProcessPoolExecutor
from fastapi.concurrency import run_in_threadpool
from functools import partial
import os
from typing import List

app = FastAPI()

# Configuration
cpu_num = 2  # CPU cores per request
max_total_cores = min(os.cpu_count() or 4, 4)  # Total CPU cores across all requests
semaphore = asyncio.Semaphore(max_total_cores // cpu_num)

# Initialize joblib Memory for caching
cache_dir = "joblib_cache"
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
memory = Memory(location=cache_dir, verbose=0)


# Example function to parallelize
def process_task(x):
    # Simulate CPU-intensive work
    return x * x


# Wrapper to run joblib in a process pool (with caching)
@memory.cache
def run_parallel_job(data: List[int], cpu_num: int):
    return Parallel(n_jobs=cpu_num, backend="loky")(delayed(process_task)(i) for i in data)


# Async wrapper to manage concurrency
async def run_parallel_with_semaphore(data: List[int]) -> List[int]:
    async with semaphore:  # Limit concurrent requests based on available cores
        # Offload to process pool to avoid blocking the event loop
        result = await run_in_threadpool(partial(run_parallel_job, data, cpu_num))
        return result


# FastAPI endpoint
@app.get("/process")
async def process_data():
    # Example input data
    input_data = list(range(10))
    results = await run_parallel_with_semaphore(input_data)
    return {"results": results}
