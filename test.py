from question import Question
from readjson import ReadJson

RJ = ReadJson()

class Test:
    def __init__(self, test_name):
        self.test_name = test_name
        self.questions = []
        data = RJ.read_json()
        self.data = data
        
    def add_questions(self, quest):
        if quest not in self.questions:
            self.questions.append(quest)
        return self.questions
        
    def read_test(self):
        test = self.data[f'{self.test_name}']
        for elem in test:
            for k,v in elem.items():
                if k == 'quest':
                    q = v
                elif k == 'answer_true':
                    t = v
                elif k == 'answer_false':
                    f = v
            quest = Question(q,t,f)
            self.add_questions(quest)