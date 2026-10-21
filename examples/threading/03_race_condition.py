from threading import Thread

count = 0


def change_count() -> None:
    global count

    for _ in range(1000):
        value = count
        value += 1
        count = value
        print(count)


def main() -> None:
    threads = []

    for _ in range(10):
        th = Thread(target=change_count)
        threads.append(th)
        th.start()


main()
