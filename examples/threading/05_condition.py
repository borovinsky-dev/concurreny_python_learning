from threading import Condition, Thread, current_thread
from time import sleep

# condition = Condition()
# data = None


# class Producer(Thread):
#     def run(self):
#         global data
#         with condition:
#             name_current_thread = current_thread().name
#             print(f"Производитель {name_current_thread} создает данные")
#             data = 10
#             condition.notify()


# class Consumer(Thread):
#     def run(self):
#         global data
#         with condition:
#             name_current_thread = current_thread().name
#             while data is None:
#                 print(f"Потребитель {name_current_thread} ждет данные")
#                 condition.wait()
#             else:
#                 print(f"Потребитель {name_current_thread} читает данные")


# def main() -> None:

#     prod = Producer()
#     cons = Consumer()
#     prod.start()
#     cons.start()

#     prod.join()
#     cons.join()


# main()

# condition = Condition()
# data = None


# class Consumer(Thread):
#     def run(self):
#         global data
#         with condition:
#             while data == None:
#                 print("Ждет данные чтобы прочитать")
#                 condition.wait()
#             else:
#                 print("Получаем данные")
#                 print(data)


# class Producer(Thread):
#     def run(self):
#         global data
#         with condition:
#             data = 100
#             condition.notify()


# def main():
#     cons = Consumer()
#     prod = Producer()

#     cons.start()
#     prod.start()

#     cons.join()
#     prod.join()


# main()

# data = []
# condition = Condition()


# class Consumer(Thread):
#     def run(self):
#         global data
#         with condition:
#             while not data:
#                 condition.wait()
#             else:
#                 while data:
#                     x = data.pop(0)
#                     print(x)
#                     condition.notify_all()


# class Producer(Thread):
#     def run(self):
#         global data
#         with condition:
#             for i in range(1, 6):
#                 while len(data) >= 2:
#                     condition.wait()

#                 data.append(i)
#                 condition.notify_all()


# def main():
# cons = Consumer()
# prod = Producer()
# prod.start()
# cons.start()

# cons.join()

# prod.join()


# main()

# data = []
# condition = Condition()


# class Producer(Thread):
#     def run(self):
#         with condition:
#             for i in range(1, 11):
#                 while len(data) >= 3:
#                     condition.wait()
#                 data.append(i)
#                 condition.notify()


# class Consumer(Thread):

#     def run(self):
#         with condition:
#             for _ in range(10):
#                 while not data:
#                     condition.wait()

#                 x = data.pop(0)
#                 print(x)
#                 condition.notify()


# def main():
#     cons = Consumer()
#     prod = Producer()
#     prod.start()
#     cons.start()

#     cons.join()

#     prod.join()

# main()

condition = Condition()
data = []


class Producer(Thread):
    def run(self):
        count = 0
        global data
        with condition:
            while True:
                count += 1
                if len(data) >= 3:
                    condition.wait()
                data.append(count)
                sleep(1)
                condition.notify()


class Consumer(Thread):
    def run(self):
        with condition:
            while True:
                while not data:
                    condition.wait()
                x = data.pop(0)
                sleep(1)
                print(x)
                condition.notify()


def main():
    cons = Consumer()
    prod = Producer()
    prod.start()
    cons.start()

    cons.join()

    prod.join()


main()

# from threading import Thread, Condition, Event, current_thread

# data = []
# condition = Condition()
# producer_finished = False


# class Producer(Thread):
#     def run(self) -> None:
#         global producer_finished
#         name_thread = current_thread()
#         with condition:
#             print(f"Поток {name_thread} начинает выполнять работу добавления чисел")
#             for i in range(1, 6):
#                 data.append(i)
#             producer_finished = True
#             condition.notify_all()


# class Worker(Thread):

#     def run(self):
#         with condition:
#             while (not producer_finished and not data) or (
#                 not data and producer_finished
#             ):
#                 condition.wait()

#             for i in range(1, 6):
#                 print(data.pop(0))


# class Worker(Thread): ...

# from threading import Thread, Condition, Event, current_thread

# condition = Condition()
# data = []
# producer_finished = False


# class Producer(Thread):

#     def run(self):
#         global data
#         global producer_finished
#         with condition:
#             print(f"Поток {current_thread()} производит данные")
#             for i in range(1, 6):
#                 data.append(i)
#             producer_finished = True
#             condition.notify_all()


# class Worker(Thread):
#     def run(self):
#         global data
#         global producer_finished
#         with condition:
#             while True:
#                 print(f"Поток {current_thread()} читает данные ...")
#                 while data == [] and producer_finished == False:
#                     condition.wait()
#                 if data == [] and producer_finished == True:
#                     return
#                 else:
#                     print(data.pop(0))


# def main():
#     prod = Producer()
#     work = Worker()
#     prod.start()
#     work.start()

#     prod.join()
#     work.join()


# main()
