class NewPage ():
    title_xpath = '//*[@id="title"]'
    content_xpath = '//*[@id="content"]'
    submit_button_xpath = '//*[@id="form"]/button'

    def __init__(self, driver):
        self.driver = driver

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.title_xpath).send_keys(title)

    def set_content(self, content):
        self.driver.find_element_by_xpath(self.content_xpath).send_keys(content)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()