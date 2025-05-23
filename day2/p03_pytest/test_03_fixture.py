import pytest


@pytest.fixture
def browser():
    class Browser:
        def __init__(self,name):
            self.name=name


    return Browser("firefox")


def test_call_browser(browser):

    assert  browser.name=="chrome"