# coding:utf-8

from db_manager import db

# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(100), nullable=False)
#     pwd = db.Column(db.String(100), nullable=False)
#     imageurl = db.Column(db.String(200), nullable=False)
#     mobile = db.Column(db.String(11), nullable=False)




# class Article(db.Model):
#     __tablename__ = 'article'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(100), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     author = db.relationship('User', backref=db.backref('articles'))
#
#
# student_teacher = db.Table('student_teacher',
#                            db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
#                            db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'), primary_key=True)
#                            )

# class Student(db.Model):
#     __tablename__ = 'student'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(100), nullable=False)
#
#     teachers = db.relationship('Teacher', secondary=student_teacher, backref=db.backref('students'))
#
# class Teacher(db.Model):
#     __tablename__ = 'teacher'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(100), nullable=True)

class User(db.Model):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=True)
    pwd = db.Column(db.String(100), nullable=True)
    mobile = db.Column(db.String(11), nullable=True)

class BillOrder(db.Model):
    __tablename__ = "tb_bill_order"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.String(100), nullable=True)
    method = db.Column(db.Integer)
    bill_type = db.Column(db.Integer)
    title = db.Column(db.String(100), nullable=True)
    content = db.Column(db.String(100), nullable=True)
    remarks = db.Column(db.String(200), nullable=True)
    amount = db.Column(db.Float)
    ctime = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

class BillMethod(db.Model):
    __tablename__ = "tb_bill_method"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)
