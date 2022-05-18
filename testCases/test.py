
import time
import unittest
import sys
import HtmlTestRunner
from selenium import webdriver
sys.path.append("C:/Users/letie/PycharmProjects/PythonFinalTest1POM")
from testCases.testLogin import TestLogin
from testCases.testReport import TestReport
from testCases.testFeedback import TestFeedback
from testCases.testNew import TestNew
from testCases.testHome import TestHome
from testCases.testExit import TestExit





class NroblueTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="C:\\Users\\letie\\PycharmProjects\\PythonFinalTest1POM\\drivers\\chromedriver.exe")
    baseURL = "https://nroblue.com/dang-nhap"
    
    driver.get(baseURL)
    driver.maximize_window()

    def test_all(self):
        login = TestLogin(self.driver)
        login.test_login()
        time.sleep(1)
        report = TestReport(self.driver)
        report.test_report()
        time.sleep(1)
        feedback = TestFeedback(self.driver)
        feedback.test_feedback()
        time.sleep(1)
        new = TestNew(self.driver)
        new.test_new()
        time.sleep(1)
        home = TestHome(self.driver)
        home.test_home()
        time.sleep(1)
        exit = TestExit(self.driver)
        exit.test_exit()
        time.sleep(1)
        
        self.driver.close()

   

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\letie\\PycharmProjects\\PythonFinalTest1POM\\reports'))
