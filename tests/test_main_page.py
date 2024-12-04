import pytest
import allure

from pages.main_page import MainPage
from data import TestData
from data import TestUrl

class TestElementMainPage:

    @allure.title('Тестирование вопросов и ответов')
    @pytest.mark.parametrize('number', TestData.question_numbers)
    def test_question_and_answer(self, driver, number):
        main_page = MainPage(driver)
        driver.get(TestUrl.main_page_url)
        main_page.clik_to_question(number)
        result = main_page.check_answer_to_question(number)
        assert result == TestData.answers[number]

    @allure.title('Тестирование перехода на главную страницу Дзен по клику на логотип Яндекс')
    def test_click_logo_yandex(self, driver):
        main_page = MainPage(driver)
        driver.get(TestUrl.main_page_url)
        main_page.click_logo_yandex()
        assert main_page.switch_to_dzen() == 'https://dzen.ru/?yredirect=true'