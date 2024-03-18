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
        {"name": "Rosa McBride", "city": "Brest", "address": "352 Main St"},
        {"name": "Bernice Young", "city": "Krakow", "address": "345 Elm St"},
        {"name": "Bob Johnson", "city": "Mexico", "address": "544 Oak St"},
        {"name": "Jerry Haynes", "city": "San Francisco", "address": "234 Pine St"},
        {"name": "Willie Lyons", "city": "New York", "address": "86 Maple St"},
        {"name": "Sharon Baker", "city": "Seoul", "address": "12 Palm St"},
        {"name": "Marie Stanley", "city": "Toronto", "address": "242 Cedar St"},
        {"name": "Carol Lopez", "city": "Boston", "address": "54 Spruce St"},
        {"name": "Johnny Kelly", "city": "Prague", "address": "346 Birch St"},
        {"name": "Olga Mills", "city": "Tokyo", "address": "856 Walnut St"}
    ]

      orders_data = [
        {"client": 1, "date": "2024-03-01", "amount": 90.80, "description": "Order 1 for Rosa McBride"},
        {"client": 2, "date": "2024-03-02", "amount": 140.75, "description": "Order 1 for Bernice Young"},
        {"client": 3, "date": "2024-03-03", "amount": 2700.25, "description": "Order 1 for Bob Johnson"},
        {"client": 4, "date": "2024-03-04", "amount": 95.40, "description": "Order 1 for Jerry Haynes"},
        {"client": 5, "date": "2024-03-05", "amount": 320.00, "description": "Order 1 for Willie Lyons"},
        {"client": 6, "date": "2024-03-06", "amount": 180.80, "description": "Order 1 for Sharon Baker"},
        {"client": 7, "date": "2024-03-07", "amount": 180.35, "description": "Order 1 for Marie Stanley"},
        {"client": 8, "date": "2024-03-08", "amount": 280.00, "description": "Order 1 for Carol Lopez"},
        {"client": 9, "date": "2024-03-09", "amount": 30.50, "description": "Order 1 for Johnny Kelly"},
        {"client": 10, "date": "2024-03-10", "amount": 155.35, "description": "Order 1 for Olga Mills"}
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
