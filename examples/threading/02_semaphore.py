from threading import Thread, Semaphore, current_thread, Lock
from time import sleep

count_threads = 10
active_threads = 0
semaphore = Semaphore(3)
lock = Lock()

# class MyThread(Thread):
#     def run(self):
#         with semaphore:
#             print("Выполняет работу")
#             sleep(1)
#             print("Закончил работу")


# def create_threads(count_threads: int) -> list[MyThread]:
#     list_threads = []
#     for _ in range(count_threads):
#         th = MyThread()
#         list_threads.append(th)
#         th.start()
#     return list_threads


# def close_threads(threds: list[MyThread]):
#     for th in threds:
#         th.join()


# def main():
#     threads = create_threads(12)

#     close_threads(threads)

# main()


class MyThread(Thread):
    def run(self):
        global active_threads

        with semaphore:
            with lock:
                active_threads += 1
                print(
                    f"Поток {current_thread().name} выполняет действие "
                    f"({active_threads})"
                )

            sleep(1)

            with lock:
                print(f"Поток {current_thread().name} закончил действие")
                active_threads -= 1


def main() -> None:

    th = MyThread()
    threads = []
    for _ in range(10):
        th = MyThread()
        threads.append(th)
        th.start()
    for th in threads:
        th.join()


main()
