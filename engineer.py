from employee import Employee

class Engineer(Employee):
  def __init__(self, name, salary, projects_count):
    super().__init__(name, salary)
    self.projects_count = projects_count

  def raise_salary(self):
    self.salary += 4.8 * self.projects_count