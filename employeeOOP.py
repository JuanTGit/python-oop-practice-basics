class Employee:
    employee_raise = 1.05

    def __init__(self, firstName, lastName, jobTitle, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.jobTitle = jobTitle
        self.salary = salary
        self.email = (firstName + '.' + lastName + '@company.com').lower()

    def applyRaise(self):
        temp = self.salary
        self.salary = (self.salary * self.employee_raise)
        print(f"{self.firstName.title()}'s salary now at {self.salary}, original {temp}.")

class Sales(Employee):
    def __init__(self, firstName, lastName, jobTitle, salary, phonenumber):
        super().__init__(firstName, lastName, jobTitle, salary)
        self.phonenumber = phonenumber

    def followUp(self, customerName):
        print(f"Dear {customerName}, Thank you for your interest in our product. Please let me know if you have any questions. My email is {self.email} or my phone number is {self.phonenumber}. Thanks, {(self.firstName + ' ' + self.lastName).title()}")

class Development(Employee):
    def __init__(self, firstName, lastName, jobTitle, salary):
        super().__init__(firstName, lastName, jobTitle, salary)
    
    def code(self):
        print(f'{(self.firstName + ' ' + self.lastName).title()} is writing code.')


salesEmp1 = Sales('James', 'Doren', 'Sales Employee', 50000, '(832)555-5555')
salesEmp1.followUp("Mike O'Neil")
salesEmp1.applyRaise()

devEmp1 = Development('Juan', 'Tejeda', 'Developer', 100000)
devEmp1.code()
devEmp1.applyRaise()