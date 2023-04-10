

class Test:
    def __init__(self, test_name):
        self.test_name = test_name,
        self.questions = []

    def add_questions(self, quest):
        if quest not in self.questions:
            self.questions.append(quest)