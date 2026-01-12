class Employee:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def get_info(self):
        return f"Сотрудник: {self.__name}, ID: {self.__id}"

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id


class Manager:
    def __init__(self, department):
        self.__department = department
        self.__managed_projects = []

    def manage_project(self, project_name):
        self.__managed_projects.append(project_name)
        return f"Менеджер управляет проектом: {project_name}"

    def get_department(self):
        return self.__department

    def get_projects(self):
        return self.__managed_projects


class Technician:
    def __init__(self, specialization):
        self.__specialization = specialization
        self.__maintenance_tasks = []

    def perform_maintenance(self, task):
        self.__maintenance_tasks.append(task)
        return f"Выполнено техническое обслуживание: {task}"

    def get_specialization(self):
        return self.__specialization

    def get_tasks(self):
        return self.__maintenance_tasks


class TechManager(Employee, Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Employee.__init__(self, name, id)
        Manager.__init__(self, department)
        Technician.__init__(self, specialization)
        self.__subordinates = []

    def add_employee(self, employee):
        self.__subordinates.append(employee)
        return f"Сотрудник {employee.get_name()} добавлен в команду"

    def get_team_info(self):
        if not self.__subordinates:
            return "В команде нет сотрудников"

        team_info = f"Команда менеджера {self.get_name()}:\n"
        for i, emp in enumerate(self.__subordinates, 1):
            team_info += f"{i}. {emp.get_info()}\n"
        return team_info

    def get_info(self):
        base_info = Employee.get_info(self)
        return f"{base_info}, Отдел: {self.get_department()}, Специализация: {self.get_specialization()}"

    def manage_project(self, project_name):
        result = Manager.manage_project(self, project_name)
        return f"Технический менеджер {self.get_name()} - {result}"

    def perform_maintenance(self, task):
        result = Technician.perform_maintenance(self, task)
        return f"Технический менеджер {self.get_name()} - {result}"


print("=== Демонстрация системы управления сотрудниками ===\n")

emp1 = Employee("Иван Петров", "EMP001")
print("Сотрудник:")
print(emp1.get_info())
print()

mgr = Manager("IT-отдел")
print("Менеджер:")
print(mgr.manage_project("Разработка новой системы"))
print(f"Отдел: {mgr.get_department()}")
print()

tech = Technician("Сетевое оборудование")
print("Техник:")
print(tech.perform_maintenance("Настройка маршрутизаторов"))
print(f"Специализация: {tech.get_specialization()}")
print()

tech_mgr = TechManager("Анна Сидорова", "TM001", "Технический отдел", "Системный администратор")
print("Технический менеджер:")
print(tech_mgr.get_info())
print(tech_mgr.manage_project("Миграция на новую платформу"))
print(tech_mgr.perform_maintenance("Обновление серверов"))
print()

emp2 = Employee("Мария Иванова", "EMP002")
emp3 = Employee("Алексей Смирнов", "EMP003")

print("Управление командой:")
print(tech_mgr.add_employee(emp1))
print(tech_mgr.add_employee(emp2))
print(tech_mgr.add_employee(emp3))
print()

print("Информация о команде:")
print(tech_mgr.get_team_info())
print()

print("Демонстрация полиморфизма:")
employees = [emp1, tech_mgr]

for emp in employees:
    print(emp.get_info())
print()

print("Проекты и задачи технического менеджера:")
tech_mgr.manage_project("Внедрение системы мониторинга")
tech_mgr.perform_maintenance("Резервное копирование данных")

print(f"Проекты: {tech_mgr.get_projects()}")
print(f"Технические задачи: {tech_mgr.get_tasks()}")