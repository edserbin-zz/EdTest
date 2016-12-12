from ..pages.base_page import BasePage


class ComparisonPage(BasePage):

    delete_button = '//span[@class="b-products-compare-list__closer-button js-remove-from-comparison"]'
    send_mail_button = '//*[@id="comparison_send_to_email"]'
    input_email = '//input[@id="comparison-email"]'
    send_mail_button_in_window = '//*[@id="submit_button"]'

    def __init__(self, driver):
        super(ComparisonPage, self).__init__(driver)
        self.url += '/comparison/list'

    def remove_good_from_list(self, number=1):
        self.click_on_the_object('//tr[@class="js-comparison-product-item"][%s]%s' % (number, self.delete_button))

    def send_email(self, email):
        self.click_on_the_object(self.send_mail_button)
        self.driver.switch_to_active_element()
        self.enter_text_into_field(self.input_email, email)
        self.click_on_the_object(self.send_mail_button_in_window)
