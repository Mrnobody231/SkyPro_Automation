import requests
import allure

from SkyPro_Automation.Lesson_10.data_base_postgresql.constants import AUTHORIZATION


@allure.epic("Company and Employee API scripts")
class Employee:
    def __init__(self, url: str):
        self.url = url

    @allure.step("api. Get access token for API requests")
    def authorization(self, authorization: dict) -> dict:
        access_token = requests.post(
            self.url + "/auth/login", json=authorization)
        return access_token.json()["userToken"]

    @allure.step("api. Create company")
    def create_company(self, name: str, description=None) -> dict:
        company = {
            'name': name,
            'description': description
        }
        my_header = {}
        my_header['x-client-token'] = self.authorization(AUTHORIZATION)
        my_company = requests.post(self.url + '/company', headers=my_header,
                                   json=company)
        return my_company.json()

    @allure.step("api. Get last created company id")
    def get_company_id(self) -> int:
        company = requests.get(
            self.url + "/company"
        )
        return company.json()[0]["id"]

    @allure.step("api. Get employee list from current company")
    def get_employee_list(self, company_id: int) -> dict:
        company = {
            "company": company_id
        }
        employee = requests.get(self.url + "/employee", params=company)
        return employee.json()

    @allure.step("api. Create employee in current company")
    def add_employee(
            self, first_name: str, last_name: str, middle_name: str,
            email: str, phone: str, is_active: bool
            ) -> dict:
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

    @allure.step("api. Get current employee by id")
    def get_employee_by_id(self, employee_id: int) -> dict:
        resp = requests.get(self.url + '/employee/' + str(employee_id))
        return resp.json()

    @allure.step("api. Update employee info.")
    def change_employee(
            self, employee_id: int, last_name: str, email: str,
            is_active: bool, phone=None, url=None
              ) -> dict:
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