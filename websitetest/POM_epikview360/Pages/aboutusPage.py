
class AboutusPage():

    def __init__(self, driver):                        # constructor
        self.driver = driver
        self.book_button_css = "a.tm-button.style-flat.tm-button-custom.tm-button-custom"
        self.breadcrumb_link_xpath = '// *[ @ id = "page-breadcrumb"] / div / ul / li[1] / a'

# creation of objects

    def click_book_button(self):
        self.driver.find_element_by_css_selector(self.book_button_css).click()

    def click_home_breadcrumb(self):
        self.driver.find_element_by_xpath(self.breadcrumb_link_xpath).click()
