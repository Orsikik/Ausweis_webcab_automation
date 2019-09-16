from pytest import fixture
from selenium import webdriver


@fixture(scope='session') # or 'function' if I want to open a new browser window in each function
def chrome_browser():
    browser = webdriver.Chrome()
    return browser

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests")

@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")