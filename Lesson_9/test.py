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
   db.create_employee(max_com_id, "Romelu", "Lukaku", "Beast",
                      "email@gmail.com", "123456789", True)
   db_list =  db.get_employee_list(max_com_id)
   api_list = api.get_employee_list()
   assert len(db_list) == len(api_list)
   api_employee = api.get_employee_list()
   employee_id = api_employee['id']
   db.delete_employee(employee_id)
   db.delete_company(max_com_id)

def test_create_employee():
   db.create_company("Sber", "Banking Service")
   max_com_id = db.last_company_id()
   db.create_employee(max_com_id, "German", "Gref", "Beast",
                      "email@gmail.com", "123456789", True)
   api_employee = api.get_employee_list()
   employee_id = api_employee['id']
   assert  api_employee is not None
   assert  api_employee['firstName'] == "German"
   assert  api_employee['lastName'] == "Gref"
   assert  api_employee['email'] == "email@gmail.com"
   db.delete_employee(employee_id)
   db.delete_company(max_com_id)