import asyncio
from asyncio import Future
import itertools
import time

async def set_future_value(future: Future) -> None:
  print("Run set_future_value(future)")
  print("Suspend set_future_value(future)")
  await asyncio.sleep(3)
  print("Resume set_future_value(future)")
  future.set_result(42)

def make_request() -> Future:
  future = Future()
  asyncio.create_task(set_future_value(future))
  return future

async def spin() -> None:
  print("Run spin()")
  try:
    for char in itertools.cycle(r'\|/-'):
      # print(f'\r{char}', flush=True, end='')
      # time.sleep(0.1)
      print("Suspend spin()")
      await asyncio.sleep(3)
      print("Resume spin()")
      time.sleep(3)
  except asyncio.CancelledError as ex:
    pass

async def main():
  print("==> Run main()")
  future = make_request()
  print(f'Is the future done? {future.done()}')
  spinner = asyncio.create_task(spin())
  print("==> Suspend main()")
  value = await future
  print("==> Resume main()")
  spinner.cancel()
  print(f'Is the future done? {future.done()}')
  print(value)

asyncio.run(main())
