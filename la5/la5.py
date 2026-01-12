class book:
    def __init__(self,title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}'
a = book('Колобок', 'Народная','0000')
print(a.get_info())

class circle:
    def __init__(self, radius=2):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, radius):
        self.radius = radius
Circle = circle()
Circle.set_radius(7)
print(Circle.get_radius())
