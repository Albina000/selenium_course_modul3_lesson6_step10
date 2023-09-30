import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# с помощью pytest_addoption и фикстуры request настраиваем тестовое окружение (передача параметров через командную строку)
# добавим обработчик опций
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose a language: es or fr")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language") # для запроса значения параметра
    browser = None
    if language == "es":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif language == "fr":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()


