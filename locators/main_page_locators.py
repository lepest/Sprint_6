from selenium.webdriver.common.by import By

class MainPageLocators:

    ELEMENTS_MAIN_PAGE = By.XPATH, "//*[@class='Home_SecondPart__T0Okx']" #Элементы загрузки главной страницы
    LIST_QUESTIONS = By.XPATH, "//*[@class='Home_FAQ__3uVm4']" #Список вопросов
    QUESTION = By.XPATH, "//div[@id='accordion__heading-{}']" #Вопрос
    ANSWER = By.XPATH, "//div[@id='accordion__panel-{}']" #Ответ
    TEXT_HEADER_MAIN_PAGE = "//div[@class='Home_Header__iJKdX']"
    ORDER_BUTTON_UP = By.XPATH, "//button[@class='Button_Button__ra12g']"  # Кнопка "Заказать"
    LOGO_YANDEX = By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"
    LOGO_DZEN = By.XPATH, "//a[@class='dzen-layout--desktop-base-header__logoLink-2h']"
    MAIN_PAGE_DZEN = By.XPATH, "//div[@class='dzen-desktop--content-micro-app__contentWrapper-NX']"