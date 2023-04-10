from database import WriteAndReadDataBase
from guest import Guest

class Ui:

    def command_message():
        print('Новый тестируемый: 1')
        print('Найти тестируемого: 2')
        print('Изменить данные тестируемого: 3')
        print('Удалить тестируемого: 4')
        print('Вывести список тестируемых: 5')
        print('Закончить работу: 0')
    
    def input_command():
        num = int(input('Введите номер действия: '))

        match num:
            case 1:
                new_guest = Guest(str(input('Фамилия: ')),str(input('Имя: ')),str(input('Отчество: ')),int(input('Полных лет: ')),int(input('Месяцев: ')))
                WriteAndReadDataBase.add_guest(new_guest)
                Ui.input_command()
            case 2:
                WriteAndReadDataBase.search_guest(str(input('Введите Имя, Фамилию или Отчество: ')))
                Ui.input_command()
            case 3:
                WriteAndReadDataBase.update_guest(str(input('Введите Имя, Фамилию или Отчество: ')))
                Ui.input_command()
            case 4:
                WriteAndReadDataBase.del_guest(str(input('Введите Имя, Фамилию или Отчество: ')))
                Ui.input_command()
            case 5:
                WriteAndReadDataBase.read_db()
                Ui.input_command()
            case 0:
                print('Досвидание!')
                exit()