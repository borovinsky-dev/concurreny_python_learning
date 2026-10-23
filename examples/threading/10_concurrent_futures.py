from concurrent.futures import ThreadPoolExecutor
from time import sleep


def square(number: int) -> int:
    sleep(1)
    return number**2


executor = ThreadPoolExecutor()


def main() -> None:
    list_executors = []
    with executor:
        for i in range(3):
            list_executors.append(executor.submit(square, (i + 1) * 10))

    for task in list_executors:
        print(task.result())


main()
