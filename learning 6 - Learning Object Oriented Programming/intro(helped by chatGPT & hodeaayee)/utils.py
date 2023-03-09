class Person:
    def __init__(self, first_name, last_name, ID, address, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.address = address
        self.dob = dob


class Student(Person):
    def __init__(self, first_name, last_name, ID, address, dob, student_id):
        Person.__init__(self, first_name, last_name, ID, address, dob)
        self.student_id = student_id
