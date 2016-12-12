from base_test import BaseTest
from pages.base_page import BasePage
from pages.comparison_page import ComparisonPage
from pages.gallery_page import GalleryPage
from pages.goods_page import GoodsPage
from pages.list_page import ListPage


class TestLogic(BaseTest):

    def go_to_main_page(self):
        self.page = BasePage(self.driver)
        self.page.navigate()

    def search_item(self, item_name):
        self.page.search_good(item_name)
        # after the searching we look goods in gallery view
        self.page = GalleryPage(self.driver)

    def change_view_representation(self, view='gallery'):
        "change view on gallery or list"
        if view == 'gallery':
            self.page.select_gallery_view()
            self.page = GalleryPage(self.driver)
        if view == 'list':
            self.page.select_list_view()
            self.page = ListPage(self.driver)

    def select_goods(self, count_of_goods):
        self.page.select_goods(count_of_goods)

    def go_to_good(self, number):
        self.page.go_to_goods(number)
        self.page = GoodsPage(self.driver)

    def click_on_selected_of_goods(self):
        """
        click on "star" button , and add or remove good from
          selected
        """
        self.page.select_goods()

    def go_to_comparison(self):
        self.page.go_to_comparison()
        self.page = ComparisonPage(self.driver)

    def delete_good_from_comprasion(self, number):
        self.page.remove_good_from_list(number)

    def send_email_with_comprasion(self, mail):
        self.page.send_email(mail)

    def return_count_of_items_in_selected(self):
        return self.page.return_count_of_goods_in_selected()
