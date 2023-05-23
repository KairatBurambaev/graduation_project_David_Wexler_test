from test import Test

class Start:

    def start_test(id):
        
        test = str(input('Выберите тест: '))

        new_test = Test(test)
        new_test.read_test()

        for elem in new_test.questions:
            print(elem.quest)