from distutils.cmd import Command
from multiprocessing import managers

from pip import main
from app import create_app
from flask import Flask
from flask_script import Manager,Server



app = create_app('development')


manager= Manager(app)
manager.add_command('server', Server)



if __name__ == '__main__':
    manager.run()