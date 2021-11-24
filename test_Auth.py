import allure


class TestShit:
    @allure.id("2")
    @allure.title("Авторизация через GitHub")
    @allure.tag("critical", "web")
    @allure.label("suite", "Auth")
    @allure.label("owner", "admin")
    def test_shit(self):
        with allure.step("Открываем главную страницу"):
            pass
        with allure.step("Выбираем авторизацию через GitHub"):
            with allure.step("Нажимаем кнопку Войти"):
                pass
        with allure.step("Нажимаем кнопку Github"):
            pass
        with allure.step("Авторизуемся как пользователь eroshenkoam"):
            with allure.step("Вводим email eroshenkoam@gmail.com"):
                pass
        with allure.step("Вводим пароль 23792"):
            pass
        with allure.step("Нажимаем кнопку Войти"):
            pass
        with allure.step("Проверяем, что авторизовались как пользовать eroshenkoam"):
            with allure.step("Должны вернуться на главную страницу"):
                pass
        with allure.step("Логин пользователя должен быть eroshenkoam"):
            pass
        with allure.step("Имя пользователя должно быть Артем Ерошенко"):
            pass


    @allure.id("4")
    @allure.title("Авторизация через Azure")
    @allure.tag("critical", "web")
    @allure.label("suite", "Auth")
    @allure.label("owner", "admin")
    def test_azure(self):
        with allure.step("Открываем главную страницу"):
            pass
        with allure.step("Выбираем авторизацию через Azure"):
            with allure.step("Нажимаем кнопку Войти"):
                pass
        with allure.step("Нажимаем кнопку Azure"):
            pass
        with allure.step("Авторизуемся как пользователь eroshenkoam"):
            with allure.step("Вводим email eroshenkoam@gmail.com"):
                pass
        with allure.step("Вводим пароль 23792"):
            pass
        with allure.step("Нажимаем кнопку Войти"):
            pass
        with allure.step("Проверяем, что авторизовались как пользовать eroshenkoam"):
            with allure.step("Должны вернуться на главную страницу"):
                pass
        with allure.step("Логин пользователя должен быть eroshenkoam"):
            pass
        with allure.step("Имя пользователя должно быть Артем Ерошенко"):
            pass
