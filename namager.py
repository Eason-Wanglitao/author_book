# coding:utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from db_manager import db


manager = Manager(app)

@manager.command
def runserver():
    print('paoqilaile')

#1.要使用Migrate，必须绑定app和db
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()