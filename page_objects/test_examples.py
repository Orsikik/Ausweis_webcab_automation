# Examples of console commands
# pytest -m smoke      ---- to start all test with mart smoke
# pytest -m "body and engine"    ---- to start testing only tests with body and engine marks in same test
# pytest -m "body or engine"     ---- to statr testing tests with body or engine marks
# pytest -m "not entertainment"  ---- to start all test exept enterteintment
# pytest --markers  ----- overview all testing system markers
# pytest --html="results" ---- to create html file to represent test results in better way
# pytest --junitxml="result.xml" -- the same but in xml
#



from pytest import mark


@mark.test
def test_fixture(chrome_browser):
    chrome_browser.get('https://www.google.com')
    assert True

@mark.env
def test_environment_is_qa(env):
    assert env == 'qa'

@mark.env
def test_environment_is_dev(env):
    assert env == 'prod'