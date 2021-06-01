from selenium.webdriver.common.by import By


from zidong.base.base_page import BasePage


class LoginPage(BasePage):
    
    user = (By.NAME,'accounts')
    pwd = (By.NAME,'pwd')
    button =(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')


    url = "http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html"

    def login(self):
        self.open()
        self.input(self.user,txt)
        self.input(self.pwd,pwd_)
        self.click(self.button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    user ='wushisi'
    pwd = '123456789'
    lp = LoginPage(driver)
    lp.login(user,pwd)
