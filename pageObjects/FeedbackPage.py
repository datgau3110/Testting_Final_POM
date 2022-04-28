class FeedbackPage():
    feedback_button_xpath = '/html/body/div[5]/div[2]/div[1]/a'

    def __init__(self, driver):
        self.driver = driver

    def click_feedback(self):
        self.driver.find_element_by_xpath(self.feedback_button_xpath).click()