class Employee:
    def __init__(self,name,role,salary,DoB):
        self.name=name
        self.role=role
        self.salary=salary
        self.DoB=DoB
    def increase_salary(self):
        self.salary=self.salary*1.1

    def calculate_age(self):
        year=int(self.DoB[6:10])
        age=2024-year
        return age





#00/00/0000
#dd/mm/yyyy



class Manager:
    def __init__(self,name,role,salary,DoB,bonus):
        self.name=name
        self.role=role
        self.salary=salary
        self.DoB=DoB
        self.bonus=bonus

    def increase_salary(self):
        self.salary=self.salary*1.2

    def calculate_age(self):
        year=int(self.DoB[6:10])
        age=2024-year
        return age

    def increase_bonus(self):
        self.bonus=self.bonus*1.05
