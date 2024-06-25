# xpaths для ввода данных в форме регистрации https://stellarburgers.nomoreparties.site/register

REGISTRATION_HEADER = "//h2[text()='Регистрация']"                   # заголовок 'Регистрация' на странице регистрации
REGISTRATION_INPUT_NAME = "//div/label[text()='Имя']"                # поле ввода Имя при регистрации
REGISTRATION_INPUT_EMAIL = "//div/label[text()='Email']"             # поле ввода Email при регистрации
REGISTRATION_INPUT_PASSWORD = "//div/label[text()='Пароль']"         # поле ввода Пароль при регистрации
REGISTRATION_BUTTON = "//button[text()='Зарегистрироваться']"        # кнопка 'Зарегистрироваться'
LOG_IN_LINK = "//a[@href='/login']"                                  # ссылка на вход в аккаунт со страницы регистрации

# xpaths для формы логина https://stellarburgers.nomoreparties.site/login
ENTRY_HEADER = "//h2[text()='Вход']"                                 # заголовок 'Вход' на странице логина
ENTRY_INPUT_LOGIN = "//input[@name='name']"                          # поле ввода login (по совместительству email)
ENTRY_INPUT_PASSWORD = "//input[@name='Пароль']"                     # поле ввода Пароль
ENTRY_BUTTON = "//button[text()='Войти']"                            # кнопка 'Войти'
RECOVER_PASSWORD_LINK = "//a[@href='/forgot-password']"              # ссылка для восстановления пароля
REGISTRATION_LINK = "//a[@href='/register']"                         # ссылка на регистрацию
INCORRECT_PASSWORD_MESSAGE = "//p[text()='Некорректный пароль']"     # сообщение об ошибке при вводе некорректного пароля


# xpaths Восстановление пароля
PASSWORD_RECOVERY_HEADER = "//h2[text()='Восстановление пароля']"    # заголовок формы "Восстановление пароля"

# xpaths для элементов на главной странице https://stellarburgers.nomoreparties.site

LOG_IN_BUTTON = "//button[text()='Войти в аккаунт']"                 # кнопка Войти в аккаунт
MY_ACCOUNT_BUTTON = "//p[text()='Личный Кабинет']"                   # кнопка для перехода в Личный кабинет
MAKE_ORDER_BUTTON = "//button[text()='Оформить заказ']"              # кнопка 'Оформить заказ' на главной странице, когда пользователь уже вошел в аккаунт

# CSS селекторы для этементов на главной странице
CONSTRUCTOR_BUTTON = "div li:nth-child(1) p"                         # кнопка перехода в раздел 'Конструктор'
LOGO = "div svg"                                                     # логотип

# xpath элементов раздела выбора ингредиентов
MAKE_BURGER_HEADER = "//h1[text()='Соберите бургер']"                # заголовок формы выбора ингредиентов 'Соберите бургер'
BUNS_BUTTON = "//span[text()='Булки']"                               # кнопка перехода к разделу Булки
BUNS_HEADER = "//h2[text()='Булки']"                                 # заголовок 'Булки'
SAUCE_BUTTON = "//span[text()='Соусы']"                              # кнопка перехода к разделу Соусы
SAUCE_HEADER = "//h2[text()=Соусы]"                                  # заголовок 'Соусы'
FILLING_BUTTON = "//span[text()='Начинки']"                          # кнопка перехода к разделу Начинки
FILLING_HEADER = "//h2[text()='Начинк']"                             # заголовок 'Начинки'
LAST_INGREDIENT = "//ul[last()]/a[last()]/img"                       # последний элемент в списке всех ингредиентов

# xpath элементов на странице профиля

PROFILE_HEADER = "//a[@href='/account/profile']"                     # заголовок Профиль на странице профиля
LOGOUT_BUTTON = "//button[text()='Выход']"                           # кнопка выхода из аккаунта
PROFILE_USER_EMAIL = "//input[@value='Email']"                       # поле Email в профиле пользователя
