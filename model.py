import json
from test import Test
from users_interface import Ui
from question import Question
from readjson import ReadJson

if __name__ == '__main__':

    ReadJson.chose_test()
    Ui.command_message()
    Ui.input_command()