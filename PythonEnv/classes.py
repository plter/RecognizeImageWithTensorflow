class Student:
    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


s = Student("小云", 20)
print(s.get_name())
