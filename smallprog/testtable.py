from prettytable import PrettyTable

# Создание таблицы и добавление заголовков
table = PrettyTable()
table.field_names = ["Имя", "Возраст", "Город"]

# Добавление строк
table.add_row(["Alice", 24, "London"])
table.add_row(["Bob", 30, "New York"])
table.add_row(["Charlie", 22, "Berlin"])

# Печать таблицы
print(table)
