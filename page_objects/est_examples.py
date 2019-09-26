# Examples of console commands
# pytest -m smoke      ---- to start all test with mart smoke
# pytest -m "body and engine"    ---- to start testing only tests with body and engine marks in same test
# pytest -m "body or engine"     ---- to statr testing tests with body or engine marks
# pytest -m "not entertainment"  ---- to start all test exept enterteintment
# pytest --markers  ----- overview all testing system markers
# pytest --html="results" ---- to create html file to represent test results in better way
# pytest --junitxml="result.xml" ---- the same but in xml
#

from pytest import mark


@mark.skip(reason='Describing why is skipping is needed')
@mark.test
def test_fixture(chrome_browser):
    chrome_browser.get('https://www.google.com')
    assert True

@mark.skip
@mark.env
def test_environment_is_prod(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://my.ausweis.io/ru/accounts/login/'
    assert port == 80


@mark.xfail(reason='Describing why is skipping is needed')
@mark.env
def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://www.ausweis.io/en/'
    assert port == 8080

@mark.skip
@mark.parametrize('tv_brand', [
    ('Samsung'),
    ('Sony'),
    ('Vizio')
])
def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")




