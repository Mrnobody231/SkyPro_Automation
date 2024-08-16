import requests


class Employee:
    def __init__(self, url):
        self.url = url
    
    def authorization(self, authorization):
        access_token = requests.post(
            self.url + "/auth/login", json=authorization)
        return access_token.json()["userToken"]

    def get_company_id(self, is_active: bool):
        company = requests.get(
            self.url + "company", active=is_active
        )
        return company.json()["id"]  # Why json() isn't yellow
    
    def get_employee_list(self, company_id):
        company = {
            "company": company_id
        }
        employee = requests.get(self.url + "/employee", params=company)
        return employee.json()
    
    def add_employee(
            self, id: int, first_name: str, last_name: str, middle_name: str,
            company_id: int, email: str, url: str, phone: str,
            birth_date: str, is_active: bool
            ):
        my_header = self.authorization()  # Do I neeed to add ["x-client-token"] ?
        employee_data = {
            "id": id,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "companyId": company_id,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birth_date,
            "isActive": is_active
        }
        employee_id = requests.post(
            self.url + "/employee", header=my_header, json=employee_data)
        return employee_id.json()["id"]  # Why json() isn't yellow
      
    def get_employee_by_id(self):
        employee = requests.get(
            f"{self.url}/employee/{self.add_employee}")
        return employee.json()
    
    def change_employee(
            self, last_name: str, email: str,
            is_active: bool, phone=None, url=None
              ):
        self.get_employee_by_id["id"]
        self.authorization()
        {
            "lastName": last_name,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": is_active
            }
        response = requests.patch(
            f"{self.url}/employee/{self.add_employee}")
        return response.json()