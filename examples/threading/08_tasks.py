from threading import Thread, Lock, Event, current_thread, Barrier, Semaphore
from time import sleep
from random import randint

# Задача решена (1 балл из 5)
# count = 0
# count_threads = 5
# lock = Lock()


# class Worker(Thread):

#     def run(self) -> None:
#         global count
#         lock.acquire()
#         count += 10000
#         lock.release()

#     @staticmethod
#     def create_workers(count_threads: int = count_threads) -> list[Worker]:
#         list_workers = []
#         for i in range(count_threads):
#             list_workers.append(Worker())
#         return list_workers

#     @staticmethod
#     def start_workers(list_workers: list[Worker]) -> None:
#         for worker in list_workers:
#             worker.start()

#     @staticmethod
#     def join_workers(list_workers: list[Worker]) -> None:
#         for worker in list_workers:
#             worker.join()


# def main() -> None:
#     worker = Worker()
#     list_workers = worker.create_workers()
#     worker.start_workers(list_workers)
#     worker.join_workers(list_workers)
#     print(count)

# main()

# задача решена (2/5)
# count_threads = 3
# event = Event()


# class Worker(Thread):
#     def run(self):
#         print(f"Поток {current_thread()} ждет сигнала от главного потока")
#         event.wait()
#         print(f"Worker в потоке {current_thread()} готов работать")


# def main() -> None:
#     list_workers = []
#     for _ in range(3):
#         th = Worker()
#         th.start()
#         list_workers.append(th)
#     sleep(2)
#     event.set()
#     for th in range(3):
#         th.join()


# main()

# задача решена(3/5)
# barrier = Barrier(4)
# count_threads = 4


# class WorkerThread(Thread):

#     def run(self) -> None:
#         print(f"Начало подготовки потока {current_thread()}")
#         sleep(randint(1, 3))
#         barrier.wait()
#         print(f"Работа потока {current_thread()}")


# def main() -> None:
#     list_threads = []
#     for _ in range(4):
#         th = WorkerThread()
#         th.start()
#         list_threads.append(th)
#     for th in list_threads:
#         th.join()


# main()
