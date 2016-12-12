import pytest

from base_test import check_failed
from temp_mail.temp_email import TempEmail
from test_logic import TestLogic


class TestScenarios(TestLogic):

    @pytest.mark.parametrize("name", [
        'BS',
        'book'
    ])
    def test_parametrize(self, name):
        self.go_to_main_page()
        self.search_item(name)
        self.go_to_good(1)
        self.click_on_selected_of_goods()
        count = self.return_count_of_items_in_selected()
        assert count == 1

    @check_failed
    def test_end_to_end_1(self):
        self.go_to_main_page()
        self.search_item('book')
        self.change_view_representation('list')
        self.select_goods(4)
        count = self.return_count_of_items_in_selected()
        assert count == 4
        self.go_to_good(4)
        self.click_on_selected_of_goods()
        count = self.return_count_of_items_in_selected()
        assert count == 3
        mail = TempEmail()
        self.go_to_comparison()
        self.send_email_with_comprasion(mail.email)
        assert 'Prom.ua' in mail.get_email_by_number(1).get('mail_from')

    @check_failed
    def test_end_to_end_2(self):
        self.go_to_main_page()
        self.search_item('book')
        self.change_view_representation('list')
        self.change_view_representation('gallery')
        self.select_goods(3)
        count = self.return_count_of_items_in_selected()
        assert count == 3
        self.go_to_good(1)
        self.click_on_selected_of_goods()
        count = self.return_count_of_items_in_selected()
        assert count == 2
        self.go_to_comparison()
        self.delete_good_from_comprasion(1)
        count = self.return_count_of_items_in_selected()
        assert count == 1


    @check_failed
    def test_failed(self):
        self.go_to_main_page()
        self.search_item('book')
        assert True is False
