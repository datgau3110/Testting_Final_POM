
import sys
import time
sys.path.append("C:/Users/letie/PycharmProjects/PythonFinalTest1POM")

from pageObjects.LoginPage import LoginPage

class TestLogin():
    email = 'danhdatgiaodo'
    password = 'danhdat12345'

    def __init__(self, driver):
        self.driver = driver

    def test_login(self):
        login = LoginPage(self.driver)
        login.set_email(self.email)
        time.sleep(2)
        login.set_password(self.password)
        time.sleep(2)
        login.click_login()
        time.sleep(2)
        

    