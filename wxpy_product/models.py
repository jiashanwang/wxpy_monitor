# coding: utf-8
from sqlalchemy import Column, DateTime, Float, Integer, String, Text
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()



class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255), info='????????????????')
    username = db.Column(db.String(255))
    nickname = db.Column(db.String(255), info='????')
    phone = db.Column(db.String(255))
    wechat = db.Column(db.String(255), info='???')
    wx_qrcode = db.Column(db.String(255), info='?????????????????????????')
    now_price = db.Column(db.Float(10))
    old_price = db.Column(db.Float(10))
    group_introduction = db.Column(db.Text, info='????')
    pay_introduction = db.Column(db.Text, info='????')
    admin_introduction = db.Column(db.String(255), info='????')
    admin_title = db.Column(db.String(255), info='????')
    mask = db.Column(db.String(255), info='?????????????????????')
    subject_title = db.Column(db.String(255), info='?????????')



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255), nullable=False, info='????????????SaaS???????????????????????????')
    phone = db.Column(db.String(255), info='?????')
    merchant_order_number = db.Column(db.String(255), info='?????')
    create_time = db.Column(db.DateTime, info='??????')
    pay_time = db.Column(db.DateTime, info='??????')
    pay_type = db.Column(db.String(255), info='????alipay\\n???wechat')
    qr_price = db.Column(db.Float(8), info='???????????')
    pay_price = db.Column(db.Float(8), info='??????????????')
    cloud_order_number = db.Column(db.String(255), info='?????')
    qr_type = db.Column(db.String(255), info='fixed?????????\\nbusiness???????\\nno_fixed??????????\\noriginal???')
