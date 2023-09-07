from datetime import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import pytest

from api_test.common.Mail import TestMail
from run import Main


def task_run():
    """
    �����������
    """
    pytest.main(["-vs", "--alluredir", Main().get_path()])

def task_send_email():
    """
    �����ʼ�
    """
    TestMail().send_email()


def func():
    # ����������BlockingScheduler()
    scheduler = BlockingScheduler()
    #ÿ������ʮ��ִ�ж�ʱ����
    scheduler.add_job(task_run,'cron',day='*',hour=21)
    scheduler.add_job(task_send_email,'cron',day='*',hour=22)
    scheduler.start()


func()