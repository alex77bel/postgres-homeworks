from csv import reader
import psycopg2


def csv_reader(filename: str) -> list[tuple]:
    """
    Получает данные из файла filename, возвращает список кортежей
    """
    data = []
    try:
        with open(filename, encoding='utf-8') as csvfile:
            for row in [*reader(csvfile)]:
                data.append(tuple(row))
    except FileNotFoundError:
        raise FileNotFoundError(f'Отсутствует файл {filename}')
    return data[1:]  # возвращаем данные без заголовка


con_params = dict(
    host="localhost",
    database="north",
    user="postgres",
    password="0112"
)

with psycopg2.connect(**con_params) as con:
    with con.cursor() as cur:
        # Заполняем таблицу 'employees'
        employees_from_csv = csv_reader('./north_data/employees_data.csv')
        cur.executemany("INSERT INTO employees VALUES (default,%s,%s,%s,%s,%s)", employees_from_csv)

        # Заполняем таблицу 'customers'
        customers_from_csv = csv_reader('./north_data/customers_data.csv')
        cur.executemany("INSERT INTO customers VALUES (%s,%s,%s)", customers_from_csv)

        # Заполняем таблицу 'orders'
        orders_from_csv = csv_reader('./north_data/orders_data.csv')
        cur.executemany("INSERT INTO orders VALUES (%s,%s,%s,%s,%s)", orders_from_csv)

con.close()
