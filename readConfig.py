import os
import codecs
import configparser

work_dirc = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(work_dirc, "properties/config.ini")

print(configPath)

class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()
        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_tools(self, name):
        value = self.cf.get("TOOLS", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

if __name__ == '__main__':
    url = ReadConfig().get_tools("logisticsUpload")
    print(url)