
import sys
import time

sys.path.append("C:/Users/letie/PycharmProjects/PythonFinalTest1POM")

from pageObjects.NewPage import NewPage

class TestNew():
    title = 'game hay lắm'
    content = 'Game hay lắm, giải trí rất tốt'

    def __init__(self, driver):
        self.driver = driver

    def test_new(self):
        new = NewPage(self.driver)
        new.set_title(self.title)
        time.sleep(2)
        new.set_content(self.content)
        time.sleep(2)
        new.click_submit()
        time.sleep(2)
        

    