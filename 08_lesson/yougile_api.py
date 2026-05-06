import requests
auth_url = '/auth/keys'
workers_url = '/users'
company_url = '/auth/companies'
base_url = 'https://ru.yougile.com/api-v2'
project_url = '/projects'
swap_url = '/projects/'
class YouGileProjectAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.id_company = None
        self.token = None
    # получение 
    # 1. id компании 
    # 2. токена 
    # 3. id сотрудника
    # для дальнейших методов    
    def get_company_id(self, login, password, name):
        url = self.base_url+company_url
        payload = {'login': login, 'password': password, 'name': name}
        resp = requests.post(url, json=payload)
        content = resp.json().get("content", [{}])
        self.id_company = content[0].get("id")
        return self.id_company

    def get_token(self, login, password, id_company):
        url = self.base_url+auth_url
        payload = {'login': login, 'password': password, 'companyId': id_company}
        response = requests.post(url, json=payload)
        self.token = response.json().get("key")
        return self.token
    def get_list_projects(self):
        url = self.base_url+project_url
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        return response.json()
    # Создание проекта
    def create_project(self, project_name):
        url = self.base_url+project_url
        payload = {"title": project_name}
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(url, json=payload, headers=headers)
        return response
    # Поиск по id проекта
    def search_project_by_id(self):
        id_project = self.get_list_projects()["content"][1]["id"]
        url = self.base_url+project_url+f"/{id_project}"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        return response.json()
    # поиск по id проекта с не правильным токеном
    def search_project_by_id_negative(self):
        id_project = self.get_list_projects()["content"][1]["id"]
        url = self.base_url+project_url+f"/{123456}"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        return response
    # изменение статуса проекта на удаленный
    def change_project_status(self, id_project):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        status = {"deleted": True}
        response = requests.put(self.base_url+swap_url+f"/{id_project}", json=status, headers=headers)
        return response