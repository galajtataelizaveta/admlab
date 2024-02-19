from peewee import *

# Создание подключения к БД SQLite
db = SqliteDatabase('database.db')

# Определение моделей
class BaseModel(Model):
    class Meta:
        database = db

class Client(BaseModel):
    name = CharField()
    city = CharField()
    address = CharField()

class Order(BaseModel):
    client = ForeignKeyField(Client, backref='orders')
    date = DateField()
    amount = DecimalField(max_digits=10, decimal_places=2)
    description = TextField()

# Функция для создания базы данных
def initialize_database():
    db.connect()
    db.create_tables([Client, Order])
    db.close()

# Функция для заполнения тестовыми данными
def fill_database():
    clients_data = [
        {"name": "John Doe", "city": "New York", "address": "123 Main St"},
        {"name": "Alice Smith", "city": "Los Angeles", "address": "456 Elm St"},
        {"name": "Bob Johnson", "city": "Chicago", "address": "789 Oak St"},
        {"name": "Emma Davis", "city": "San Francisco", "address": "101 Pine St"},
        {"name": "Michael Wilson", "city": "Seattle", "address": "222 Maple St"},
        {"name": "Sophia Brown", "city": "Miami", "address": "333 Palm St"},
        {"name": "David Martinez", "city": "Dallas", "address": "444 Cedar St"},
        {"name": "Olivia Rodriguez", "city": "Boston", "address": "555 Spruce St"},
        {"name": "William Lee", "city": "Denver", "address": "666 Birch St"},
        {"name": "Ava Gonzalez", "city": "Phoenix", "address": "777 Walnut St"}
    ]

    orders_data = [
        {"client": 1, "date": "2024-02-18", "amount": 100.50, "description": "Order 1 for John Doe"},
        {"client": 2, "date": "2024-02-18", "amount": 200.75, "description": "Order 1 for Alice Smith"},
        {"client": 3, "date": "2024-02-19", "amount": 150.25, "description": "Order 1 for Bob Johnson"},
        {"client": 4, "date": "2024-02-19", "amount": 75.50, "description": "Order 1 for Emma Davis"},
        {"client": 5, "date": "2024-02-20", "amount": 120.00, "description": "Order 1 for Michael Wilson"},
        {"client": 6, "date": "2024-02-20", "amount": 180.60, "description": "Order 1 for Sophia Brown"},
        {"client": 7, "date": "2024-02-21", "amount": 90.75, "description": "Order 1 for David Martinez"},
        {"client": 8, "date": "2024-02-21", "amount": 250.00, "description": "Order 1 for Olivia Rodriguez"},
        {"client": 9, "date": "2024-02-22", "amount": 300.30, "description": "Order 1 for William Lee"},
        {"client": 10, "date": "2024-02-22", "amount": 175.25, "description": "Order 1 for Ava Gonzalez"}
    ]

    db.connect()
    for client_data in clients_data:
        Client.create(**client_data)

    for order_data in orders_data:
        Order.create(**order_data)
    db.close()

# Функция для отображения содержимого таблицы
def show_table(table_name):
    db.connect()
    if table_name == "CLIENTS":
        for client in Client.select():
            print(f"{client.name}\t{client.city}\t{client.address}")
    elif table_name == "ORDERS":
        for order in Order.select():
            print(f"{order.client}\t{order.date}\t{order.amount}\t{order.description}")
    db.close()

import sys

# Распределение действий в зависимости от переданных параметров
if len(sys.argv) == 1:
    print("Usage:")
    print(" init - to create the database")
    print(" fill - to fill the database with test data")
    print(" show [table_name] - to show the content of the specified table")

elif len(sys.argv) > 1:
    if sys.argv[1] == "init":
        initialize_database()
    elif sys.argv[1] == "fill":
        fill_database()
    elif sys.argv[1] == "show":
        if len(sys.argv) == 3:
            show_table(sys.argv[2])
        else:
            print("Please provide table name to show its contents.")
