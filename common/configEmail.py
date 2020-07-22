from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os
import  time

curent_dirc = os.path.dirname(os.path.realpath(__file__))
print("#######")
print(curent_dirc)
report_dirc = os.path.join(curent_dirc, "report")
class Email:
    def find_new_report(report_dirc):
        lists = os.listdir(report_dirc)
        lists.sort(key=lambda fn: os.path.getmtime(report_dirc + "\\" + fn))
        new_report = os.path.join(report_dirc, lists[-1])
        # print(new_report)
        return new_report

    def find_new_reportNew(report_dirc):
        lists = os.listdir(report_dirc)
        lists.sort(key=lambda fn: os.path.getmtime(report_dirc + "\\" + fn))
        new_report = os.path.join(report_dirc, lists[-1])
        print(new_report)
        file = open(new_report, "r", encoding='utf-8')
        text = file.read()
        content = Email.get_str_btw(text, '<div class=\'heading\'>', '<table id=\'result_table')
        return content

    def find_new_reportNew2(report_dirc):
        file = open(report_dirc, "r", encoding='utf-8')
        text = file.read()
        content = Email.get_str_btw(text, '<div class=\'heading\'>', '<table id=\'result_table')
        return content

    def send_mail(report_dirc):
        # new_report = Email.find_new_reportNew(report_dirc)
        new_report = Email.find_new_reportNew2(report_dirc)
        # 读取报告
        # f = open(new_report, 'rb')
        # mail_body = f.read()
        # f.close()
        # 定义邮件正文，报告以正文的形式发送
        msg = MIMEText(new_report, 'html', 'utf-8')

        # 定义邮件标题
        msg['Subject'] = Header("接口自动化测试报告"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "utf-8")
        msg['From'] = Header("崔杨", 'utf-8')

        # 163邮箱
        # mail_server = 'smtp.163.com'
        # user_name = 'cuiyang102579@163.com'
        # pwd = 'YMIRUQKQUVHCVDOB'
        # sender = 'cuiyang102579@163.com'
        # receivers = ['cuiyang102579@163.com']

        # homedo邮箱
        mail_server = 'smtp.homedo.com'
        user_name = 'cuiyang@homedo.com'
        pwd = 'Cy102579'
        sender = 'cuiyang@homedo.com'
        receivers = ['cuiyang@homedo.com','cuiyang102579@163.com']

        # smtp = smtplib.SMTP(mail_server,465)
        smtp = smtplib.SMTP_SSL(mail_server, 465)
        smtp.login(user_name, pwd)
        smtp.sendmail(sender, receivers, msg.as_string())
        smtp.quit()
        print("emial has send out")
    # 读取两个字符串中间的内容
    def get_str_btw(s, f, b):
        par = s.partition(f)
        return (par[2].partition(b))[0][:]

if __name__ == "__main__":
    curent_dirc = os.path.dirname(os.path.realpath(__file__))
    report_dirc = os.path.join(curent_dirc, "report")

    get_path = os.path.dirname(os.path.abspath(__file__))
    print(get_path)
    log_path = os.path.join(os.path.dirname(get_path), "report")
    get_path = os.path.dirname(get_path)

    print(get_path)
    Email.send_mail(log_path)

    # file = open('D:\\workspace\\pythonWork\\Report\\2020-07-13 16_42_06_result.html', "r",encoding='utf-8')
    # text = file.read()
    # content = Email.get_str_btw(text, '<div class=\'heading\'>', '<table id=\'result_table')
    # print(content)
    # now = time.strftime("%Y%m%d%H%M%S")
    # print(now)
