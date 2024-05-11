import datetime

class Task:
    def __init__(self, description, deadline, status, on_time_status):
        # Конструктор класса Task, принимающий описание задачи, срок выполнения, статус и статус по времени
        self.description = description
        self.deadline = deadline
        self.status = status
        self.on_time_status = on_time_status

    def list_tasks(self):
        # Метод вывода списка задач
        if self.status == "":
            print(f"{self.description} Срок: {self.deadline}")
        if self.on_time_status:
            print(f"{self.description} Срок: {self.deadline} Статус: {self.status} {self.on_time_status}")

    def write_to_file(self, filename):
        # Метод записи задачи в файл
        with open(filename, "a") as file:
            file.write(f"{self.description},{self.deadline},{self.status}")
            file.write("\n")

    @staticmethod
    def read_from_file(filename):
        # Статический метод для чтения задач из файла
        tasks = []
        with open(filename, "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                if 4 > len(task_data) >= 3:
                    description, deadline = task_data[:2]
                    tasks.append(Task(description, deadline, "", ""))
                else:
                    description, deadline, status, on_time_status = task_data[:4]
                    tasks.append(Task(description, deadline, status, on_time_status))
        return tasks

def add_new_task():
    # Функция для добавления новой задачи
    description = input("Введите описание новой задачи: ")
    deadline = input("Введите срок выполнения новой задачи (гггг-мм-дд): ")
    new_task = Task(description, deadline, "", "")
    new_task.write_to_file("tasks.txt")
    print("Новая задача успешно добавлена.")

def mark_task_as_done():
    # Функция для пометки задачи как выполненной
    tasks = Task.read_from_file("tasks.txt")
    if not tasks:
        print("Список текущих задач пуст.")
        return

    print("Список текущих задач:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.description}")

    try:
        task_index = int(input("Выберите номер задачи для пометки как выполненной: ")) - 1
        if 0 <= task_index < len(tasks):
            task = tasks[task_index]
            on_time = input("Введите дату фактического выполнения задачи (гггг-мм-дд): ")
            deadline_date = datetime.datetime.strptime(task.deadline, "%Y-%m-%d").date()
            done_date = datetime.datetime.strptime(on_time, "%Y-%m-%d").date()
            if done_date <= deadline_date:
                task.on_time_status = "В срок"
            else:
                task.on_time_status = "Не в срок"
            task.status = "Выполнено"
            tasks.pop(task_index)
            with open("tasks_complete.txt", "a") as file:
                file.write(f"{task.description}, {task.deadline}, {task.status},{task.on_time_status},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            with open("tasks.txt", "w"):
                for task in tasks:
                    task.write_to_file("tasks.txt")
            print("Задача успешно помечена как выполненная.")
        else:
            print("Некорректный номер задачи.")
    except ValueError:
        print("Введите корректное число.")

def exit_program():
    # Функция для выхода из программы
    print("Программа завершена.")
    exit()

# Основной цикл программы
while True:
    print("Менеджер задач. Выберите действие:")
    print("1. Вывести список текущих задач.")
    print("2. Вывести список выполненных задач.")
    print("3. Ввести новую задачу.")
    print("4. Пометить задачу выполненной.")
    print("5. Завершить программу.")
    choice = input("Введите номер действия (1, 2, 3, 4 или 5): ")

    if choice == "1":
        # Вывод списка текущих задач
        print("Список текущих задач:")
        tasks = Task.read_from_file("tasks.txt")
        if not tasks:
            print("Список текущих задач пуст.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. ", end="")
                task.list_tasks()
    elif choice == "2":
        # Вывод списка выполненных задач
        print("Список выполненных задач:")
        tasks = Task.read_from_file("tasks_complete.txt")
        if not tasks:
            print("Список выполненных задач пуст.")
        else:
            for task in tasks:
                task.list_tasks()
    elif choice == "3":
        # Добавление новой задачи
        add_new_task()
    elif choice == "4":
        # Пометка задачи как выполненной
        mark_task_as_done()
    elif choice == "5":
        # Завершение программы
        exit_program()
    else:
        print("Некорректный выбор.")
