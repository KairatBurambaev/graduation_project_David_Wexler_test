import sqlite3
from datetime import date
from sqlite3 import Error

class WriteAndReadDataBase:

    def __init__(self):
        cur, conn = self.connect_db()
        self.cursor = cur
        self.sqlite_connection = conn

    def connect_db(self):
        sqlite_connection = sqlite3.connect('/home/kairat/code/Veksler/guest.db')
        cursor = sqlite_connection.cursor()
        return cursor, sqlite_connection
    
    def end_connect(self):
        self.sqlite_connection.close()
     
    def read_db(self):
        self.cursor.execute("SELECT * FROM guest")
        results = self.cursor.fetchall()
        for row in results:
            print(row)
       
    def search_guest(self, guest):
        self.cursor.execute("SELECT * FROM guest")
        results = self.cursor.fetchall()
        for row in results:
            for elem in row:
                if guest in str(elem):
                    print(row)

    def add_guest(self, guest):
        current_date = date.today()

        sqlite_insert_query = """INSERT INTO guest
                            (guest_id, surename, name, patronymic, age_year, age_month, recording_datetime)
                            VALUES
                            (?, ?, ?, ?, ?, ?, ?);"""

        data_tuple = (None, guest.surename, guest.name, guest.patronymic, guest.age_year, guest.age_month, current_date)
        self.cursor.execute(sqlite_insert_query, data_tuple)
        user_id = self.cursor.lastrowid
        
        self.cursor.execute("INSERT INTO test (guest_id) VALUES (?)", (user_id,))

        self.sqlite_connection.commit()
        
        print("Запись успешно вставлена ​​в таблицу guest", self.cursor.rowcount)

    def update_guest(self, guest):
        self.search_guest(guest)
        
        id = int(input('Введите id тестируемого: '))

        sqlite_update_query = """UPDATE guest SET surename=?, name=?, patronymic=?, age_year=?, age_month=? 
                                WHERE guest_id=?"""

        self.cursor.execute(sqlite_update_query, (str(input('Фамилия: ')),str(input('Имя: ')),str(input('Отчество: ')),int(input('Полных лет: ')),int(input('Месяцев: ')), id))
        self.sqlite_connection.commit()
        print("Запись успешно обновлена", self.cursor.rowcount)
    
    def del_guest(self, guest):
        self.search_guest(guest)
        
        id = int(input('Введите id тестируемого: '))

        self.cursor.execute("DELETE FROM guest WHERE guest_id=?", (id,))
        self.cursor.execute("DELETE FROM test WHERE guest_id=?", (id,))

        self.sqlite_connection.commit()
        print("Запись успешно удалена", self.cursor.rowcount)