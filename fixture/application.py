from selenium.webdriver.firefox.webdriver import WebDriver
wd = WebDriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = Webdriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def test_open_homepage(self):
        wd = self.wd
        wd.get("https://account.usafootball.com/login/")


    def destroy(self):
        self.wd.quit()
