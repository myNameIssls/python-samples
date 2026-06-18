"""面向对象编程示例"""


class Animal:
    """动物基类"""

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} 发出声音: {self.sound}")

    def __str__(self):
        return f"<动物: {self.name}>"


class Dog(Animal):
    """狗类，继承自动物类"""

    def __init__(self, name, breed):
        super().__init__(name, "汪汪")
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} ({self.breed}) 叫道: {self.sound}!")

    def fetch(self):
        print(f"{self.name} 正在接飞盘!")


if __name__ == "__main__":
    dog = Dog("旺财", "金毛")
    dog.make_sound()
    dog.fetch()
    print(dog)
