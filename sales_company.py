

import requests

from api_test.common.Payload import ReqBody
from api_test.interface_common.common import Common
# env_webtest=http://webtest.datauseful.com
# env_web=https://web.datauseful.com

class CompanySales:
    def company_sales_analysis(self,company_id):
        '需求商机接口'
        req = {
            "method":"POST",
            "url":self.host + "/data/v2/api/company/sales/analysis",
            "headers":ReqBody.header_body(self.environ),
            "json":{
                "meta":ReqBody.req_body(),
                "data":{
                    "company_id":company_id
                }
            }
        }


        res = self.send_api(req)
        return res.json()



    def company_sales_analysis1(self):
        '需求商机接口'
        url  = "http://webtest.datauseful.com/data/v2/api/company/sales/analysis"
        header = {
            "Content-Type": "application/json",
            "cli-iden": 'hogKAD/FEcC+KDcTS3M9uABJeLb7IB9iNqh0tvQWbNPrtBBOMPqeaYR6kIxNiYwlpwzVcJ4omavHQYDdF0/lc6R2cimYS/uEoACASNM8dnAWekcPxaEAiqqUjxz5P6QQHUI3VYGU5dx6ieDWBO608EWFlMSybYlXOevEU9NpVLvTaLyGclUaTypkMmk0y96+YMVLJPeXs0AJE0tjUGxgFn+y/PH5r16C5vIG7JE9uEgqtWE5qWPynZR4oq1AAYswoAdXkK4ai1IZ3jzJMuCi8A==',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400'
        }
        r = requests.post(url=url,headers=header)



    def company_sales_business_analysis(self,company_id):
        '业务分析接口'
        req = {
            "method":"POST",
            "url":self.host + "/data/v2/api/company/sales/business_analysis",
            "headers":ReqBody.header_body(self.environ),
            "json":{
                "meta":ReqBody.req_body(),
                "data":{
                    "company_id":company_id
                }
            }
        }


        res = self.send_api(req)
        return res.json()


    def company_sales_partner(self,company_id):
        '合作伙伴接口'
        req = {
            "method":"POST",
            "url":self.host + "/data/v2/api/company/sales/partner",
            "headers":ReqBody.header_body(self.environ),
            "json":{
                "meta":ReqBody.req_body(),
                "data":{
                    "company_id":company_id
                }
            }
        }

        res = self.send_api(req)
        return res.json()





# print(CompanySales().company_sales_partner('6639518870284772424'))








