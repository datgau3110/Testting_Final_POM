class ExitPage():
    exit_button_xpath = '/html/body/div[2]/div/div/a[3]'

    def __init__(self, driver):
        self.driver = driver

    def click_exit(self):
        self.driver.find_element_by_xpath(self.exit_button_xpath).click()