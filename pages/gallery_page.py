# coding=utf-8

from ..pages.base_page import BasePage


class GalleryPage(BasePage):

    goods_container = '//div[@class="b-product-line b-product-line_size_wide js-gallery-container"]'

    def __init__(self, driver, goods='Velosipednye-shiny'):
        super(GalleryPage, self).__init__(driver)
        self.url += '/%s?output=gallery' % goods

    def select_goods(self, count):
        """select or deselect the goods """
        for i in range(1, count+1):
            self.hover_element('%s/div[@itemscope="itemscope"][%s]' % (self.goods_container, str(i)))
            self.click_on_the_object('%s/div[@itemscope="itemscope"][%s]//span/span/span'
                                     % (self.goods_container, str(i)))

    def go_to_goods(self, number=1):
        """select first good from list"""
        self.click_on_the_object('%s/div[@itemscope="itemscope"][%s]//img' % (self.goods_container, number))