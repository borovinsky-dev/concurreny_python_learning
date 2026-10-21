from threading import Thread, Barrier
from time import sleep
from random import randint


class Worker(Thread):
    def __init__(self, barrier: Barrier) -> None:
        super().__init__()
        self.barrier = barrier

    def run(self) -> None:
        print(f"{self.name}: подготовка")
        sleep(randint(1, 3))

        print(f"{self.name}: ожидание остальных")
        self.barrier.wait()

        print(f"{self.name}: начало работы")


def main() -> None:
    count = 3
    barrier = Barrier(count)

    threads = [Worker(barrier) for _ in range(count)]

    for th in threads:
        th.start()

    for th in threads:
        th.join()


main()
