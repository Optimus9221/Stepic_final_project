import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='Choose browser: chrome or firefox',
    )
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Browser language, e.g. en or ru',
    )


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None

    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        options = ChromeOptions()
        options.add_argument(f'--lang={user_language}')
        options.add_experimental_option(
            'prefs',
            {'intl.accept_languages': user_language},
        )
        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        options = FirefoxOptions()
        options.set_preference('intl.accept_languages', user_language)
        options.set_preference('general.useragent.locale', user_language)

        snap_firefox = '/snap/firefox/current/usr/lib/firefox/firefox'
        if os.path.isfile(snap_firefox):
            options.binary_location = snap_firefox

        browser = webdriver.Firefox(options=options)

    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    yield browser
    print('\nquit browser..')
    browser.quit()