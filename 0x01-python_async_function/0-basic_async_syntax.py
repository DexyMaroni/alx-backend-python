#!/usr/bin/env python3

""" An Asynchronous Program """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    A coroutine that takes in a default value (max_delay)

    and waits for a certain amount of time before continuing.

    """

    randomNumber = random.uniform(0, max_delay)
    await asyncio.sleep(randomNumber)
    return randomNumber
