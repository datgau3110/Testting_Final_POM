import sys
import time
sys.path.append("C:/Users/letie/PycharmProjects/PythonFinalTest1POM")

from pageObjects.HomePage import HomePage

class TestHome():
    def __init__(self, driver):
        self.driver = driver

    def test_home(self):
        home = HomePage(self.driver)
        home.click_home()
        time.sleep(1)