from threading import Event, Thread, current_thread
from time import sleep

# event = Event()
# count_threads = 5


# def worker() -> None:
#     print(f"{current_thread().name}: Ожидаю старта")
#     event.wait(timeout=3)
#     print(f"{current_thread().name}: Сигнал получен, начинаю работу")


# def create_run_threads() -> list[Thread]:
#     list_threads = []
#     for _ in range(count_threads):
#         th = Thread(target=worker)
#         print("Ожидаю старта")
#         th.start()
#         list_threads.append(th)

#     return list_threads


# def close_threads(list_threads: list[Thread]):
#     for th in list_threads:
#         th.join()


# def main() -> None:
#     name_main_thread = current_thread()
#     print(f"{name_main_thread}-поток начал работу")
#     list_threads = create_run_threads()
#     sleep(3)
#     event.set()
#     close_threads(list_threads)


# main()

# event = Event()
# class MyThread(Thread):
#     def run(self):
#         while not event.is_set():
#             print(f"Поток {current_thread().name} работает")
#             event.wait(1)
#         else:
#             print(f"Поток {current_thread().name} остановлен")

# def main() -> None:
#     thread = MyThread()
#     thread.start()
#     sleep(3)
#     event.set()
#     thread.join()
# main()

# event = Event()

# class MyThread(Thread):
#     def run(self):
#         print("Поток ожидает разрешения")
#         event.wait()
#         print("Поток начинает работу...")
#         for _ in range(3):
#             print("Работаю....")
#             sleep(1)
#         print("Работа завершена")


# def main() -> None:
#     my_th = MyThread()
#     my_th.start()
#     print("Сигнализируем из главного потока")
#     event.set()
#     my_th.join()


# main()

start_event = Event()
stop_event = Event()


class MyThread(Thread):
    def run(self) -> None:
        start_event.wait()
        while not stop_event.is_set():
            print(f"Поток {current_thread().name} работает")
            stop_event.wait(1)
        print(f"Поток остановлен: {current_thread().name}")

    @classmethod
    def create_threads(cls, count: int) -> list[MyThread]:
        list_threads = []
        for i in range(count):
            th = MyThread()
            th.start()
            list_threads.append(th)
        return list_threads


def main():
    threads = MyThread.create_threads(3)
    sleep(2)
    start_event.set()
    sleep(5)
    stop_event.set()
    for th in threads:
        th.join()


main()
