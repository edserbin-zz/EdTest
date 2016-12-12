from ..pages.base_page import BasePage


class GoodsPage(BasePage):

    def __init__(self, driver, goods='p45257130-velo-pokryshka-kenda.html'):
        super(GoodsPage, self).__init__(driver)
        self.url += '/%s.html ' % goods

    def select_goods(self):
        self.click_on_the_object('//div[@class="b-favorites-icon"]//span/span/span')

    def scrool_bootom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
