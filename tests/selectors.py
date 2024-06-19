# xpaths для ввода данных в форме регистрации https://stellarburgers.nomoreparties.site/register

REGISTRATION_HEADER = ".//h2[text()='Регистрация']"             # заголовок 'Регистрация' на странице регистрации
REGISTRATION_INPUT_NAME = ".//fieldset[1]//input"               # поле ввода Имя при регистрации
REGISTRATION_INPUT_EMAIL = ".//fieldset[2]//input"              # поле ввода Email при регистрации
REGISTRATION_INPUT_PASSWORD = ".//fieldset[3]//input"           # поле ввода Пароль при регистрации
REGISTRATION_BUTTON = ".//button[text()='Зарегистрироваться']"  # кнопка 'Зарегистрироваться'


# xpaths для формы логина https://stellarburgers.nomoreparties.site/login
LOG_IN_LINK = ".//a[@href='/login']"                             # ссылка на вход в аккаунт
ENTRY_HEADER = ".//h2[text()='Вход']"                            # заголовок 'Вход' на странице логина
ENTRY_INPUT_LOGIN = ".//fieldset[1]//input"                      # поле ввода login (по совместительству email)
ENTRY_INPUT_PASSWORD = ".//fieldset[2]//input"                   # поле ввода Пароль
ENTRY_BUTTON = ".//button[text()='Войти']"                       # кнопка 'Войти'
RECOVER_PASSWORD_LINK = "//p[2]/a[@href='/forgot-password']"     # ссылка для восстановления пароля
REGISTRATION_LINK = "//p[1]/a[@href='/register']"                # ссылка на регистрацию
INCORRECT_PASSWORD_MESSAGE = \
    ".//fieldset[3]//p[text()='Некорректный пароль']"            # сообщение об ошибке при вводе некорректного пароля


# xpaths Восстановление пароля
PASSWORD_RECOVERY_HEADER = ".//h2[text()='Восстановление пароля']" # заголовок формы "Восстановление пароля"

# xpaths для элементов на главной странице https://stellarburgers.nomoreparties.site

LOG_IN_BUTTON = ".//button[text()='Войти в аккаунт']"  # кнопка Войти в аккаунт
MY_ACCOUNT_BUTTON = ".//p[text()='Личный Кабинет']"    # кнопка для перехода в Личный кабинет
MAKE_ORDER_BUTTON = ".//section[2]//button"            # кнопка 'Оформить заказ' на главной странице, когда пользователь уже вошел в аккаунт

# CSS селекторы для этементов на главной странице
CONSTRUCTOR_BUTTON = "div li:nth-child(1) p"           # кнопка перехода в раздел 'Конструктор'
LOGO = "div svg"                                       # логотип

# xpath элементов раздела выбора ингредиентов
MAKE_BURGER_HEADER = ".//h1[text()='Соберите бургер']"       # заголовок формы выбора ингредиентов 'Соберите бургер'
BUNS_BUTTON = ".//span[text()='Булки']"                      # кнопка перехода к разделу Булки
BUNS_HEADER = "//h2[1]"                                      # заголовок 'Булки'
SAUCE_BUTTON = ".//span[text()='Соусы']"                     # кнопка перехода к разделу Соусы
SAUCE_HEADER = ".//h2[2]"                                    # заголовок 'Соусы'
FILLING_BUTTON = ".//span[text()='Начинки']"                 # кнопка перехода к разделу Начинки
FILLING_HEADER = ".//h2[3]"                                  # заголовок 'Начинки'
LAST_INGREDIENT = "//section[1]/div[2]/ul[3]/a[last()]/p"    # последний элемент в списке всех ингредиентов

# xpath элементов на странице профиля

PROFILE_HEADER = ".//li[1]/a[@href='/account/profile']"                        # заголовок Профиль на странице профиля
LOGOUT_BUTTON = ".//li[3]/button[text()='Выход']"                              # кнопка выхода из аккаунта
PROFILE_USER_EMAIL = \
    ".//li[2][@class='Profile_profileListItem__2th0t mb-6']//input[@value]"    # поле Email в профиле пользователя
