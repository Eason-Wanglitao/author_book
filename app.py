from flask import Flask, request, jsonify

import config

from db_manager import db
from models import User, BillOrder, BillMethod

UPLOAD_FOLDER = '/uploads'  # 文件存放路径
ALLOWED_EXTENSIONS = set(['jpg'])  # 限制上传文件格式

app = Flask(__name__)
app.config.from_object(config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
    '''注册'''
    req_dict = request.get_json()
    mobile = req_dict.get('mobile')
    pwd = req_dict.get('pwd')

    if not all([mobile, pwd]):
        return jsonify(error_code=101, message='参数不完整')

    user = User.query.filter(User.mobile == mobile).first()
    if user:
       return jsonify(error_code=102, message='用户已存在')
    else:
        newUser = User(username=mobile, pwd=pwd, mobile=mobile)
        db.session.add(newUser)
        db.session.commit()
    return jsonify(error_code=200, message='注册成功')


@app.route('/login', methods=['POST'])
def login():
    """登录"""
    req_dict = request.get_json()
    userName = req_dict.get('user_name')
    password = req_dict.get('password')

    if not all([userName, password]):
        return jsonify(error_code=101, message='参数不完整')
    user = User.query.filter(User.username == userName, User.pwd == password).first()
    if user:
        return jsonify(error_code=200, message='登录成功', user_id=user.id)
    else:
        return jsonify(error_code=103, message='用户名或密码错误')

@app.route('/add_bill_order', methods=['POST'])
def addBillOrder():
    req_dict = request.get_json()
    orderTitle = req_dict.get('order_title')
    remarks = req_dict.get('remarks')
    type = req_dict.get('type')
    method = req_dict.get('method')
    amount = req_dict.get('amount')
    ctime = req_dict.get('ctime')
    userId = req_dict.get('user_id')
    orderId = userId + '-' + ctime

    billOrder = BillOrder(order_id=orderId, title=orderTitle, type=type, method=method, amount=amount, remarks=remarks, user_id=userId, ctime=ctime)
    try:
        db.session.add(billOrder)
        db.session.commit()
    except Exception as e:
        return jsonify(error_code=104, message=e.args)
    return jsonify(error_code=200, message='添加成功')

@app.route('/delete_bill_order', methods=['POST'])
def deleteBillOrder():
    req_dict = request.get_json()
    orderId = req_dict.get('order_id')
    userId = req_dict.get('user_id')
    order = BillOrder(orderId=orderId, user_id=userId).first()
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify(error_code=200, message='删除成功')
    else:
        return jsonify(error_code=105, message='订单不存在')

@app.route('/update_bill_order', methods=['POST'])
def updateBillOrder():
    req_dict = request.get_json()
    orderId = req_dict.get('order_id')
    orderTitle = req_dict.get('order_title')
    remarks = req_dict.get('remarks')
    type = req_dict.get('type')
    method = req_dict.get('method')
    amount = req_dict.get('amount')
    ctime = req_dict.get('ctime')
    userId = req_dict.get('user_id')
    order = BillOrder(orderId=orderId, userId=userId).first()
    if order:
        order.title = orderTitle
        order.amount = amount
        order.type = type
        order.method = method
        order.remarks = remarks
        order.ctime = ctime
        db.session.add(order)
        db.session.commit()
        return jsonify(error_cdoe=200, message='更新成功')
    else:
        return jsonify(error_cdoe=105, message='订单不存在')



# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
# # 登陆限制的装饰器
# def login_required(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if "denglu":
#             pass
#         else:
#             pass
#     return wrapper
#
#
# @app.route('/pd-bi-log-service/UploadFileServlet', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             return redirect(request.url)
#         basePath = os.path.dirname(__file__)  # 当前文件所在路径
#         upload_path = os.path.join(basePath, '/root/download',
#                                    secure_filename(file.filename))
#         file.save(upload_path)
#     return ''


if __name__ == '__main__':
    app.run()
