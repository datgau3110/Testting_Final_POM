import sys
import time
sys.path.append("C:/Users/letie/PycharmProjects/PythonFinalTest1POM")

from pageObjects.FeedbackPage import FeedbackPage

class TestFeedback():
    def __init__(self, driver):
        self.driver = driver

    def test_feedback(self):
        feedback = FeedbackPage(self.driver)
        feedback.click_feedback()
        time.sleep(1)