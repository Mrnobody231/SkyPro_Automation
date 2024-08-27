import requests

from SkyPro_Automation.Lesson_9.constants import AUTHORIZATION


class Employee:
    def __init__(self, url):
        self.url = url
    
    def authorization(self, authorization):
        access_token = requests.post(
            self.url + "/auth/login", json=authorization)
        return access_token.json()["userToken"]

    def create_company(self, name, description=None):
        company = {
            'name': name,
            'description': description
        }
        my_header = {}
        my_header['x-client-token'] = self.authorization(AUTHORIZATION)
        my_company = requests.post(self.url + '/company', headers=my_header,
                                   json=company)
        return my_company.json()

    def get_company_id(self):
        company = requests.get(
            self.url + "/company"
        )
        return company.json()[0]["id"]
    
    def get_employee_list(self, company_id):
        company = {
            "company": company_id
        }
        employee = requests.get(self.url + "/employee", params=company)
        return employee.json()
    
    def add_employee(
            self, first_name: str, last_name: str, middle_name: str,
            email: str, phone: str, is_active: bool
            ):
        my_header = {}
        my_header['x-client-token'] = self.authorization(AUTHORIZATION)
        employee_data = {
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "companyId": self.get_company_id(),
            "email": email,
            "phone": phone,
            "isActive": is_active
        }
        employee_id = requests.post(
            self.url + "/employee", headers=my_header, json=employee_data)
        return employee_id.json()["id"]

    def get_employee_by_id(self, employee_id):
        resp = requests.get(self.url + '/employee/' + str(employee_id))
        return resp.json()
    
    def change_employee(
            self, employee_id: int, last_name: str, email: str,
            is_active: bool, phone=None, url=None
              ):
        my_header = {}
        my_header["x-client-token"] = self.authorization(AUTHORIZATION)
        body = {
        "lastName": last_name,
        "email": email,
        "url": url,
        "phone": phone,
        "isActive": is_active
        }
        response = requests.patch(self.url + '/employee/' + str(employee_id),
                                  headers=my_header, json=body)
        return response.json()