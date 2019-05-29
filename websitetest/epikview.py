from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import HtmlTestRunner
import unittest
# import urllib3
# import re


class EpikView(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome\
            (r"C:/Users/Arpita Sharma/PycharmProjects/Epikso_Gov/browserdrivers/chromedriver.exe")
        cls.driver.set_page_load_timeout(30)
        cls.driver.get("https://epiksolution.org/epikviewdemo/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_logo(self):
        logo = self.driver.find_element_by_xpath('//*[@id="page-header-inner"]/div/div/div/div/div[1]/div/a/img[1]')
        self.driver.implicitly_wait(10)
        print(logo.is_displayed())                                         # verify if logo is displayed or not
        logo.click()
        print("Title of Home Page is : " + self.driver.title)              # returns title of homepage
        homePage_url = self.driver.current_url
        print("Home Page URL is : " + homePage_url)                        # returns URL of home page


    def test_header_homepage(self):
        headerLink_home = self.driver.find_element_by_xpath('//*[@id="menu-item-421"]/a/div/span')
        self.driver.implicitly_wait(10)
        headerLink_home.click()
        homePage_url = self.driver.current_url
        print("Home Page URL is : " + homePage_url)                        # returns URL of home page

    #driver.implicitly_wait(15)

    def test_header_about(self):
        headerLink_aboutUs = self.driver.find_element_by_xpath('//*[@id="menu-item-396"]/a')
        self.driver.implicitly_wait(10)
        headerLink_aboutUs.click()
        about_url = self.driver.current_url
        print("About Us Page URL is : " + about_url)  # returns URL of about us page
        print("Title of About Us Page is : " + self.driver.title)  # returns title of about us page
        # driver.implicitly_wait(15)

    def test_header_contact(self):
        headerLink_contact = self.driver.find_element_by_xpath('//*[@id="menu-item-420"]/a/div/span')
        self.driver.implicitly_wait(10)
        headerLink_contact.click()
        contact_url = self.driver.current_url
        print("Contact Us Page URL is : " + contact_url)  # returns URL of contact page
        print("Title of contact us Page is : " + self.driver.title)  # returns title of contact page


    def test_contactpage_form(self):
            self.driver.get("https://epiksolution.org/epikviewdemo/contact-us/")
            self.driver.find_element_by_name('your-name').send_keys("Arpita")
            self.driver.find_element_by_name('your-email').send_keys("arpita@mailinator.com")
            self.driver.find_element_by_name('your-tel').send_keys("9898989898")
            self.driver.find_element_by_name('your-message').send_keys('Welcome to Epik view 360 message')
            self.driver.find_element_by_xpath('//*[@id="wpcf7-f7-p417-o1"]/form/p[5]/input').click()
            address_text = self.driver.find_element_by_class_name('content')
            print(address_text.text)


    def test_bookappoint_btn(self):
        btn_Bookappoint = self.driver.find_element_by_xpath('//*[@id="header-right-inner"]/div/a[1]')
        self.driver.implicitly_wait(10)
        btn_Bookappoint.click()
        bookAppoint_url = self.driver.current_url
        print("Book An Appointment Page URL is : " + bookAppoint_url)  # returns URL of Book an appointment page
        print("Title of Home Page is : " + self.driver.title)  # returns title of Book an Appointment page

    def test_footer_aboutview360(self):
        self.driver.get("https://epiksolution.org/epikviewdemo/")
        ids = self.driver.find_elements_by_xpath('//*[@href]')
        self.driver.implicitly_wait(10)
        for i in ids:
            print(i.get_attribute('href'))

        # print("About View 360 page URL is : " + footer_aboutview_url)
        # print("Title of About view Page is : " + self.driver.title)
        # i.find_element_by_css_selector(".link[href='https://epikview360.com/about-us/']").click()
        # i.find_element_by_css_selector('a[innertext=["About View 360"]').click()

    def test_footer_logo(self):
        self.driver.get("https://epiksolution.org/epikviewdemo/")
        footer_logo = self.driver.find_element_by_xpath("//img[contains(@alt,'logo (1)')]")
        self.driver.implicitly_wait(10)
        footer_logo.click()

    def test_textbody(self):
        self.driver.get("https://epiksolution.org/epikviewdemo/")
        text_body = self.driver.find_element_by_css_selector('body')
        self.driver.implicitly_wait(10)
        time.sleep(10)
        text_body.send_keys(Keys.CONTROL+'a')

    def test_homepage_scroll(self):
        self.driver.get("https://epiksolution.org/epikviewdemo/")
        # element1 = self.driver.find_elements_by_xpath("// *[ @ id = 'tm-row-5ccaa4a896467']")
        element1 = self.driver.find_element_by_class_name("page-footer-inner")
        self.driver.implicitly_wait(30)
        element1.location_once_scrolled_into_view

    def test_footer_aboutlink(self):
        element2 = self.driver.find_element_by_css_selector("a.link")
        element2.click()
        abouturl = self.driver.current_url
        print(abouturl)

    def test_footer_contactlink(self):
        element3 = self.driver.find_element_by_partial_link_text("Contact Us")
        element3.click()
        contacturl = self.driver.current_url
        print(contacturl)

    def test_footer_bookappointment(self):
        element3 = self.driver.find_element_by_partial_link_text("Book An Appointment")
        element3.click()
        bookurl = self.driver.current_url
        print(bookurl)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("PGE_Tests Completed")

    if __name__ == '__main__':
        unittest.main(
            testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Arpita Sharma/PycharmProjects/Epikso_Gov/Reports')
                     )

