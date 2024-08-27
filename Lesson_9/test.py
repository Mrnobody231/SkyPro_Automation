from SkyPro_Automation.Lesson_9.DataBase import DataBase
from SkyPro_Automation.Lesson_9.Employee import Employee
from SkyPro_Automation.Lesson_9.constants import *

api = Employee(X_CLIENTS_URL)
db = DataBase(DB_CONNECTION)


def test_db_connection():
   table_names =  db.db_table_names()
   assert table_names[1] == 'company'
   assert table_names[2] == 'employee'

def test_get_employee_list():
   db.create_company("Pigu LT", "Goods and Stuff")
   max_com_id = db.last_company_id()
   db.create_employee(max_com_id, 'Romelu', 'Lukaku', 'Beast',
                      'email@gmail.com', '123456789', True)
   db_list =  db.get_employee_list(max_com_id)
   api_list = api.get_employee_list(max_com_id)
   assert len(db_list) == len(api_list)
   api_employee = (api.get_employee_list(max_com_id))[0]
   employee_id = api_employee['id']
   db.delete_employee(employee_id)
   db.delete_company(max_com_id)

def test_create_employee():
   db.create_company("Sber", "Banking Service")
   max_com_id = db.last_company_id()
   db.create_employee(max_com_id, "German", "Gref", "Beast",
                      "email@gmail.com", "123456789", True)
   api_employee = (api.get_employee_list(max_com_id))[0]
   employee_id = api_employee['id']
   assert api_employee is not None
   assert api_employee['firstName'] == "German"
   assert api_employee['lastName'] == "Gref"
   assert api_employee['email'] == "email@gmail.com"
   assert api_employee['companyId'] == max_com_id
   db.delete_employee(employee_id)
   db.delete_company(max_com_id)

def test_get_employee_by_id():
   db.create_company("Sber", "Banking Service")
   max_com_id = db.last_company_id()
   db.create_employee(max_com_id, "German", "Gref", "Beast",
                      "email@gmail.com", "123456789", True)
   employee_id = db.last_employee_id(max_com_id)
   employee_result = api.get_employee_by_id(employee_id)
   assert employee_result['firstName'] == 'German'
   assert employee_result['email'] ==  "email@gmail.com"
   assert employee_result['isActive'] == True
   assert employee_result['middleName'] == "Beast"
   db.delete_employee(employee_id)
   db.delete_company(max_com_id)

def test_update_employee_info():
   db.create_company("Sber", "Banking Service")
   max_com_id = db.last_company_id()
   db.create_employee(max_com_id, "German", "Gref", "Beast",
                      "email@gmail.com", "123456789", True)
   employee_id = db.last_employee_id(max_com_id)
   db.update_employee("Oskar", employee_id)
   result = (api.get_employee_list(max_com_id))[0]
   assert result['lastName'] == "Oskar"
   db.delete_employee(employee_id)
   db.delete_company(max_com_id)