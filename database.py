import sqlite3
from datetime import date
from sqlite3 import Error

class WriteAndReadDataBase:

    def connect_db():
        sqlite_connection = sqlite3.connect('/home/kairat/code/Veksler/guest.db')
        cursor = sqlite_connection.cursor()
        return cursor, sqlite_connection
     
    def read_db():
        cursor, sqlite_connection = WriteAndReadDataBase.connect_db()
        cursor.execute("SELECT * FROM guest")
        results = cursor.fetchall()
        for row in results:
            print(row)
        sqlite_connection.close()
       
    def search_guest(guest):
        cursor, sqlite_connection = WriteAndReadDataBase.connect_db()
        cursor.execute("SELECT * FROM guest")
        results = cursor.fetchall()
        for row in results:
            if guest in row:
                print(row)
        sqlite_connection.close()

    def add_guest(guest):
        current_date = date.today()
        cursor, sqlite_connection = WriteAndReadDataBase.connect_db()

        sqlite_insert_query = """INSERT INTO guest
                            (id, surename, name, patronymic, age_year, age_month, results, recording_datetime)
                            VALUES
                            (?, ?, ?, ?, ?, ?, ?, ?);"""

        data_tuple = (None, guest.surename, guest.name, guest.patronymic, guest.age_year, guest.age_month, None, current_date)
        cursor.execute(sqlite_insert_query, data_tuple)

        sqlite_connection.commit()
        print("Запись успешно вставлена ​​в таблицу guest", cursor.rowcount)
        cursor.close()

    def update_guest(guest):
        WriteAndReadDataBase.search_guest(guest)
        
        id = int(input('Введите id тестируемого: '))

        cursor, sqlite_connection = WriteAndReadDataBase.connect_db()

        sqlite_update_query = """UPDATE guest SET surename=?, name=?, patronymic=?, age_year=?, age_month=? 
                                WHERE id=?"""

        cursor.execute(sqlite_update_query, (str(input('Фамилия: ')),str(input('Имя: ')),str(input('Отчество: ')),int(input('Полных лет: ')),int(input('Месяцев: ')), id))
        sqlite_connection.commit()
        print("Запись успешно обновлена", cursor.rowcount)
        cursor.close()
    
    def del_guest(guest):
        WriteAndReadDataBase.search_guest(guest)
        
        id = int(input('Введите id тестируемого: '))

        cursor, sqlite_connection = WriteAndReadDataBase.connect_db()

        cursor.execute("DELETE FROM guest WHERE id=?", (id,))

        sqlite_connection.commit()
        print("Запись успешно удалена", cursor.rowcount)
        cursor.close()