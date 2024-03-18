from peewee import *    
import argparse

db = SqliteDatabase("database.db")


class CLIENTS(Model):
    NAME = CharField()
    CITY = CharField()
    ADDRESS = CharField()

    class Meta:
        database = db
        table_name = "Clients"


class ORDERS(Model):
    CLIENT = ForeignKeyField(CLIENTS)
    DATE = DateField()
    AMOUNT = IntegerField()
    DESCRIPTION = CharField()

    class Meta:
        database = db
        table_name = "Orders"


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


def pretty_print(*args, FIRST=False):
    MAX = 12
    data = []
    for arg in args:
        if len(arg) > MAX:
            data.append(arg[:MAX])
        else:
            data.append(arg + (" " * (MAX - len(arg))))
    print(" | ".join(data))
    if FIRST:
        print("_" * ((MAX + 3) * len(args)))


def init():
    if db.get_tables():
        db.drop_tables([CLIENTS, ORDERS])
    db.create_tables([CLIENTS, ORDERS])


def fill():
    for i in range(10):
        order_data = orders_data[i].copy()
        order_data["CLIENT"] = CLIENTS.create(**clients_data[i])
        ORDERS.create(**order_data)


def show(tablename):
    table = {"orders": ORDERS, "clients": CLIENTS}[tablename]
    pretty_print(*table._meta.sorted_field_names, FIRST=True)
    for i in table.select():
        # print(f"{i.CLIENT} | {i.DATE} | {i.AMOUNT} | {i.DESCRIPTION}")
        pretty_print(
            *tuple(str(getattr(i, field)) for field in table._meta.sorted_field_names)
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
    parser.add_argument("parametr", help="Параметр, что необходимо сделать, возможные значения: init, fill, show")
    parser.add_argument("tablename", nargs="?", default="")
    try:
        args = parser.parse_args()
    except SystemExit:
        print("Использование: python лаба1.py init/fill/show [tablename]\n\ninit инициализирует базу данных\nfill заполняет базу данных случайными данными\nshow [tablename] показывает таблицу из базы данных")
        quit(1)
    parametr = args.parametr.lower()
    tablename = args.tablename.lower()
    if parametr not in ("init", "fill", "show"):
        parser.error("Возможные значения parametr: init, fill, show")
    if parametr == "show" and tablename not in ("orders", "clients"):
        parser.error("show требует название таблицы, возможные значения: orders, clients")
    args = [tablename] if tablename else []
    db.connect()
    try:
        {"init": init, "fill": fill, "show": show}[parametr](*args)
    finally:
        db.close()
