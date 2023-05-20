import json

class ReadJson:

    def __init__(self):
        data = self.read_json()
        self.data = data

    def read_json(self):
        with open('Tests/Tests.json') as file:
            data = json.load(file)
        return data