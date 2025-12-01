import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es, fr, ru, etc.")


def pytest_configure(config):
    # Регистрируем кастомные метки
    config.addinivalue_line(
        "markers", "need_review: tests for peer review"
    )
    config.addinivalue_line(
        "markers", "login_guest: tests for guest login"
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {
        'intl.accept_languages': user_language
    })

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    yield browser
    browser.quit()