from flask import Flask, redirect, url_for, request, render_template

import config
from flask_sqlalchemy import SQLAlchemy

from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/uploads'  #文件存放路径
ALLOWED_EXTENSIONS = set(['jpg']) #限制上传文件格式

app = Flask(__name__)
app.config.from_object(config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
db = SQLAlchemy(app)

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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/pd-bi-log-service/UploadFileServlet', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:

            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':

            return redirect(request.url)
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, '/Users/wanglitao/Desktop/author_book',
                                   secure_filename(file.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        file.save(upload_path)
    return ''


if __name__ == '__main__':
    app.run()
