from ..pages.base_page import BasePage


class ListPage(BasePage):

    goods_container = '//div[@class="b-product-line js-list-container"]'

    def __init__(self, driver, goods='Velosipednye-shiny'):
        super(ListPage, self).__init__(driver)
        self.url += '/%s?output=list' % goods

    def select_goods(self, count):
        """select or deselect the goods """
        for i in range(1, count+1):
            self.hover_element('%s/div[%s]' % (self.goods_container, str(i)))
            self.click_on_the_object('%s/div[%s]//span/span/span'
                                     % (self.goods_container, str(i)))

    def go_to_goods(self, number=1):
        """select first or other good from list"""
        self.click_on_the_object('%s/div[%s]/h3/a' % (self.goods_container, number))
