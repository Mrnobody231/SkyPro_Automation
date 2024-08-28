import allure
from SkyPro_Automation.Lesson_10.data_base_postgresql.DataBase import DataBase
from SkyPro_Automation.Lesson_10.data_base_postgresql.Employee import Employee
from SkyPro_Automation.Lesson_10.data_base_postgresql.constants import *

api = Employee(X_CLIENTS_URL)
db = DataBase(DB_CONNECTION)

@allure.severity("Critical")
@allure.title("DataBase tables")
@allure.description("Connect to postgreSQL base and check according to assert configuration")
@allure.feature("Get")
def test_db_connection():
   with allure.step("Get table names in data base"):
      table_names =  db.db_table_names()
   with allure.step("Check if index 1 has the name 'company'"):
      assert table_names[1] == 'company'
   with allure.step("Check if index 2 has the name 'employee'"):
      assert table_names[2] == 'employee'

@allure.severity("Critical")
@allure.title("Employee list")
@allure.description("Check if created employee info in data base has the same length as API request ")
@allure.feature("Get")
def test_get_employee_list():
   db.create_company("Pigu LT", "Goods and Stuff")
   max_com_id = db.last_company_id()
   db.create_employee(max_com_id, 'Romelu', 'Lukaku', 'Beast',
                      'email@gmail.com', '123456789', True)
   db_list =  db.get_employee_list(max_com_id)
   api_list = api.get_employee_list(max_com_id)
   with allure.step("Check if data base length is the same as by API request"):
      assert len(db_list) == len(api_list)
   api_employee = (api.get_employee_list(max_com_id))[0]
   employee_id = api_employee['id']
   db.delete_employee(employee_id)
   db.delete_company(max_com_id)

@allure.severity("Critical")
@allure.title("Create employee")
@allure.description("Check if created employee info in data base is the same as in API request ")
@allure.feature("Create")
def test_create_employee():
   db.create_company("Sber", "Banking Service")
   max_com_id = db.last_company_id()
   db.create_employee(max_com_id, "German", "Gref", "Beast",
                      "email@gmail.com", "123456789", True)
   api_employee = (api.get_employee_list(max_com_id))[0]
   employee_id = api_employee['id']
   with allure.step("Check if employee list is not empty"):
      assert api_employee is not None
   with allure.step("Check if employee's 'firstName' is 'German'"):
      assert api_employee['firstName'] == "German"
   with allure.step("Check if employee's 'lastName' is 'Gref'"):
      assert api_employee['lastName'] == "Gref"
   with allure.step("Check if employee's 'email' is 'email@gmail.com'"):
      assert api_employee['email'] == "email@gmail.com"
   with allure.step("Check if employee's 'companyId' has the direct company ID "):
      assert api_employee['companyId'] == max_com_id
   db.delete_employee(employee_id)
   db.delete_company(max_com_id)

@allure.severity("Critical")
@allure.title("Get employee by ID")
@allure.description("Check if created employee info in data base is the same as in API request according"
                    " to employee 'id' ")
@allure.feature("Get")
def test_get_employee_by_id():
   db.create_company("Sber", "Banking Service")
   max_com_id = db.last_company_id()
   db.create_employee(max_com_id, "German", "Gref", "Beast",
                      "email@gmail.com", "123456789", True)
   employee_id = db.last_employee_id(max_com_id)
   employee_result = api.get_employee_by_id(employee_id)
   with allure.step("Check if employee's 'firstName' is 'German'"):
      assert employee_result['firstName'] == 'German'
   with allure.step("Check if employee's 'email' is 'email@gmail.com'"):
      assert employee_result['email'] ==  "email@gmail.com"
   with allure.step("Check if employee's 'is Active' is True"):
      assert employee_result['isActive'] == True
   with allure.step("Check if employee's 'middleName' is 'Beast'"):
      assert employee_result['middleName'] == "Beast"
   db.delete_employee(employee_id)
   db.delete_company(max_com_id)

@allure.severity("Critical")
@allure.title("Update employee")
@allure.description("Check if updated employee info as 'lastName' in data base is the same as in API request ")
@allure.feature("Create")
def test_update_employee_info():
   db.create_company("Sber", "Banking Service")
   max_com_id = db.last_company_id()
   db.create_employee(max_com_id, "German", "Gref", "Beast",
                      "email@gmail.com", "123456789", True)
   employee_id = db.last_employee_id(max_com_id)
   db.update_employee("Oskar", employee_id)
   result = (api.get_employee_list(max_com_id))[0]
   with allure.step("Check if employee's 'lastName' was successfully changed into 'Oskar'"):
      assert result['lastName'] == "Oskar"
   db.delete_employee(employee_id)
   db.delete_company(max_com_id)