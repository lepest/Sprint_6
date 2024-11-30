import allure

from pages.base_page import TestBasePage
from locators.order_page_locators import OrderPageLocators

class TestOrderPage(TestBasePage):

    @allure.step('Выбрать время проката')
    def select_rental_period(self, period):
        self.click_element_with_wait(OrderPageLocators.RENTAL_PERIOD)
        format_locator_rental_period = self.get_format_locators(OrderPageLocators.PERIOD_LOCATOR, period)
        self.scroll_to_element(format_locator_rental_period)
        self.click_element_with_wait(format_locator_rental_period)

    @allure.step('Поле с вводом и выбором станции')
    def select_field_station(self, station):
        self.click_element_with_wait(OrderPageLocators.STATION_FIELD_INPUT)
        self.enter_text_to_field(OrderPageLocators.STATION_FIELD_INPUT, station)
        self.find_element_with_wait(OrderPageLocators.LIST_STATION)
        self.click_element_with_wait(OrderPageLocators.STATION_FIELD_CLICK)

    @allure.step('Выбрать дату')
    def select_field_date(self, date):
        self.enter_text_to_field(OrderPageLocators.DATE_FIELD, date)
        self.find_element_with_wait(OrderPageLocators.DATE_CALENDAR)
        self.click_element_with_wait(OrderPageLocators.SELECT_DATE)

    @allure.step('Выбрать цвет самоката')
    def select_color_scooter(self, color):
        format_locator_color_scooter = self.get_format_locators(OrderPageLocators.COLOR_SCOOTER, color)
        self.click_element_with_wait(format_locator_color_scooter)

    @allure.step('Заполнение формы заказа')
    def fill_in_first_form_order_scooter(self, name, surname, address, station, telephone, date, period, color, comment):
        self.find_element_with_wait(OrderPageLocators.ORDER_FORM)
        self.enter_text_to_field(OrderPageLocators.NAME_FIELD, name)
        self.enter_text_to_field(OrderPageLocators.SURNAME_FIELD, surname)
        self.enter_text_to_field(OrderPageLocators.ADDRESS_FIELD, address)
        self.select_field_station(station)
        self.enter_text_to_field(OrderPageLocators.TELEPHONE_FIELD, telephone)
        self.click_element_with_wait(OrderPageLocators.BUTTON_NEXT)
        self.find_element_with_wait(OrderPageLocators.ORDER_FORM)
        self.select_field_date(date)
        self.select_rental_period(period)
        self.select_color_scooter(color)
        self.enter_text_to_field(OrderPageLocators.COMMENT_FIELD, comment)
        self.click_element_with_wait(OrderPageLocators.ORDER_BUTTON_FINISH)
        self.find_element_with_wait(OrderPageLocators.WINDOW_ORDER_CONFIRMATION)
        self.click_element_with_wait(OrderPageLocators.BUTTON_YES)
        result = self.get_text_from_element(OrderPageLocators.WINDOW_SUCCESSFUL_ORDER)
        return result

    @allure.step('Клик на логотип Самокат')
    def click_logo_scooter(self):
        self.click_element_with_wait(OrderPageLocators.LOGO_SCOOTER)
        self.find_element_with_wait(OrderPageLocators.ELEMENTS_MAIN_PAGE)
