import allure
from pages.base_page import TestBasePage
from locators.main_page_locators import MainPageLocators

class TestMainPage(TestBasePage):

    @allure.step('Поиск и нажатие на кнопку "Заказать", для обеих кнопок')
    def click_order_button(self, locator):
        self.find_element_with_wait(MainPageLocators.ELEMENTS_MAIN_PAGE)
        self.scroll_to_element(locator)
        self.click_element_with_wait(locator)

    @allure.step('Клик на вопрос')
    def clik_to_question(self, number):
        self.find_element_with_wait(MainPageLocators.ELEMENTS_MAIN_PAGE)
        format_question_locator = self.get_format_locators(MainPageLocators.QUESTION, number)
        self.scroll_to_element(format_question_locator)
        self.click_element_with_wait(format_question_locator)

    @allure.step('Получить ответ на вопрос')
    def get_answer_text(self, number):
        format_answer_locator = self.get_format_locators(MainPageLocators.ANSWER, number)
        return self.get_text_from_element(format_answer_locator)

    @allure.step('Проверить ответ на вопрос')
    def check_answer_to_question(self, number):
        self.clik_to_question(number)
        return self.get_answer_text(number)

    @allure.step('Нажатие на кнопки "Заказать" вверху страницы')
    def click_order_button_for_test_logo(self):
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_UP)

    @allure.step('Клик на логотип Яндекс')
    def click_logo_yandex(self):
        self.click_element_with_wait(MainPageLocators.LOGO_YANDEX)

    @allure.step('Переход на страницу Дзен')
    def switch_to_dzen(self):
        self.switch_to_window()
        self.find_element_with_wait(MainPageLocators.MAIN_PAGE_DZEN)