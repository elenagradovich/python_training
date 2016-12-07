import pytest
from fixture.application import Application
import json

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        #Чтение файла конфигурации
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    #Пользователь создает новую фикстуру
    if fixture is None or not fixture.is_valid():#Переинициализация фикстуры, с ней что-то случилось и нужно заново создать
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

