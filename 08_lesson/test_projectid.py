from yougile_api import YouGileProjectAPI

# Данные для авторизации (подтягиваются из окружения)
base_url = 'https://ru.yougile.com/api-v2'
login_name = 'misha.vish@mail.ru'
password_name = 'QAtesting888700'
name_project = 'Тест'
api = YouGileProjectAPI(base_url)
# Метод post(создание проекта)
def test_create_project_positive():
    company_id = api.get_company_id(login=login_name, password=password_name, name=name_project)
    api.get_token(login=login_name, password=password_name, id_company=company_id)
    response = api.create_project("New Test Project")
    assert response.status_code == 201

def test_create_project_negative_empty_title():
    Company_id = api.get_company_id(login=login_name, password=password_name, name=name_project)
    api.get_token(login=login_name, password=password_name, id_company=Company_id)
    response = api.create_project("")
    assert response.status_code == 400

def test_search_project_by_id_positive():
    company_id = api.get_company_id(login=login_name, password=password_name, name=name_project)
    api.get_token(login=login_name, password=password_name, id_company=company_id)
    search = api.search_project_by_id()
    assert search["id"] is not None

def test_search_project_by_id_negative():
    company_id = api.get_company_id(login=login_name, password=password_name, name=name_project)
    api.get_token(login=login_name, password=password_name, id_company=company_id)
    search = api.search_project_by_id_negative()
    assert search.status_code == 404

def test_change_project_status_positive():
    company_id = api.get_company_id(login=login_name, password=password_name, name=name_project)
    api.get_token(login=login_name, password=password_name, id_company=company_id)
    search = api.search_project_by_id()['id']
    swap = api.change_project_status(id_project=search)
    assert swap.status_code == 200

def test_change_project_status_negative():
    company_id = api.get_company_id(login=login_name, password=password_name, name=name_project)
    api.get_token(login=login_name, password=password_name, id_company=company_id)
    search = api.search_project_by_id()
    swap = api.change_project_status(id_project=search)
    assert swap.status_code == 404