#coding=utf-8
import readConfig as readConfig
from common import configHttpC
import json
localReadConfig = readConfig.ReadConfig()
url = localReadConfig.get_tools("logisticsUpload")
print(url)


def myfile():
    for i in range(500):
     headers = {'Content-Type': 'application/json'}
     data = [{
       "imageUrl": "https://project-homedo.oss-cn-shanghai.aliyuncs.com/3f75f6aa-69a1-4adf-be65-b86e96337aa4_上传业务免单活动.jpg",
        "expressNumber": i}]
     run = configHttpC.ConfigHttpC(url, params=None, data=json.dumps(data), headers=headers, method='POST')
     print(run.response)



def my(a):
    url='https://sin66-api.fat.homedo.com/mng/resource/add'
    headers = {'Content-Type': 'application/json','auth-code': 'homedo-api-access','ticket':'8d79f50d-86a9-4e13-b85b-033d1d182d34'}
    data={
    "resourceTitle":"一建资料"+a,
    "firstCategory":"一建资料",
    "introduction":"近年来，随着城市规模和城市化水近年来，随着城市规模和城市化水近年来，随着城市规模和城市化水",
    "mainPicUrl":"https://project-homedo.oss-cn-shanghai.aliyuncs.com/fc077b9c-177a-4c04-a2fe-aa6cc5caea76_12306.jpg",
    "resourceAttachmentUrl":"https://project-homedo.oss-cn-shanghai.aliyuncs.com/73abcb45-172d-4dcb-a3e3-a70b870b31cd_商品清单.rar",
    "sort":1,
    "tag":"甲乙丙丁;甲;乙;丙;丁",
    "resourceBody":"<p class=\"ql-align-center\"><strong>安防PPP模式对智慧城市建设影响和作用</strong></p><p>自1996年公安部提出“科技强警”到现在，国内平安城市建设之路已走过20年有余。“科技强警”战略实施以及“3111”试点工程、雪亮工程战略，将中国城市视频监控建设的热潮迅速由试点区域延伸至全国，由公安主导延伸到各部委、各行业主管部门都积极重视。目前，我国城市视频监控建设仍处于全面建设阶段，各省市先后推出众多针对平安城市、雪亮工程等的安防建设项目，大大拉动了安防产业的发展。根据前瞻产业研究院数据，2016年安防行业总产值已达到5,400亿元，同比增长11%，预计2017年市场规模达5,958亿元。按照《中国安防行业“十三五”(2016-2020年)发展规划》，“十三五”期间，中国安防行业将向规模化、联网化、自动化、智能化转型升级，预计到2020年，安防行业总产值将达到8,000亿元，年增长率超过10%。单是视频监控每年的市场规模也不容小窥，如下图，2017年视频监控整体的市场规模1,907亿元，预计2018年将达到2,145亿元。安防项目建设作为智慧城市建设的重要组成部分，将为智慧城市发展打下坚实的基础，而智慧城市的兴起对安防行业也将起到助推作用。</p><p class=\"ql-align-center\"><br></p><p>随着智慧城市、平安城市的深入推进，安防领域、尤其是安防设备及工程方面，将会保持持续增长的发展态势，安防项目呈现单体项目规模大、PPP模式为主流、运营周期长、技术应用难度高、区域保护明显、项目实施成本增加等特点。近几年由于国家对城镇化、反恐维稳、社会治理等的推动，无论是智慧城市还是平安城市的资源投入都很大。从国家财政收入和支出指标来看，我国历年财政支出均超财政收入，且缺口历年增大。2015年我国全年财政收入15.2万亿，财政支出17.6万亿，财政缺口达到2.4万亿；2016年我国全年财政收入15.9万亿，财政支出18.8万亿，财政缺口达到2.9万亿，为历年最高。而从地方政府的财政情况看，目前我国地方政府债务累计规模也在不断增加。</p><p><br></p><p>在这样的环境下，PPP这种新的业务模式开始越来越受到大家的重视，安防项目建设和融资模式也有了新的选择。从我们监测的数量来看(如下图)，2017年监测到的PPP项目有63个，占总项目数量的3%；市场规模约400亿元，占总市场规模的40%，由此可见PPP项目的单体项目规模巨大，平均规模近6亿元。安防项目投入如此之巨大，单个项目投资动辄数亿元、甚至十数亿元，如果只是采用财政支出的方式支持建设，将为地方政府带来巨大的财政压力。虽然原来的BT、BOT等建设模式可以有效缓解政府财政支出，但在一定程度上还是不能解决财政压力，特别是一些经济欠发达地区和偏远地区，建成后的分期付款依然使其背上债务。而智慧城市是比平安城市所涉范围更广、应用更复杂、资金需求更大，住建部在发起智慧城市试点</p><p class=\"ql-align-center\"><br></p>"
    }
    run = configHttpC.ConfigHttpC(url, params=None, data=json.dumps(data), headers=headers, method='POST')
    print(run.response)

def aaa():
        url = 'http://oms.fat.homedo.com/oms-totalinquiry-web/valetApplication/saveEnquiryWhole'
        # headers = {'Content-Type': 'application/json','Cookie':'gr_user_id=428a340c-bc78-425b-920d-180f6574e91c; grwng_uid=ad8b19a2-5ac8-4bad-9fd6-1224bbd05bd1; HMD_R=159400604323452375; Hm_lvt_51d4bdf6fae0f9d4bb58c528601ab693=1594006362; UM_distinctid=17322c91198514-08df1b22bac11b-4353760-1fa400-17322c911998da; NTKF_T2D_CLIENTID=guestCC1E2284-4588-9994-63C8-235995AA626B; a8c7c3f6977ae463_gr_last_sent_cs1=402300; _ga=GA1.2.1471859676.1594036306; LoginErrorCount=0; IsRemember=null; AccountId=405785; a016ee4c2a76b6bb_gr_last_sent_cs1=405785; utime=7776000; Hm_lvt_d1d21a226b3b6cbb96842713353fc9f7=1594006226,1594621667; COOKIE_USERfat.=54e26dfa-84e6-473f-8d00-d9381c8d37a9; COOKIE_USERdev.=93356d4b-0517-44f6-8530-fdc8f3a87537; _gid=GA1.2.470483385.1594690741; nTalk_CACHE_DATA={uid:hd_1000_ISME9754_guestCC1E2284-4588-99,tid:1594703558143673}; COOKIE_USERINFOfat.=%7B%22userId%22%3A%225705283077884826862%22%2C%22userName%22%3A%22%u5D14%u6768%22%2C%22depId%22%3A%22343ab9dc-79ab-4f5a-9601-05a0a69a6e1d%22%2C%22depName%22%3A%22%u6D4B%u8BD5%22%2C%22respCode%22%3A%220000%22%7D; COOKIE_USERINFOfat..sig=MlejMSWD_7WscYeiggUhHXfAzhGv8wQ9jkphLnie79M; EGG_SESS=PwJ-wpaGjYe-xzoIijB0MiKRxFycBv7FPiak4nRLzZo424NdDCTfEOX1MZMC6sdXHaC3ByXLDLa8j_-Dwap_uxV7zgJImdeDnxYkXnnPK8_UCQhT7yo8QJ3uV6EO0WgzdDgGUuBS45rGTzLoImGhiKyk7AIj_qrwptF0rYzIl8LhtQohvgiKkyTXjnr5sp-IoQborduBXH4SViuxnmWINyjQgACAQSQ3bti283WDVTWMabM6SLnRKsVNr1K_Lu87y1GtlnYPNpMp1PP-A3nOec7gQfZLpkOSaSksh6OYTPPgR2D5AfOaMDotNp8IrOwY_I_tZZe2cwAPeV9fG85SldU5Xd6uH-b4Eol8Sv11ciU='}
        headers = {'Content-Type': 'application/json','Cookie':'COOKIE_USERfat.=8d79f50d-86a9-4e13-b85b-033d1d182d34'}
        data={
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
    print('#####')
    for i in range(50,52):
      my(str(i));

    # test_tools4()