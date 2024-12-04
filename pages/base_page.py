import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    driver = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator)

    @allure.step('Клик на элемент')
    def click_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    @allure.step('Ввод текста в поле')
    def enter_text_to_field(self, locator, text):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получить текст из элемента')
    def get_text_from_element(self, locator):
        element = self.driver.find_element(*locator).text
        return element

    @allure.step('Прокручивание до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Форматирование локаторов')
    def get_format_locators(self, data_locator, data):
        method, locator = data_locator
        locator = locator.format(data)
        return method, locator

    @allure.step('Переход на другую вкладку')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Получить url')
    def get_url(self):
        return self.driver.current_url