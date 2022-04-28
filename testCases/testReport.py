
import sys
import time
sys.path.append("C:/Users/letie/PycharmProjects/PythonFinalTest1POM")

from pageObjects.ReportPage import ReportPage

class TestReport():
    def __init__(self, driver):
        self.driver = driver

    def test_report(self):
        report = ReportPage(self.driver)
        report.click_report()
        time.sleep(1)
        
    

    