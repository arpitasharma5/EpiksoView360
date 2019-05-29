from websitetest.POM_epikview360.Locators.locators import Locators


class HomePage():

    def __init__(self, driver):
        self.driver = driver
        str1 = '//*[@id="page-header-inner"]/div/div/div/div/div[1]/div/a/img[1]'
        self.headerlogo_image_xpath = str1
        # self.headerlogo_image_xpath = '//*[@id="page-header-inner"]/div/div/div/div/div[1]/div/a/img[1]'
        # self.headerlogo_image_xpath = '//*[@id="page-header-inner"]/div/div/div/div/div[1]/div/a/img[1]'
        # self.headerlogo_image_xpath = "xpath=(.//*[normalize-space(text()) and normalize-space(.)='Home'])[1]/preceding::img[1]"
        str2 = '// *[ @ id = "menu-item-421"] / a / div / span'
        self.header_LinkHome_xpath = str2
        # self.header_LinkHome_xpath = '//*[@id="menu-item-421"]/a/div/span'
        # # self.header_LinkAbout_xpath = '//*[@id="menu-item-396"]/a/div/span'
        # self.header_LinkAbout_xpath ="(.//*[normalize-space(text()) and normalize-space(.)='Home'])[1]/following::span[1]"
        # self.header_LinkContact_xpath = '//*[@id="menu-item-420"]/a/div/span'
        # self.bookaptbutton_btn_xpath = '//*[@id="header-right-inner"]/div/a[1]'
        # self.footer_logo_xpath = "//img[contains(@alt,'logo (1)')]"
        # # self.page_scroll_classname = "page-footer-inner"
        self.footer_aboutlink_cssselector = "a.link"
        self.footer_contactlink_linktext = "Contact Us"
        self.footer_bookappointment_partiallinktext = "Book An Appointment"

    def click_headerlogo(self):
        self.driver.find_element_by_xpath(self.headerlogo_image_xpath).click()

    def click_homeheaderlink(self):
        self.driver.find_element_by_xpath(self.header_LinkHome_xpath).click()

    def click_aboutheaderlink(self):
        self.driver.find_element_by_xpath(self.header_LinkAbout_xpath).click()

    def click_contactheaderlink(self):
        self.driver.find_element_by_xpath(self.header_LinkContact_xpath).click()

    def click_bookappointment_btn(self):
        self.driver.find_element_by_xpath(self.bookaptbutton_btn_xpath).click()

    def click_footerlogo(self):
        self.driver.execute_script("window.scrollTo(0,7000)")
        self.driver.find_element_by_xpath(self.footer_logo_xpath).click()

    def click_footeraboutlink(self):
        self.driver.find_element_by_css_selector(self.footer_aboutlink_cssselector).click()

    def click_footercontactlink(self):
        self.driver.find_element_by_partial_link_text(self.footer_contactlink_linktext).click()

    def click_footerbookappointment(self):
        self.driver.find_element_by_partial_link_text(self.footer_bookappointment_partiallinktext).click()
