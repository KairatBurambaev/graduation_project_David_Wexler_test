

class Guest:
    def __init__(self, surename, name, patronymic, age_year, age_month):
        self.surename = surename
        self.name = name
        self.patronymic = patronymic
        self.age_year = age_year
        self.age_month = age_month
        self.result = {}

    def add_result(self, test, result):
        self.result[f'{test}'] = result

    def as_dict(self):
        return {
            'surename': self.surename,
            'name': self.name,
            'patronymic': self.patronymic,
            'age': str(self.age_year) + ' year ' + str(self.age_month) + ' month',
            'result': self.result
        }