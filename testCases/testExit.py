import sys
import time
sys.path.append("C:/Users/letie/PycharmProjects/PythonFinalTest1POM")

from pageObjects.ExitPage import ExitPage

class TestExit():
    def __init__(self, driver):
        self.driver = driver

    def test_exit(self):
        exit = ExitPage(self.driver)
        exit.click_exit()
        time.sleep(1)