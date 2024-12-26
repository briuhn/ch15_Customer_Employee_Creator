class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def full_name(self):
        return self.first_name + " " + self.last_name

class Customer(Person):
    def __init__(self, first_name, last_name, email, phone_number):
        Person.__init__(self, first_name, last_name, email)
        self.phone_number = phone_number

class Employee(Person):
    def __init__(self, first_name, last_name, email, ssn):
        Person.__init__(self, first_name, last_name, email)
        self.ssn = ssn
