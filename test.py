import pytest
from lab_1 import init, fill, show, db, ORDERS, CLIENTS
from peewee import *
from os.path import exists

def test_init():
    db.connect()
    init()
    assert exists("database.db")
    db.close()

def test_init_second_time():
    db.connect()
    init()
    assert exists("database.db")
    db.close()

def test_show_empty():
    db.connect()
    for tablename in ("clients", "orders"):
        show(tablename)
    db.close()

def test_fill():
    db.connect()
    for i in range(25):
        fill()
    assert CLIENTS.select().count() >= 10
    db.close()

def test_show():
    db.connect()
    for tablename in ("clients", "orders"):
        show(tablename)
    db.close()


