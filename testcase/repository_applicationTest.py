import readConfig
from common import configHttpC
import unittest
import json
from common.Log import Log
from common.StringUtils import get_now

localReadConfig = readConfig.ReadConfig()
url = localReadConfig.get_utms("utms_api")
log = Log()
repoName=get_now()

class repository_application(unittest.TestCase):
    ''' UTMS 应用类别管理'''

    @classmethod
    def setUpClass(self):
        print("start.......")
        globals()["repoId"]='0'

    @classmethod
    def tearDownClass(self):
        print("end.....")

    def test_1_repository_applicationadd(self):
        ''' 新增应用类别'''
        log.info("开始test_1_repository_applicationadd")
        urlnew = url + 'repository_application'
        log.info("请求地址"+urlnew)
        headers = {'Content-Type': 'application/json'}
        data = {"repoId":0,"repoName":repoName,"sort":0,"remark":'name'+repoName}
        run = configHttpC.ConfigHttpC(urlnew, params=None, data=json.dumps(data), headers=headers, method='POST')
        log.info(run.response)
        respCode=run.response['respCode']
        self.assertEqual("0000",respCode)


    def test_2_repository_applicationsearch(self):
        ''' 查询应用类别'''
        log.info("开始test_2_repository_applicationedit")
        urlnew = url + 'repository_application?current=1&size=10&repoName='+repoName
        log.info("请求地址"+urlnew)
        headers = {'Content-Type': 'application/json'}
        run = configHttpC.ConfigHttpC(urlnew, params=None, data=None, headers=headers, method='GET')
        log.info(run.response)
        globals()["repoId"]=run.response['data']['records'][0]['repoId']
        log.info(globals()["repoId"])
        respCode = run.response['respCode']
        self.assertEqual("0000", respCode)

    def test_3_repository_applicationedit(self):
        ''' 修改应用类别'''
        log.info("开始test_3_repository_applicationedit")
        log.info(globals()["repoId"])
        if globals()["repoId"] == '0':
            self.assertFalse("repoId不存在")
        urlnew = url + 'repository_application/' + globals()["repoId"]
        # urlnew = url + 'repository_application/500960652742225920'
        log.info("请求地址" + urlnew)
        headers = {'Content-Type': 'application/json'}
        data = {"repoId": globals()["repoId"], "repoName": repoName, "sort": 0, "remark": 'autotest'+get_now()}
        run = configHttpC.ConfigHttpC(urlnew, params=None, data=json.dumps(data), headers=headers, method='PUT')
        log.info(run.response)
        respCode = run.response['respCode']
        self.assertEqual("0000", respCode)

    def test_4_repository_applicationenable(self):
        ''' 停用应用类别'''
        log.info("开始test_4_repository_applicationenable")
        log.info(globals()["repoId"])
        if globals()["repoId"] == '0':
            self.assertFalse("repoId不存在")
        urlnew = url + 'repository_application/' + globals()["repoId"]+'/enable'
        log.info("请求地址" + urlnew)
        headers = {'Content-Type': 'application/json'}
        data = {"enable":False}
        run = configHttpC.ConfigHttpC(urlnew, params=None, data=json.dumps(data), headers=headers, method='PATCH')
        log.info(run.response)
        respCode = run.response['respCode']
        self.assertEqual("0000", respCode)



if __name__ == "__main__":
      # tools.test_tools3(1);
      # suite = unittest.TestSuite()
      # suite.addTest(repository_application("repository_applicationadd"))
      # runner = unittest.TextTestRunner()
      # runner.run(suite)
      unittest.main();


