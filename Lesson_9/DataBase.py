from sqlalchemy import create_engine, text, inspect


class DataBase:
    def __init__(self, engine):
        self.engine = create_engine(engine)

    scripts = {
        'create_company': text('INSERT INTO company (name, description) VALUES (:name, :description)'),
        'max_company_id': text('SELECT MAX(id) FROM company'),
        'delete_company': text('DELETE FROM company WHERE id = :company_id'),
        'get_employee_list': text('SELECT * FROM company WHERE company_id = :id'),
        'create_employee': text('INSERT INTO employee (first_name, last_name,'
                                ' middle_name, email, phone, is_active) VALUES '
                                '(:first_name, :last_name, :middle_name, :email, :phone, :is_active'),
        'max_employee_id': text('SELECT MAX(id) FROM employee'),
        'get_employee_by_id': text('SELECT * FROM employee WHERE id = :employee_id'),
        'change_employee': text('UPDATE employee SET last_name = :last_name WHERE id = :employee_id'),
        'delete_employee': text('DELETE FROM employee WHERE id = :employee_id')
    }

    def db_table_names(self):
        inspector = inspect(self.engine)
        return inspector.get_table_names()

    def execute_query(self, query_key, parameter=None):
        with self.engine.connect() as connection:
            result = connection.execute(self.scripts[query_key], parameter)
            connection.commit()
            return result

    def create_company(self, company_name, company_descr):
        return self.execute_query('create_company',
                                  {'name' : company_name, 'description' : company_descr})

    def last_company_id(self):
        row =  self.execute_query('max_company_id').fetchone()
        return row[0]

    def delete_company(self, company_id):
        return self.execute_query('delete_company', {'id': company_id})

    def get_employee_list(self, company_id):
        return self.execute_query('get_employee_list', {'company_id' : company_id})

    def create_employee(self, company_id: str, first_name: str, last_name: str, middle_name: str,
                        email: str, phone: str, is_active: bool):
        rows = self.execute_query('create_employee', {'company_id' : company_id,
                                        'first_name' : first_name, 'last_name' : last_name, 'middle_name' : middle_name,
                                            'email' : email, 'phone' : phone, 'is_active' : is_active})
        return rows.fetchall()

    def last_employee_id(self):
        row =  self.execute_query('max_employee_id').fetchone()
        return row[0]

    def get_employee_by_id(self, employee_id):
        return self.execute_query('get_employee_by_id', {'id' : employee_id})

    def update_employee(self, last_name, employee_id):
        return self.execute_query('change_employee', {'last_name' : last_name, 'id' : employee_id})

    def delete_employee(self, employee_id):
        return self.execute_query('delete_employee', {'id': employee_id})