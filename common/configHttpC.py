import requests


class ConfigHttpC:

    def __init__(self, url, params, data, headers, method):
        self.response = self.run_main(url, params, data, headers, method)

    def send_post(self, url, data, headers):
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=url, data=data, headers=headers,verify=False)
        return response.json()

    def send_get(self, url, params, headers):
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, params=params, headers=headers,verify=False)
        return response.json()

    def run_main(self, url, params, data, headers, method):
        respose = None
        if method == 'GET':
            respose = self.send_get(url, params, headers)
        else:
            respose = self.send_post(url, data, headers)
        return respose


if __name__ == '__main__':
    url = 'http://erp.fat.homedo.com/Test/Go?username=cuiyang2&password=cuiyang2'
    headers = {'Content-Type': 'application/json'}
    # data=[{"imageUrl":"https://project-homedo.oss-cn-shanghai.aliyuncs.com/3f75f6aa-69a1-4adf-be65-b86e96337aa4_M站.jpg","expressNumber":"6953787337958"},{"imageUrl":"https://project-homedo.oss-cn-shanghai.aliyuncs.com/3f75f6aa-69a1-4adf-be65-b86e96337aa4_上传业务免单活动.jpg","expressNumber":"6953787337958"}]
    # print(type(data))
    # run = ConfigHttpC(url,params=None,data=json.dumps(data),headers=headers,method='POST')
    run = ConfigHttpC(url,params=None,data=None,headers=headers,method='POST')
    print(run.response)


