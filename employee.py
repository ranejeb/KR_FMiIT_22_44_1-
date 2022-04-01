class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def raise_salary(self, coefficient):
    self.salary *= coefficient

    