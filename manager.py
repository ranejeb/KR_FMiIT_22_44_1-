from employee import Employee

class Manager(Employee):
  def __init__(self, name, salary, sales_volume):
    super().__init__(name, salary)
    self.sales_volume = sales_volume

  def raise_salary(self, minimal_sales_volume):
    if self.sales_volume > minimal_sales_volume:
      self.salary += minimal_sales_volume * 0.01
    