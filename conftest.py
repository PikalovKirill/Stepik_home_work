import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



#волщебная встроенная функция для обработки инфы из терминала
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose languages")




@pytest.fixture(scope="function")
def browser(request):

    #хуй знает зачем нужна данная строка
    browser = None 
    
    #логика обработки командной строки
    language = request.config.getoption("language")
    
    #передача в options языка
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    #вывод о старте браузера
    print("\nstart chrome browser for test..")

    #старт браузера, в зависимости от выбраного языка
    browser = webdriver.Chrome(options=options)

    #код после обрабоки тела теста
    yield browser 
    time.sleep(2)
    print("\nquit browser..")
    browser.quit()