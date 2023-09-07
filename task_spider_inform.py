#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author:
@file: bid_for_bidInfo.py
@time: 2022/8/17 16:09
@desc: 爬虫数据采集情况通知
"""

import json
import pymysql
from datetime import datetime,timedelta
from feapder.db.mysqldb import MysqlDB
from feapder.utils.log import log
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

online = True

if online:
    MYSQL_IP = "10.9.2.78"
    MYSQL_USER_NAME = "root"
    MYSQL_USER_PASS = "tianzhuanjiawa_009"
    MYSQL_PORT = 3306
    MYSQL_DB = "spider"

    APP_MYSQL_IP = "172.16.196.21"
    APP_MYSQL_USER_NAME = "root"
    APP_MYSQL_USER_PASS = "QJpSWTZBZtTCHsM5"
    APP_MYSQL_PORT = 3306
    APP_MYSQL_DB = "data"
else:
    MYSQL_IP = "106.75.108.206"
    MYSQL_USER_NAME = "root"
    MYSQL_USER_PASS = "tianzhuanjiawa_009"
    MYSQL_PORT = 3307
    MYSQL_DB = "spider"

db = MysqlDB(
    ip=MYSQL_IP, port=MYSQL_PORT, db=MYSQL_DB, user_name=MYSQL_USER_NAME, user_pass=MYSQL_USER_PASS,
)

bid_db = MysqlDB(
    ip=APP_MYSQL_IP, port=APP_MYSQL_PORT, db=APP_MYSQL_DB, user_name=APP_MYSQL_USER_NAME, user_pass=APP_MYSQL_USER_PASS,
)


def sendMail(message, Subject, sender_show, recipient_show, to_addrs, cc_show=''):
    '''
    :param message: str 邮件内容
    :param Subject: str 邮件主题描述
    :param sender_show: str 发件人显示，不起实际作用如："xxx"
    :param recipient_show: str 收件人显示，不起实际作用 多个收件人用','隔开如："xxx,xxxx"
    :param to_addrs: str 实际收件人
    :param cc_show: str 抄送人显示，不起实际作用，多个抄送人用','隔开如："xxx,xxxx"
    '''


    user = 'linjian@datauseful.com'
    password = 'sZVHn4iloe5Ri2Oi'


    msg = MIMEText(message, 'html', _charset="utf-8")
    # 邮件主题描述
    msg["Subject"] = Subject
    # 发件人显示，不起实际作用
    msg["from"] = sender_show
    # 收件人显示，不起实际作用
    msg["to"] = recipient_show
    # 抄送人显示，不起实际作用
    msg["Cc"] = cc_show
    with SMTP_SSL(host="smtp.feishu.cn", port=465) as smtp:
        # 登录发邮件服务器
        smtp.login(user=user, password=password)
        # 实际发送、接收邮件配置
        smtp.sendmail(from_addr=user, to_addrs=to_addrs.split(','), msg=msg.as_string())


def timestamp_for_date(timestamp,formatter="%Y-%m-%d %H:%M:%S"):
    date = datetime(1970, 1, 1) + timedelta(seconds=timestamp) + timedelta(hours=8)

    data_strf = date.strftime(formatter)
    return data_strf

def statement_result(sql):
    mdb = pymysql.connect(host=MYSQL_IP,port=MYSQL_PORT,user=MYSQL_USER_NAME,passwd=MYSQL_USER_PASS,db=MYSQL_DB)

    df = pd.read_sql(sql, con=mdb)
    mdb.close()
    return df.to_html()


def task_inform():
    sql = '''select page,tag,source,cntSql,remark from task_spider_inform where active=0'''
    tasks = db.find(sql)

    message = ''
    for page,tag,source,cntSql,remark in tasks:
        log.info(f'获取{tag}数据。。。')

        html = statement_result(cntSql)
        message = message + f'<div>页面:{page}</div>'
        message = message + f'<div>模块:{tag}</div>'
        message = message + f'<div>数据源:{source}</div>'
        if remark:
            message = message + f'<div>注:{remark}</div>'
        message = message + html
        message = message + '<br><br><br>'
        log.info('数据获取结束。。。')
    log.info('开发发送邮件。。。。')
    Subject = '爬虫每日数据统计'
    # 显示发送人
    sender_show = 'linjian@datauseful.com'
    # 显示收件人
    recipient_show = 'linjian@datauseful.com'
    # 实际发给的收件人
    to_addrs = 'linjian@datauseful.com,wangdakan@datauseful.com,yeshuai@datauseful.com'
    sendMail(message, Subject, sender_show, recipient_show, to_addrs)
    log.info('邮件发送成功。。。')

if __name__ == "__main__":
    task_inform()