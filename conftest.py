import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    #Пользователь создает новую фикстуру
    if fixture is None:
        fixture = Application()
    else:
        #Переинициализация фикстуры, с ней что-то случилось и нужно заново создать
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
