from queue import Queue
from threading import Thread, current_thread
from time import sleep
from random import randint

tasks = Queue()


class Producer(Thread):
    def run(self) -> None:
        print(f"{current_thread()} начинает добавление чисел ...")
        for i in range(1, 16):
            # добавление чисел в очередь
            tasks.put(i)
            print(f"Добавлено число {i} в очередь")
        print(f"Числа добавлены в очередь")
        tasks.put(None)


class Consumer(Thread):

    def run(self) -> None:
        print(f"{current_thread()} начинает считывание чисел ...")
        while True:
            sleep(randint(1, 2))
            element = tasks.get()
            tasks.task_done()
            if element != None:
                print(element, end="\t")
            else:
                break


def main() -> None:
    prod = Producer()
    cons = Consumer()
    prod.start()
    cons.start()
    tasks.join()
    prod.join()
    cons.join()


main()
