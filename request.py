import asyncio
import json
import time
from typing import Coroutine

import aiohttp

time_s = time.time()
url_list = [
    "http://intent-recognizer.ru",
    "http://intent-recognizer.ru",
    "http://intent-recognizer.ru",
    "http://intent-recognizer.ru",
]

headers = {
    'Cookie': 'SESSIONID=cb45ff64588e419518a6a0dff39249fb; TOKEN=1be88642-4678-4477-a83d-5fd1aa07c83c',
    'Content-Type': 'application/json'
}
body = {'text': 'привет яху'}
payload = json.dumps(body)
request_params = {'data': payload}


async def request(method: str, url, request_args: [dict] = None, ):
    try:
        async with aiohttp.ClientSession(
                headers=headers,
        ) as session:
            async with session.request(method, url, **request_args, timeout=5) as response:
                # print(response.status, url)
                return response
    except Exception as exc:
        print(exc)


async def main():
    tasks = []
    for url in url_list:
        task: Coroutine = request("POST", url, request_params)
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
delta = time.time() - time_s
print(f'Run time :- {delta}')
