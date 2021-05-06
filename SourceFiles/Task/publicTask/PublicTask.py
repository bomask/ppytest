
from selenium import webdriver
import sys
sys.path.append('F:\\ppytestNew\\SourceFiles')
from Object import PublicObject

class PublicTask:
    def __init__(self):
        self.public_o = PublicObject.PublicObject()

    def sendKeys(self, type, element_path, key_words):
        if type.upper() == "name":
            self.public_o.findEleByName(element_path).send_keys(key_words)
        elif type.upper() == "id":
            self.public_o.findEleByID(element_path).send_keys(key_words)
        elif type.upper() == "class":
            self.public_o.findEleByClass(element_path).send_keys(key_words)
        elif type.upper() == "xpath":
            self.public_o.findEleByXpath(element_path).send_keys(key_words)
        else:
            print("sorry")

    def click(self, type, element_path):
        if type.upper() == "name":
            self.public_o.findEleByName(element_path).click()
        elif type.upper() == "id":
            self.public_o.findEleByID(element_path).click()
        elif type.upper() == "class":
            self.public_o.findEleByClass(element_path).click()
        elif type.upper() == "xpath":
            self.public_o.findEleByXpath(element_path).click()
        else:
            print("sorry")

    def openBrowser(self, url=None):
        self.public_o.driver.get(url)



