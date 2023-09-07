from datetime import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import pytest

from api_test.common.Mail import TestMail
from run import Main


def task_run():
    """
    测试运行入口
    """
    pytest.main(["-vs", "--alluredir", Main().get_path()])

def task_send_email():
    """
    发送邮件
    """
    TestMail().send_email()


def func():
    # 创建调度器BlockingScheduler()
    scheduler = BlockingScheduler()
    #每天晚上十点执行定时任务
    scheduler.add_job(task_run,'cron',day='*',hour=21)
    scheduler.add_job(task_send_email,'cron',day='*',hour=22)
    scheduler.start()


func()