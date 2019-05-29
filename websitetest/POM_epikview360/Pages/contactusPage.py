from websitetest.POM_epikview360.Locators.locators import Locators


class ContactUsPage():

    def __init__(self, driver):
        self.driver = driver
        self.name_textbox_name = "your-name"
        self.email_textbox_name = "your-email"
        self.phone_textbox_name = "your-tel"
        self.message_textarea_name = "your-message"
        self.button_btn_xpath = '//*[@id="wpcf7-f7-p417-o1"]/form/p[5]/input'
        self.breadcrumb_link_xpath = '// *[ @ id = "page-breadcrumb"] / div / ul / li[1] / a'
        self.link_phone = "//a[contains(text(),'+1-925-444-0466')]"
        self.link_email = "a[contains(text(), 'contact@epikso.com')]"

    def enter_name(self, yourname):
        self.driver.find_element_by_name(self.name_textbox_name).click()
        self.driver.find_element_by_name(self.name_textbox_name).clear()
        self.driver.find_element_by_name(self.name_textbox_name).send_keys(yourname)

    def enter_email(self, email):
        self.driver.find_element_by_name(self.email_textbox_name).clear()
        self.driver.find_element_by_name(self.email_textbox_name).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element_by_name(self.phone_textbox_name).clear()
        self.driver.find_element_by_name(self.phone_textbox_name).send_keys(phone)

    def enter_message(self, message):
        self.driver.find_element_by_name(self.message_textarea_name).clear()
        self.driver.find_element_by_name(self.message_textarea_name).send_keys(message)

    def click_send(self):
        self.driver.find_element_by_xpath(self.button_btn_xpath).click()

    def click_home_breadcrumb(self):
        self.driver.find_element_by_xpath(self.breadcrumb_link_xpath).click()

    def click_phone_link(self):
        self.driver.find_element_by_xpath(self.link_phone).click()

    def click_email_link(self):
        self.driver.find_element_by_xpath(self.link_email).click()

