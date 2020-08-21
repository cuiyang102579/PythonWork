import random
import readConfig
from common import configHttpC
import unittest
import json
from common.Log import Log
from common.StringUtils import get_now, db_to_json
from common.configDB import DataBase

localReadConfig = readConfig.ReadConfig()
url = localReadConfig.get_utms("utms_api")
log = Log()
# appName='应用名称'+get_now()

# con={"host":localReadConfig.get_db('host'),"user":localReadConfig.get_db('user'),"passwd":localReadConfig.get_db('passwd')}
print(localReadConfig.get_db('passwd'))
con={"host":localReadConfig.get_db('host'),"user":localReadConfig.get_db('user'),"passwd":'Y,l+7L0w'}


class application(unittest.TestCase):
    ''' UTMS 应用管理'''

    @classmethod
    def setUpClass(self):
        log.info("start.......")
        log.info(localReadConfig.get_db('passwd'))
        log.info('Y,l+7L0w')
        # 存储新增的应用id
        globals()["repoId"]='0'
        # 数据初始化，定义项目类型以及名称
        joinTypes=['THIRD_PARTY','R_D','COOPERATION']
        ids = [{'id': 1001, 'repo_name': '团队协调'}, {'id': 1002, 'repo_name': '移动办公'}, {'id': 1003, 'repo_name': '项目管理'}, {'id': 1004, 'repo_name': '客户关系'}, {'id': 1005, 'repo_name': '供应链管理'}, {'id': 1006, 'repo_name': '财务报销'}, {'id': 1007, 'repo_name': '法务工具'}]
        ds= random.choice(ids)
        self.repositoryId=ds['id']
        self.repo_name=ds['repo_name']
        log.info(self.repo_name)
        self.name=self.repo_name+get_now()
        self.joinType=random.choice(joinTypes)
        self.remark = "一句话简介" + get_now()

        # 连接数据库
        self.conn = DataBase(con, "saas_application")
        # print(self.repositoryId)
        # print(self.name)
    @classmethod
    def tearDownClass(self):
        log.info("end.....")
        self.conn.close()

    def test_1_application_simple(self):
        ''' 新增应用'''
        log.info("开始test_1_application_simple")
        urlnew = url + 'application/simple'
        log.info("请求地址"+urlnew)
        headers = {'Content-Type': 'application/json'}
        run = configHttpC.ConfigHttpC(urlnew, params=None, data=json.dumps(application.get_data(self)), headers=headers, method='POST')
        log.info(run.response)
        respCode=run.response['respCode']

        if respCode == '0000':
            sql = 'SELECT id from application  where app_name = ' + '\'' + self.name + '\';'
            res = self.conn.execute(sql)
            print(res)
            jsondata = db_to_json(res, 'id')
            globals()["repoId"] = jsondata[0]['id']

        self.assertEqual("0000",respCode)

    def test_2_application_simple_edit(self):
        ''' 编辑应用'''
        log.info("开始test_2_application_simple_edit")
        if  globals()["repoId"] == '0':
            self.assertFalse("未获取到repoId，无法进行编辑")
        urlnew = url + 'application/'+str(globals()["repoId"])+'/simple'
        log.info("请求地址" + urlnew)
        headers = {'Content-Type': 'application/json'}
        # datanew=self.data
        self.remark = "修改一句话简介" + get_now()
        run = configHttpC.ConfigHttpC(urlnew, params=None, data=json.dumps(application.get_data(self)), headers=headers, method='PATCH')
        log.info(run.response)
        respCode = run.response['respCode']
        self.assertEqual("0000", respCode)

    def test_3_application_extra(self):
        ''' 编辑介绍'''
        log.info("开始test_3_application_extra")
        if globals()["repoId"] == '0':
            self.assertFalse("未获取到repoId，无法进行编辑")
        urlnew = url + 'application/' + str(globals()["repoId"]) + '/extra'
        log.info("请求地址" + urlnew)
        headers = {'Content-Type': 'application/json'}
        data={"introduce":"河姆渡是一款专注于智能建筑采购的手机APP，产品涵盖弱电安防智能化行业源头好货。\n秒杀、团购、折扣等优惠活动一应俱全，让您采购成本直降10%~30%。\n更有方案馆、规划咨询、整单采购等立体式配套服务。\n\n【与头部品牌深度合作，打造智能建筑强力供应体系】\n河姆渡覆盖智能建筑行业：信息设施、公共安全、楼宇自控、智能照明、机房工程、音视频、智能家居、线缆管材、电脑/外设、辅材/工具等10大品类、15万款SKU，源头直采，品质保证。\n\n【完善的服务体系，保障产品安装及使用】\n河姆渡有超过300位线上客拓人员、2000位线下服务人员，7*12小时提供服务，触达商品全生命周期，让您放心采购、后顾无忧。\n\n【完善的物流体系，极速发货使命必达】\n河姆渡遍布全国的57个仓储中心，凡下单者，虽远必达。\n\n【特色技术服务，助您解决项目困扰】\n河姆渡设有方案馆、众包馆等技术服务，可以帮助用户提供工程服务能力，提供工程业务水平。\n\n【行业最新资讯，打造智能建筑行业的“头条”】\n专注智能的信息传播与搜集，在“智能”版块内，你可以看到国内一线的智能领域顶尖品牌资讯：新品发布、企业资讯以及对应的智能活动。","functionDesc":"河姆渡全新起航，只为最可爱的您。\n1、找人手版块——需求极速对接。\n2、找活干--项目信息对接\n2、资讯实时更新——打造智能建筑行业的“头条”。\n3、在线课程限时免费——行业牛人，实战解析行业信息。\n4、优化部分问题，体验更顺畅。\n河姆渡祝您2020年全家安康！\n河姆渡，工业互联，数字产业。\n智能建筑采购神器 - 更多选择 更多优惠 尽在河姆渡","priceDesc":"免费","coverImage":"https://wuyou-resource.oss-cn-shanghai.aliyuncs.com/Solution/542d4a81-dc86-4344-a2b2-6720853ed58e_河姆渡.jpg","contentImages":["https://wuyou-resource.oss-cn-shanghai.aliyuncs.com/Solution/7028973e-e2b4-4a3e-b47b-aa4c9d5b1038_4.jpg","https://wuyou-resource.oss-cn-shanghai.aliyuncs.com/Solution/a758bb56-6dee-4123-82c3-79b08da1c6b1_3.jpg","https://wuyou-resource.oss-cn-shanghai.aliyuncs.com/Solution/bcf7b5e5-a98b-414b-b662-9faf9a18e547_2.jpg","https://wuyou-resource.oss-cn-shanghai.aliyuncs.com/Solution/918e52e5-c6a1-4ae6-92a6-c81c7e311287_河姆渡.jpg","https://wuyou-resource.oss-cn-shanghai.aliyuncs.com/Solution/ec660dbb-42af-4e7a-8142-87cc09b582bc_4.jpg"]}
        run = configHttpC.ConfigHttpC(urlnew, params=None, data=json.dumps(data), headers=headers, method='PUT')
        log.info(run.response)
        respCode = run.response['respCode']
        self.assertEqual("0000", respCode)

    def test_4_application_group(self):
        ''' 应用列表查询'''
        log.info("开始test_4_application_group")
        if globals()["repoId"] == '0':
            self.assertFalse("未获取到repoId，无法进行编辑")
        urlnew = url + 'application/group?groupType=REPOSITORY'
        log.info("请求地址" + urlnew)
        headers = {'Content-Type': 'application/json'}
        run = configHttpC.ConfigHttpC(urlnew, params=None, data=None, headers=headers, method='GET')
        # log.info(run.response)
        data=run.response['data']['records']
        print("&&&&&&&&&&&&&&&&&&&&&&")
        log.info(self.repo_name )
        log.info(globals()["repoId"])
        print("&&&&&&&&&&&&&&&&&&&&&&")
        print(data)
        blean = False
        for x in range(0,len(data)):
            if data[x]['groupName'] ==self.repo_name :
                c=data[x]['applicationSimpleList']
                applicationSimpleList=data[x]['applicationSimpleList']
                for y in range(0,len(applicationSimpleList)):
                    a= applicationSimpleList[y]['applicationId']
                    b=globals()["repoId"]
                    if applicationSimpleList[y]['applicationId'] == str(globals()["repoId"]):
                        log.info("查询结果正确 "+str(globals()["repoId"]))
                        blean=True
                        break
        if blean :
            self.assertTrue("查询结果正确")
        else :
            self.assertFalse("未查询到本次新增的数据")



    def get_data(self):
        data = {
            "appName": self.name,
            "appAliasName": "简称",
            "enable": True,
            "repositoryId": self.repositoryId,
            # "repositoryId":"1003",
            "joinType": self.joinType,
            "billingPlans": [
                "ACCOUNT_ONLINE_NUMBER",
                "ACCOUNT_CONCURRENT_NUMBER",
                "REQUEST_NUMBER"],
            "supportDevices": [
                "APP",
                "WEB",
                "WX_MINIAPP",
                "H5"],
            "routePath": "http://www.baidu.com",
            "routeParam": "/",
            "sort": 0,
            "appIcon": "https://wuyou-resource.oss-cn-shanghai.aliyuncs.com/Solution/ace61e01-de05-4478-8b00-a3cafa6cba2c_200-200.png",
            "remark": self.remark,
            # "remark": globals()["remark"],
            "providerName": "上海河服务商有限公司",
            "providerBrandName": "品牌名称",
            "providerKefu": "400-807-7117"}
        return data



if __name__=="__main__":
    unittest.main();
