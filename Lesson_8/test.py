from constants import X_CLIENTS_URL, AUTHORIZATION
from Employee import Employee

employee = Employee(X_CLIENTS_URL)


def test_authorization_token():
    token = employee.authorization(AUTHORIZATION)
    assert token is not None

def test_company_id():
   company = employee.get_company_id()
   assert  company is not None

def test_get_employee_list():
    res_employee = employee.get_employee_list()
    assert res_employee is not None

def test_create_new_employee():
    res_employee = employee.add_employee("New Company", "Company", "Com",
                                         "email@gmail.com","123456789", True)
    assert res_employee is not None

def test_get_employee():
    response = employee.get_employee_by_id()
    assert response is not None
    assert response["lastName"] == "Company"

def test_change_employee():
     response = employee.change_employee("New Last Name", "new.email@gmail.com", True)
     assert response is not None
     assert response["email"] == "new.email@gmail.com"