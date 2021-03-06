import sqlite3
import traceback
import sys

try:
    sql_conn = sqlite3.connect('ChainCarDealerships.db')

    query_carDealerships = '''CREATE TABLE carDealerships 
    (id INTEGER PRIMARY KEY,
    name_carShowroom TEXT NOT NULL, 
    FOREIGN KEY (cars_id) REFERENCES cars(id) ON DELETE CASCADE ON UPDATE);'''

    query_cars = '''CREATE TABLE cars
    (id INTEGER PRIMARY KEY,
    name_car TEXT NOT NULL, 
    number_of_cars INTEGER, 
    FOREIGN KEY (car_dealerships_id) 
    REFERENCES car_dealerships(id) 
    ON DELETE CASCADE ON UPDATE);'''

    query_network_cars = '''CREATE TABLE network_cars 
    (id INTEGER PRIMARY KEY,
    name_network TEXT NOT NULL);'''

    cursor = sql_conn.cursor()

    # cursor.execute(query_car_dealerships)

    # sql_conn.commit()

    cursor.execute(query_carDealerships)

    sql_conn.commit()

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite:", error)
    print("Класс исключения:", error.__class__)
    print("Исключение", error.args)
    print("Печать подробностей исключения SQLite: ")
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if(sql_conn):
        sql_conn.close()
        print("Соединение с SQLite закрыто")