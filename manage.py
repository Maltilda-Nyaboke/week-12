from distutils.cmd import Command
from multiprocessing import managers
from app import create_app
from flask import Flask
from flask_script import Manager,Server



app = create_app('development')

app= Flask(__name__)

manager= Manager(app)
manager.add.command(Server, Manager)