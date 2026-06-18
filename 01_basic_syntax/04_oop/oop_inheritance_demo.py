"""面向对象编程示例

本文件演示 Python 面向对象编程的核心概念：
- 类（Class）：对象的蓝图/模板
- 对象（Object）：类的实例
- 继承（Inheritance）：子类继承父类的属性和方法
- 方法重写（Override）：子类可以重写父类的方法
- self：代表对象本身
- __init__：构造函数，创建对象时自动调用
- __str__：字符串方法，print() 时自动调用
"""


# ==================== 定义父类：Animal ====================
class Animal:
    """动物基类：所有动物的父类"""

    # __init__：构造函数，创建对象时自动调用
    # self：代表正在创建的这个对象本身
    def __init__(self, name, sound):
        # 将参数赋值给对象的属性（类似贴标签）
        self.name = name      # 动物的名字
        self.sound = sound    # 动物的叫声

    # 定义一个实例方法：让动物发出叫声
    def make_sound(self):
        print(f"{self.name} 发出声音: {self.sound}")

    # __str__：特殊方法，print(对象) 时自动调用
    # 必须返回字符串
    def __str__(self):
        return f"<动物: {self.name}>"


# ==================== 定义子类：Dog（继承自 Animal）====================
class Dog(Animal):
    """狗类：继承自动物类"""

    # 子类的 __init__：需要调用父类的构造函数初始化通用属性
    def __init__(self, name, breed):
        # super().__init__()：调用父类的构造函数
        # "汪汪" 是固定值，因为狗的叫声都是汪汪
        super().__init__(name, "汪汪")
        # 狗独有的属性：品种
        self.breed = breed

    # 方法重写（Override）：子类重新定义父类的方法
    # 子类的方法名与父类相同时，会覆盖父类的方法
    def make_sound(self):
        print(f"{self.name} ({self.breed}) 叫道: {self.sound}!")

    # 子类独有方法：父类没有的方法
    def fetch(self):
        """让狗接飞盘"""
        print(f"{self.name} 正在接飞盘!")


# ==================== 程序入口 ====================
# 只有直接运行这个文件时才会执行下面的代码
# 如果被其他文件 import，下面的代码不会执行
if __name__ == "__main__":
    # 创建 Dog 对象：Dog("名字", "品种")
    dog = Dog("旺财", "金毛")

    # 调用对象的方法
    dog.make_sound()    # 输出：旺财 (金毛) 叫道: 汪汪!
    dog.fetch()         # 输出：旺财 正在接飞盘!

    # print() 调用 __str__ 方法
    print(dog)          # 输出：<动物: 旺财>
