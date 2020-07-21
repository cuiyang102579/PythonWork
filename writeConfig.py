import configparser

#  实例化configParser对象
import os

config = configparser.ConfigParser()
# -read读取ini文件
work_dirc = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(work_dirc, "properties\config.ini")

config.read(configPath, encoding='utf-8')
list = []
list = config.sections()  # 获取到配置文件中所有分组名称
print(list)

# config.set('OMS', 'fatoms', 'fatoms002')  # 给type分组设置值
# config.remove_option('OMS', 'uatoms')  # 删除type分组的stuno

# o = open(configPath, 'w')
# config.write(o)
# o.close()  # 不要忘记关闭

class WriteConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()

    # 新增或更新配置文件
    def setConfig(self,sections,typename,val):
        if sections not in list:  # 如果分组type不存在则插入type分组
            config.add_section(sections)
            config.set(sections, typename, val)  # 给type分组设置值
        config.set(sections, typename, val)  # 给type分组设置值
        o = open(configPath, 'w')
        config.write(o)
        o.close()  # 不要忘记关闭

    # 删除某一参数
    def removeConfig(self,sections,typename):
        self.cf.remove_option(sections, typename)  # 删除type分组的stuno
        o = open(configPath, 'w')
        self.cf.write(o)
        o.close()  # 不要忘记关闭

    # 删除某一分组
    def removeConfigType(self, sections):
        config.remove_section(sections)
        o = open(configPath, 'w')
        config.write(o)
        o.close()  # 不要忘记关闭


if __name__ == '__main__':
    print("11111")
    w = WriteConfig()
    # w.setConfig("OMS",'fatoms','fatoms6')
    w.setConfig("OMS",'fatoms','fatoms6')
    # WriteConfig.removeConfig('OMS','uatoms7')
    # w= WriteConfig()
    # w.removeConfigType('HOMEDO1')

