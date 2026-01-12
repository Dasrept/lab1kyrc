class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password


user = UserAccount("hunterx666", "grigorii@mail.com", "12345")

print(user.check_password("12345"))
user.set_password("new_pass")
print(user.check_password("12345"))
print(user.check_password("new_pass"))


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}, Вид топлива: {self.fuel_type}"


car = Car("Dodge", "Ram TRX", "Бензин(Недстаточно)")
print(car.get_info())