import pytest
import os.path
import main

# Тест на создание БД
def test_create_database():  
    main.init_db()
    assert os.path.exists(main.db_name) == True

# Тест на наличие столбцов в Clients
def test_clients():  
    assert main.Clients.name == False
    assert main.Clients.city == False
    assert main.Clients.address == False

# Тест на наличие столбцов в Orders
def test_orders():  
    assert main.Orders.clients == False
    assert main.Orders.amount == False
    assert main.Orders.date == False
    assert main.Orders.description == False

# Тест на наличие 10 строк в Clients
def test_sum_clients():  
    main.fill_db()
    assert len(main.Clients.select()) > 10

# Тест на наличие 10 строк в Orders
def test_sum_orders():  
    main.fill_db()
    assert len(main.Orders.select()) > 10
