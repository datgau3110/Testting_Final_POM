class ReportPage():
    report_button_xpath = '//*[@id="pageHeader"]/div/div[3]/a'

    def __init__(self, driver):
        self.driver = driver

    def click_report(self):
        self.driver.find_element_by_xpath(self.report_button_xpath).click()