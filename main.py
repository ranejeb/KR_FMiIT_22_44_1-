from employee import Employee
from manager import Manager
from engineer import Engineer

maria = Employee("Мария", 1000)
petr = Engineer("Пётр", 1000, 5)
joseph = Manager("Иосиф", 1000, 1500.6)

print("Сотрудник:")
print("Имя: ", maria.name)
print("Заработная плата: ", maria.salary)
maria.raise_salary(1.2)
print("Заработная сотрудника плата после повышения с коэффициентом 1.2: ", maria.salary)
print("\n")

print("Инженер:")
print("Имя: ", petr.name)
print("Заработная плата: ", petr.salary)
print("Разработано проектов: ", petr.projects_count)
petr.raise_salary()
print("Заработная плата инженера после пересмотра: ", petr.salary)
print("\n")

print("Менеджер:")
print("Имя: ", joseph.name)
print("Заработная плата: ", joseph.salary)
print("Объем продаж: ", joseph.sales_volume, "т.")
joseph.raise_salary(1700)
print("Заработная плата менеджера после пересмотра с минимальным объемом продаж 1700 т.: ", joseph.salary)
joseph.raise_salary(1200)
print("Заработная плата менеджера после пересмотра с минимальным объемом продаж 1200 т.: ", joseph.salary)
print("\n")