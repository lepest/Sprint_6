from selenium.webdriver.common.by import By

class OrderPageLocators:

    ELEMENTS_MAIN_PAGE = By.XPATH, "//*[@class='Home_SecondPart__T0Okx']"  # Элементы загрузки главной страницы
    ORDER_BUTTON_UP = By.XPATH, "//button[@class='Button_Button__ra12g']" #Кнопка "Заказать"
    ORDER_BUTTON_MIDDLE = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']" # Кнопка "Заказать" в середине страницы
    ORDER_FORM = By.XPATH, "//div[@class='Order_Content__bmtHS']" #Форма заказа
    NAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']" #Поле "Имя"
    SURNAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']" #Поле "Фамилия"
    ADDRESS_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']" #Поле "Адрес"
    STATION_FIELD_CLICK = By.XPATH, "//div[@class='select-search__select']/ul/li[1]/button/div[2]" #Выбор станции из выпадающего списка
    STATION_FIELD_INPUT = By.XPATH, "//div/div/input[@placeholder='* Станция метро']" #Поле "Станция", ввести текст
    LIST_STATION = By.XPATH, "//div[@class='select-search__select']"  # Выпадющий список станций
    TELEPHONE_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']" #Поле "Телефон"
    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']" #Кнопка "Далее"
    DATE_FIELD = By.XPATH, "//input[@placeholder='* Когда привезти самокат']" #Поле "Дата"
    DATE_CALENDAR = By.XPATH, "//div[@class='react-datepicker__tab-loop']" #Отображение календаря из поля "Дата"
    SELECT_DATE = By.XPATH, "//div[@class='react-datepicker__week']/div[@tabindex='0']"
    RENTAL_PERIOD = By.XPATH, "//span[@class='Dropdown-arrow']" #Поле "Срок аренды"
    LIST_RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-menu']" #Список выбора срока аренды
    PERIOD_LOCATOR = By.XPATH, "//div[text()='{}']" #Срок аренды, отдельный пункт
    COLOR_SCOOTER = By.XPATH, "//input[@id='{}']" #Чексбокс - выбор цвета самоката
    BLACK_COLOR_SCOOTER = By.XPATH, "//input[@id='black']" #Локатор чёрного самоката
    GREY_COLOR_SCOOTER = By.XPATH, "//input[@id='grey']" #Локатор серого самоката
    COMMENT_FIELD = By.XPATH, "//input[@placeholder='Комментарий для курьера']" #Поле "Комментарий"
    ORDER_BUTTON_FINISH = By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']" #Кнопка "Заказать" на форме заказа
    WINDOW_ORDER_CONFIRMATION = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']" #Окно подтверждения заказа
    BUTTON_YES = By.XPATH, "//button[text()='Да']" #Кнопка "Да" в окне подтверждения заказа
    WINDOW_SUCCESSFUL_ORDER = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']" #Окно "Заказ оформлен"
    LOGO_SCOOTER = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']" #Логотип Самокат