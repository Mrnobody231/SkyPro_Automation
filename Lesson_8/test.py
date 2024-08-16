from constants import X_CLIENTS_URL, AUTHORIZATION
from Employee import Employee

employee = Employee(X_CLIENTS_URL)


def test_authorization_token():
    token = employee.authorization(AUTHORIZATION)
    assert token is not None

def test():
    pass