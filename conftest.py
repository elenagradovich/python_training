import pytest
from fixture.application import Application
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    global fixture
    global target#Ссылка на конфигурационный файл
    browser = request.config.getoption("--browser")#получаем из def pytest_addoption(parser)
   #Путь к текущему файлу
    web_config = load_config(request.config.getoption("--target"))['web']
    # if target is None:
    #     config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
    #     #Чтение файла конфигурации
    #     with open(config_file) as f:#f объект кот.указывает на открытый файл
    #         target = json.load(f)
    # #Пользователь создает новую фикстуру
    if fixture is None or not fixture.is_valid():#Переинициализация фикстуры, с ней что-то случилось и нужно заново создать
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                          user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture



@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):#Передается парсер коммандной строки у которого есть метод addoption
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

def pytest_generate_tests(metafunc): #metafunc -получение инфо о тестовой функции
    #параметризация тестов путём "внедрения" тестовых данных в фикстуру при помощи hook-функции pytest_generate_tests
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file))as f:#
        return jsonpickle.decode(f.read())

