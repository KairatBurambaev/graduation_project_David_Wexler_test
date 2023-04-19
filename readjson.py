from question import Question
from test import Test
import json

class ReadJson:

    def __init__(self):
        data = self.read_json()
        self.data = data

    def read_json(self):
        with open('Tests/Tests.json') as file:
            data = json.load(file)
        return data

    def chose_test(self, test_name):

        test_name = self.data[f'{test_name}']

        for quest in test_name:
            for k,v in quest.items():
                if k == 'quest':
                    q = k
                    if k == 'answer_true':
                        t = k
                        if k == 'answer_false':
                            f = k
                            que = Question(q,t,f)
                            test_name = Test.add_questions(que)