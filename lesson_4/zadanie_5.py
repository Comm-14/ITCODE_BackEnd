class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_paid(self):
        pass

class Manager(Employee):
    def get_paid(self):
        return self.salary + 7500
    def __str__(self):
        return f"Manager: {self.name}, Salary: {self.salary}"


class Worker(Employee):
    def get_paid(self):
        return self.salary
    def __str__(self):
        return f"Worker: {self.name}, Salary: {self.salary}"


manager = Manager("Jane Smith", 70000)
worker = Worker("Bob Johnson", 40000)

print(manager)
print(worker)

print(f"Manager's salary: {manager.get_paid()}")
print(f"Worker's salary: {worker.get_paid()}")