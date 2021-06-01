from selenium import webdriver


class BasePage:
    def __init__(self):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def locator(self,loc):
        return self.driver.find_element(*loc)

    def input(self,loc,txt):
        self.locator(loc).send_keys(txt)

    def click(self,loc):
        self.locator(loc).click()
        