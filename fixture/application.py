from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Application(WebDriver):

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get("https://account.usafootball.com/login/")


    def destroy(self):
        self.wd.quit()
