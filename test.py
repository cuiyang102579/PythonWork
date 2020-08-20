import os
import time

from common.Log import Log
from common.StringUtils import del_file
from common.configEmail import Email
from packages.HTMLTestReportCN import HTMLTestRunner
import unittest

log = Log()
curent_dirc = os.path.dirname(os.path.realpath(__file__))
report_dirc = os.path.join(curent_dirc, "report")
print("#######"+report_dirc)

# 指定测试用例为当前文件夹下的 testcase 目录
# test_dir = './testcase'
test_dir =os.path.join(curent_dirc, "testcase")

# discover = unittest.defaultTestLoader.discover(test_dir, pattern='*load*.py')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*Test*.py')


if __name__ == "__main__":
    del_file(report_dirc)
    # 执行测试用例
    now = time.strftime("%Y%m%d%H%M%S")
    # filename = report_dirc + now + '.html'
    filename = report_dirc  + '/index.html'
    log.info(filename)
    print('*********'+filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Interface Test Report',
                            description='')
    runner.run(discover)
    fp.close()

    # 发送邮件
    # curent_dirc = os.path.dirname(os.path.realpath(__file__))
    # report_dirc = os.path.join(curent_dirc, "Report")
    Email.send_mail(filename)
    # Email.send_mail(report_dirc)

