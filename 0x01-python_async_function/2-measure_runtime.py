#!/usr/bin/env python3
"""
2-measure_runtime.py - Provides a coroutine for
 measuring the time of concurrently running multiple
 random delays
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Concurrently runs n random delays each with a maximum delay
     of max_delay seconds and measures the execution time

    n (int): The number of concurrent random delays to spawn
    max_delay (int): The maximum delay time allowed (inclusive)

    Returns: the ratio of the execution time to n
    """

    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed: float = time.perf_counter() - start
    return elapsed / n
