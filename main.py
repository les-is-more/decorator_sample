#!/usr/local/bin/python3

import string, os
from db.connection import Connection
from db.schema import account_schema
from utils.consprint import ConsolePrinter
from utils.router import Router
Connection(':memory:').createTable(**account_schema)
kwargs_keys = ["name", "age", "password", "coins", "user_type", "coin_limit", "initial_bet", "reward"]


# define the router decorator
class Session:
    __consoleMainOptions = ['PLAY','QUIT']

    def __init__(self):
        self.currMod ='intro'

    @Router.default('home')
    def Introduction(self):
        modTitle = "MINI-CASINO"
        modDesc = "Welcome to the {}! This is an experimental game, accessed through the terminal. The game can only played with an account, so please sign up or login using account.".format(moduleTitle.title())
        modKeyMap = {}
        return input('Press Letter: ')

    @Router.special('register')
    def Registration(self):
        #should have an interactive feature
        modTitle = "ACCOUNT REGISTRATION"
        modDesc = "Please login."
        return input('Press Letter: ')

    @Router.default('login')
    def Login(self):
        pass

    @Router.special('')
    def Main(self):
        while True:
            os.system('clear')


if __name__ == '__main__':
    Session().Main()


## Notes to do:

## 1. Can we write to a base dictionary that will write a session file or log containing some important info
## 2. Create a nav class, that will have it's own properties, esp the keymap props
## 3. Create a simple, top of mind keymapper and possible
