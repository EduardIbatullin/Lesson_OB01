class Store:
    def __init__(self, name, address):
        # Инициализация магазина с указанием наименования и адреса
        self.name = name
        self.address = address
        self.items = {}  # Словарь для хранения товаров магазина

    def add_item(self, item_name, price):
        # Добавление товара в магазин
        self.items[item_name] = price

    def remove_item(self, item_name):
        # Удаление товара из магазина по его названию
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} успешно удален из магазина {self.name}")
        else:
            print(f"Товар {item_name} в магазине {self.name} не найден")

    def get_price(self, item_name):
        # Получение цены товара по его названию
        if item_name in self.items:
            print(f"Наименование товара: {item_name}, Цена: {self.items[item_name]} рублей")
        else:
            print(f"Товар {item_name} в магазине {self.name} не найден")

    def update_price(self, item_name, new_price):
        # Обновление цены товара по его названию
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара {item_name} успешно изменена на {new_price} рублей")
        else:
            print(f"Товар {item_name} в магазине {self.name} не найден")

    def list_items(self):
        # Вывод списка товаров магазина
        print(f"\nМагазин: {self.name}, Адрес: {self.address}")
        if self.items:
            print("Список товаров:")
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. {item}: {self.items[item]} рублей")
        else:
            print("В магазине нет товаров.")


def main_menu():
    # Вывод основного меню программы
    print("\nОсновное меню:")
    print("1. Вывести список магазинов")
    print("2. Выбрать магазин")
    print("3. Завершить программу")


def store_submenu():
    # Вывод подменю работы с товарами магазина
    print("\nПодменю работы с товарами магазина:")
    print("1. Вывести список товаров")
    print("2. Добавить товар")
    print("3. Изменить цену товара")
    print("4. Удалить товар")
    print("5. Узнать цену товара")
    print("6. Вернуться в основное меню")
    print("7. Завершить программу")


# Создание объектов магазинов
store_1 = Store("ЦУМ", "г. Москва, ул. Петровка, д. 2")
store_2 = Store("Магнит", "г. Москва, ул. Садовая, д. 5")
store_3 = Store("М.Видео", "г. Москва, ул. Ленинградская, д. 7")

# Наполнение магазинов товарами
store_1.add_item("Сумочка Gucci", 15000)
store_1.add_item("Сумочка Versace", 20000)
store_1.add_item("Сумочка Armani", 25000)

store_2.add_item("Молоко", 100)
store_2.add_item("Хлеб", 50)
store_2.add_item("Сыр", 100)

store_3.add_item("Телевизор Sony", 100000)
store_3.add_item("Телевизор Samsung", 120000)
store_3.add_item("Телевизор LG", 80000)


def main():
    # Основная функция программы
    while True:
        main_menu()  # Вывод основного меню
        choice = input("Выберите пункт из меню: ")

        if choice == "1":
            # Вывод списка всех магазинов
            print("\nСписок магазинов:")
            for index, store in enumerate([store_1, store_2, store_3], start=1):
                print(f"{index}. {store.name}")
        elif choice == "2":
            # Выбор магазина для работы
            store_selection()
        elif choice == "3":
            print("Программа завершена.")
            exit()  # Завершение программы
        else:
            print("Некорректный ввод. Пожалуйста, выберите пункт из меню.")


def store_selection():
    # Функция выбора магазина для работы
    while True:
        print("\nВыберите магазин:")
        for index, store in enumerate([store_1, store_2, store_3], start=1):
            print(f"{index}. {store.name}")
        store_index = input("Введите номер магазина или '0' для возврата в основное меню: ")

        if store_index == "0":
            break
        elif store_index.isdigit() and 1 <= int(store_index) <= 3:
            selected_store = [store_1, store_2, store_3][int(store_index) - 1]
            store_submenu()  # Вывод подменю для выбранного магазина
            store_action(selected_store)
        else:
            print("Некорректный ввод. Пожалуйста, введите номер магазина.")


def store_action(store):
    # Функция выполнения действий с выбранным магазином
    while True:
        action = input("Выберите действие из подменю: ")

        if action == "1":
            store.list_items()  # Вывод списка товаров магазина
        elif action == "2":
            # Добавление товара в магазин
            item_name = input("Введите наименование товара: ")
            price = input("Введите цену товара: ")
            if price.isdigit():
                store.add_item(item_name, int(price))
                print("Товар успешно добавлен.")
            else:
                print("Некорректный ввод цены.")
        elif action == "3":
            # Изменение цены товара
            store.list_items()
            item_index = input("Введите номер товара для изменения цены: ")
            new_price = input("Введите новую цену: ")
            if item_index.isdigit() and 1 <= int(item_index) <= len(store.items) and new_price.isdigit():
                selected_item = list(store.items.keys())[int(item_index) - 1]
                store.update_price(selected_item, int(new_price))
            else:
                print("Некорректный ввод.")
        elif action == "4":
            # Удаление товара из магазина
            store.list_items()
            item_index = input("Введите номер товара для удаления: ")
            if item_index.isdigit() and 1 <= int(item_index) <= len(store.items):
                selected_item = list(store.items.keys())[int(item_index) - 1]
                store.remove_item(selected_item)
            else:
                print("Некорректный ввод.")
        elif action == "5":
            # Получение цены товара по его названию
            item_name = input("Введите наименование товара: ")
            store.get_price(item_name)
        elif action == "6":
            main()  # Возврат в основное меню
        elif action == "7":
            print("Программа завершена.")
            exit()  # Завершение программы
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из подменю.")
        store_submenu()


if __name__ == "__main__":
    main()  # Вызов основной функции программы
