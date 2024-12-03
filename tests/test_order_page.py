import pytest
import allure

from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators
from data import TestUrl
from data import TestDataOrder

class TestElementOrderPage:

    @allure.title('Тестирование заказа самоката путем нажатия кнопок "Заказать"')
    @pytest.mark.parametrize(
        'locator, data_for_order',
        [
            (OrderPageLocators.ORDER_BUTTON_UP, TestDataOrder.data_order_first.values()),
            (OrderPageLocators.ORDER_BUTTON_MIDDLE, TestDataOrder.data_order_second.values())
        ]
    )
    def test_order_scooter(self, driver, locator, data_for_order):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        driver.get(TestUrl.main_page_url)
        main_page.click_order_button(locator)
        finish_window_text = order_page.fill_in_first_form_order_scooter(*data_for_order)
        assert "Заказ оформлен" in finish_window_text

    @allure.title('Тестирование перехода на главную страницу по клику на логотип Самокат')
    def test_click_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        driver.get(TestUrl.main_page_url)
        main_page.click_order_button_for_test_logo()
        order_page.click_logo_scooter()
        assert driver.current_url == TestUrl.main_page_url

