from selenium import webdriver


class PublicObject:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def findEleByClass(self, element_path):
        return self.driver.find_element_by_class_name(element_path)

    def findEleByID(self, element_path):
        return self.driver.find_element_by_id(element_path)

    def findEleByName(self, element_path):
        return self.driver.find_element_by_name(element_path)

    def findEleByTag(self, element_path):
        return self.driver.find_element_by_tag_name(element_path)

    def findEleByXpath(self, element_path):
        return self.driver.find_element_by_xpath(element_path)
