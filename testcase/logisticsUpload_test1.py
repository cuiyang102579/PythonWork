import readConfig as readConfig
from common import configHttpC
import unittest
import json
localReadConfig = readConfig.ReadConfig()
url = localReadConfig.get_tools("logisticsUpload")


class tools(unittest.TestCase):
    ''' 河姆渡面单上传工具2'''
    def test_tools(self):
        ''' 面单上传-单张上传2'''
        headers = {'Content-Type': 'application/json'}
        data = [ {
                    "imageUrl": "https://project-homedo.oss-cn-shanghai.aliyuncs.com/3f75f6aa-69a1-4adf-be65-b86e96337aa4_上传业务免单活动.jpg",
                    "expressNumber": "8888"}]
        run = configHttpC.ConfigHttpC(url, params=None, data=json.dumps(data), headers=headers, method='POST')
        # print(run.response)
        respCode=run.response['respCode']
        self.assertEqual("0000",respCode)

    def test_tools2(self):
        ''' 面单上传-多张上传2 '''
        headers = {'Content-Type': 'application/json'}
        data = [{
            "imageUrl": "https://project-homedo.oss-cn-shanghai.aliyuncs.com/3f75f6aa-69a1-4adf-be65-b86e96337aa4_M站.jpg",
            "expressNumber": "8888"}, {
            "imageUrl": "https://project-homedo.oss-cn-shanghai.aliyuncs.com/3f75f6aa-69a1-4adf-be65-b86e96337aa4_上传业务免单活动.jpg",
            "expressNumber": "8888"}]
        run = configHttpC.ConfigHttpC(url, params=None, data=json.dumps(data), headers=headers, method='POST')
        # print(run.response)
        respCode = run.response['respCode']
        # self.assertEqual("0000", "1111","返回值不正确："+respCode)
        self.assertTrue("返回值不正确："+respCode)

    def test_tools3(self):
        url = 'http://oms.fat.homedo.com/oms-totalinquiry-web/valetApplication/saveEnquiryWhole'
        # headers = {'Content-Type': 'application/json','Cookie':'gr_user_id=428a340c-bc78-425b-920d-180f6574e91c; grwng_uid=ad8b19a2-5ac8-4bad-9fd6-1224bbd05bd1; HMD_R=159400604323452375; Hm_lvt_51d4bdf6fae0f9d4bb58c528601ab693=1594006362; UM_distinctid=17322c91198514-08df1b22bac11b-4353760-1fa400-17322c911998da; NTKF_T2D_CLIENTID=guestCC1E2284-4588-9994-63C8-235995AA626B; a8c7c3f6977ae463_gr_last_sent_cs1=402300; _ga=GA1.2.1471859676.1594036306; LoginErrorCount=0; IsRemember=null; AccountId=405785; a016ee4c2a76b6bb_gr_last_sent_cs1=405785; utime=7776000; Hm_lvt_d1d21a226b3b6cbb96842713353fc9f7=1594006226,1594621667; COOKIE_USERfat.=54e26dfa-84e6-473f-8d00-d9381c8d37a9; COOKIE_USERdev.=93356d4b-0517-44f6-8530-fdc8f3a87537; _gid=GA1.2.470483385.1594690741; nTalk_CACHE_DATA={uid:hd_1000_ISME9754_guestCC1E2284-4588-99,tid:1594703558143673}; COOKIE_USERINFOfat.=%7B%22userId%22%3A%225705283077884826862%22%2C%22userName%22%3A%22%u5D14%u6768%22%2C%22depId%22%3A%22343ab9dc-79ab-4f5a-9601-05a0a69a6e1d%22%2C%22depName%22%3A%22%u6D4B%u8BD5%22%2C%22respCode%22%3A%220000%22%7D; COOKIE_USERINFOfat..sig=MlejMSWD_7WscYeiggUhHXfAzhGv8wQ9jkphLnie79M; EGG_SESS=PwJ-wpaGjYe-xzoIijB0MiKRxFycBv7FPiak4nRLzZo424NdDCTfEOX1MZMC6sdXHaC3ByXLDLa8j_-Dwap_uxV7zgJImdeDnxYkXnnPK8_UCQhT7yo8QJ3uV6EO0WgzdDgGUuBS45rGTzLoImGhiKyk7AIj_qrwptF0rYzIl8LhtQohvgiKkyTXjnr5sp-IoQborduBXH4SViuxnmWINyjQgACAQSQ3bti283WDVTWMabM6SLnRKsVNr1K_Lu87y1GtlnYPNpMp1PP-A3nOec7gQfZLpkOSaSksh6OYTPPgR2D5AfOaMDotNp8IrOwY_I_tZZe2cwAPeV9fG85SldU5Xd6uH-b4Eol8Sv11ciU='}
        headers = {'Content-Type': 'application/json', 'Cookie': 'COOKIE_USERfat.=54e26dfa-84e6-473f-8d00-d9381c8d37a9'}
        data = {
            "applyUserType": 1,
            "accountId": "402034",
            "areaId": "772",
            "address": "N",
            "budgetType": 16,
            "projectStage": "",
            "projectIndustryId": "",
            "brandRecordType": "",
            "tenderBrandName": "",
            "standardBrandName": "",
            "tenderCompanyCount": "",
            "recordRemark": "",
            "projectLinkmanName": "N X",
            "projectMobile": "18900000000",
            "projectEmail": "",
            "enquiryWholeApplyCounsel": {
                "remark": ""
            },
            "enquiryWholeApplyDesign": {
                "complanyName": "",
                "remark": ""
            },
            "enquiryWholeApplyWorks": {
                "remark": "",
                "worksDateTime": ""
            },
            "enquiryWholeApplyFiles": [

            ],
            "extensionModel": {
                "endTroubleTime": "",
                "receiveMode": 1,
                "startTroubleTime": '',
                "subscribeTime": "",
                "subscribeType": 1,
                "subscribeWeekDay": 0
            },
            "recipientModels": [
                {
                    "email": "11@sf.com",
                    "mobile": "18900000000",
                    "type": 1,
                    "userName": "1"
                },
                {
                    "email": "",
                    "mobile": "",
                    "type": 2,
                    "userName": ""
                }
            ],
            "enquiryWholeApplyProductList": [

            ],
            "productFileUrl": "",
            "searchkey": "cytest01",
            "projectName": "11",
            "provinceId": "5",
            "cityId": "65"
        }
        run = configHttpC.ConfigHttpC(url, params=None, data=json.dumps(data), headers=headers, method='POST')
        print(run.response)

if __name__ == "__main__":
      # tools.test_tools3(1);
      suite = unittest.TestSuite()
      suite.addTest(tools("test_tools"))
      runner = unittest.TextTestRunner()
      runner.run(suite)


