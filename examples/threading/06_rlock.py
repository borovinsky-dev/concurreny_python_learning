from threading import Thread, RLock

lock = RLock()


def second():
    with lock:
        print("Вторая функция: работа выполнена")


def first():
    with lock:
        print("Первая функция: начинаю работу")
        second()
        print("Первая функция: заканчиваю работу")


thread = Thread(target=first)
thread.start()
thread.join()
