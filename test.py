import os
import time,sys
from common.configEmail import Email
from packages.HTMLTestReportCN import HTMLTestRunner
import unittest


# 指定测试用例为当前文件夹下的 testcase 目录
test_dir = './testcase'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*load*.py')


if __name__ == "__main__":


    # 执行测试用例
    now = time.strftime("%Y%m%d%H%M%S")
    filename = './report/' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Interface Test Report',
                            description='')
    runner.run(discover)
    fp.close()

    # 发送邮件
    curent_dirc = os.path.dirname(os.path.realpath(__file__))
    report_dirc = os.path.join(curent_dirc, "Report")
    Email.send_mail(report_dirc)
