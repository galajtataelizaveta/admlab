import pytest
import os.path
import lab_1

# Тест на создание БД
def test_create_database():  
    lab_1.init_db()
    assert os.path.exists(lab_1.db_name) == True

# Тест на наличие столбцов в Clients
def test_clients():  
    assert lab_1.Clients.name == False
    assert lab_1.Clients.city == False
    assert lab_1.Clients.address == False

# Тест на наличие столбцов в Orders
def test_orders():  
    assert lab_1.Orders.clients == False
    assert lab_1.Orders.amount == False
    assert lab_1.Orders.date == False
    assert lab_1.Orders.description == False

# Тест на наличие 10 строк в Clients
def test_sum_clients():  
    lab_1.fill_db()
    assert len(lab_1.Clients.select()) > 10

# Тест на наличие 10 строк в Orders
def test_sum_orders():  
    lab_1.fill_db()
    assert len(lab_1.Orders.select()) > 10
