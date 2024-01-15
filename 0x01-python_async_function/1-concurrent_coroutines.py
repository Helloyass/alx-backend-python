#!/usr/bin/env python3
"""
1-concurrent_coroutines.py - Provides a coroutine for
 concurrently running multiple random delays
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Concurrently runs n random delays each with a maximum delay
     of max_delay seconds

    n (int): The number of concurrent random delays to spawn
    max_delay (int): The maximum delay time allowed (inclusive)

    Returns: a list of the delays that were implemented
    """

    wait_times: List[float] = []

    async def append_wait_random() -> None:
        """
        Implements a random wait and adds the wait time into a list

        Returns: none
        """
        wait_times.append(await wait_random(max_delay))

    await asyncio.gather(*(append_wait_random() for _ in range(n)))
    return wait_times
