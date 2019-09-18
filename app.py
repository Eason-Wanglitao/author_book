from flask import Flask, redirect, url_for

import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return redirect('/login/')
    return 'Hello World!'


@app.route('/login/')
def login():
    return '这是登录页面'

@app.route('/article/<id>')
def article(id):
    return '参数是%s' % id


if __name__ == '__main__':
    app.run()
