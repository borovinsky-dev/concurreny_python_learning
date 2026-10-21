from threading import Thread, current_thread
from time import sleep


def worker() -> None:
    print("Дочерний поток")
    for i in range(5):
        print(i)


def main() -> None:

    print("Main-поток")
    th_1 = Thread(target=worker)
    print("Запуск дочерного потока")
    th_1.start()
    th_1.join()
    print("Конец работы дочерного потока")
    print("Работа главного потока")
    for i in range(100, 106):
        print(i)


main()
