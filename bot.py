# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import datetime

bot_name = "Bot1"

bot = ChatBot(
    bot_name,
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    database='../database.json',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'Sorry, but  I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)

# Training.
bot.train(['Who was the first man in the space?', 'Not me',
           'How many planets in the Solar System?', '8 planets'])

bot.train(['whats up', 'nothing new, but allright',
           'how are you?', 'Im incrediable',
           'hello', 'hi'])

bot.train(['what is your name?', 'My name is {}'.format(bot_name),
           'who are you?', 'My name is {}'.format(bot_name),
           'where are you?', 'in your computer'])

bot.train(['whats the weather like today?', 'Nice weather'])
bot.train(['what time is it?', datetime.datetime.now().strftime("%H:%M:%S"),
           'what date is it?', datetime.datetime.now().strftime("%A %d %b %Y"),
           ])


def bot_says(bot, message):
    print("{}: {}".format(bot.name, message))


def user_says(user):
    print("{}: ".format(user.name), end='')
    user_text = input()
    return user_text


class User:
    pass
user = User()
user.name = "user"


while True:
    try:
        user_text = user_says(user)
        resp = bot.get_response(user_text)
        bot_says(bot, resp)

    except (KeyboardInterrupt):
        print("\nBye")
        break
