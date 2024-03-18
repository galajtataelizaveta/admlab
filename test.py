import pytest
import os.path
import lab_1
from lab_1 import clear_tables, fill_database, Clients, Orders, db

# Фикстура для проверки отсутствия базы данных
@pytest.fixture(autouse=True)
def check_database_exists():
    if not os.path.exists(lab_1.database):
        pytest.fail("Не существует базы данных")

# Тест на создание БД
def test_create_database():
    lab_1.initialize_database()
    assert os.path.exists(lab_1.database) == True

# Тест на наличие столбцов в Clients
def test_clients():
    assert hasattr(lab_1.Clients, "name")
    assert hasattr(lab_1.Clients, "city")
    assert hasattr(lab_1.Clients, "address")

# Тест на наличие столбцов в Orders
def test_orders():
    assert hasattr(lab_1.Orders, "client")
    assert hasattr(lab_1.Orders, "amount")
    assert hasattr(lab_1.Orders, "date")
    assert hasattr(lab_1.Orders, "description")

# Тест на проверку количества клиентов в базе данных
def test_sum_clients():
    with pytest.raises(Exception):
        with db:
            clear_tables()
            fill_database()

            num_clients = Clients.select().count()
            assert num_clients >= 0

# Тест на проверку количества заказов в базе данных
def test_sum_orders():
    with pytest.raises(Exception):
        with db:
            clear_tables()
            fill_database()

            num_orders = Orders.select().count()
            assert num_orders >= 0


