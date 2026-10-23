import asyncio
from time import sleep
from random import randint

# async def task_one() -> None:
#     print("Задача 1: начало...")
#     await asyncio.sleep(2)


# async def task_two() -> None:
#     print("Задача 2: начало ...")
#     await asyncio.sleep(1)


# async def main() -> None:
#     await asyncio.gather(task_one(), task_two())


# asyncio.run(main())

count_concurrent_tasks = 4


async def process_order(order_id: int) -> str:
    print("Обработка заказа началась")
    await asyncio.sleep(randint(1, 3))
    print("Обработка заказза завершилась")
    return f"Заказ {order_id} обработан"


async def main() -> None:
    list_coroutines = [
        asyncio.create_task(process_order(i)) for i in range(count_concurrent_tasks)
    ]
    print(f"Список задач: {len(list_coroutines)}")
    await asyncio.gather(*list_coroutines)
    print("Все задачи завершились")


asyncio.run(main())
