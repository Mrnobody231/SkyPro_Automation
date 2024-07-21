class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def my_name(self):
        return self.name
    
    def my_surname(self):
        return self.surname
    
    def full_name(self):
        return self.name + " " + self.surname
