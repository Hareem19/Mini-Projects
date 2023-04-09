class emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def getSalary(self):
        print(self.salary)
emp1=emp("fdfg","232")
print(emp1.salary)
print(emp1.name)
emp2=emp("waji","35000")
print(emp2.salary)
print(emp2.name)
emp2.getSalary()