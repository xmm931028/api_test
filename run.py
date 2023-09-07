
import os
import pytest

from api_test.common.Mail import TestMail


class Main:

    @classmethod
    def get_path(self):
        project_path = os.path.dirname(__file__)
        html = os.path.join(project_path, "result", "html")
        return html


    def run(self):
        # """
        # 测试运行入口
        # """
        pytest.main(["-vs","--alluredir",Main().get_path()])
        os.system("allure generate ./result/html -o result/report --clean")






if __name__ == '__main__':
    print(Main().run())
    # print(Main().get_path())



