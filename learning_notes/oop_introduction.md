# Python 面向对象编程（OOP）入门指南

> 通过 `oop_inheritance_demo.py` 示例，从小白角度理解 OOP 核心概念。

---

## 一、先明白「面向对象」到底是什么

想象你在玩一个「宠物养成游戏」。游戏里有很多动物：狗、猫、鸟……

### 不用 OOP 的写法（过程式）

```python
# 每条狗，你都得手写一堆变量
dog1_name = "旺财"
dog1_sound = "汪汪"
dog1_breed = "金毛"

def dog1_speak():
    print(f"{dog1_name} 发出声音: {dog1_sound}")
```

**问题**：每多一只狗，就要复制粘贴一遍。代码又乱又难维护。

### 用 OOP 的写法

先画一个「蓝图（模板）」，告诉电脑「动物长什么样」，然后用这个蓝图快速「造」出无数只动物！

这就是 OOP 的核心思想——**用「模板（类）」批量生产「对象」**。

---

## 二、认识代码中的核心概念

| 术语 | 大白话翻译 | 对应代码 |
|------|-----------|---------|
| **类（Class）** | 一张「设计蓝图/模板」 | `class Animal:` |
| **对象（Object）** | 用蓝图造出来的「实物」 | `dog = Dog(...)` |
| **属性（Attribute）** | 对象的「特征/数据」 | `self.name = name` |
| **方法（Method）** | 对象「会做的动作」 | `def make_sound(self):` |
| **继承（Inheritance）** | 儿子遗传爸爸的能力 | `class Dog(Animal):` |

---

## 三、逐行拆解代码

### 3.1 定义「动物」这个蓝图（基类）

```python
class Animal:
    """动物基类"""

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} 发出声音: {self.sound}")

    def __str__(self):
        return f"<动物: {self.name}>"
```

#### 1. `class Animal:` — 创建一个类

- `class` 是 Python 的关键字，意思是「我要定义一个新的模板了」
- `Animal` 是模板的名字（首字母大写，这是约定俗成的规范）

#### 2. `def __init__(self, name, sound):` — 构造函数

这是最让初学者困惑的地方，但其实很简单：

- `__init__` 是 **两个下划线 + init + 两个下划线**，意思是「initialize（初始化）」
- 它就像一个「启动开关」：每当你用这个模板造一个新对象时，Python 会**自动调用**它
- 参数 `name` 和 `sound` 就是造对象时要告诉 Python 的信息
- **`self` 是什么？** → `self` 就像「我自己」，代表即将被创建的那个对象

**生活化类比**：

想象你去奶茶店点奶茶 🍵：

```
你说："来一杯珍珠奶茶！"          → Dog("旺财", "金毛")
店员启动制作流程                   → Python 自动调用 __init__
店员贴上标签：「奶茶名字=珍珠」     → self.name = "旺财" 
制作完成，递给你                   → 返回一个对象
```

#### 3. `self.name = name` — 保存属性

```python
self.name = name      # 把传入的 name，存到这个对象身上
```

意思是：**"把 `name` 这个值，贴到 `self`（我自己）身上，以后叫 `self.name` 就能拿到它"**。

你可以把它想象成在一只玩具熊的胸口贴上「姓名标签」。🧸

#### 4. `def make_sound(self):` — 定义方法

这就是这个类会做的「动作」。注意第一个参数必须是 `self`——因为它要通过 `self` 来访问自己身上的属性（如 `self.name`、`self.sound`）。

#### 5. `def __str__(self):` — 「魔法方法」

这也是 Python 的一个特殊约定。当你执行 `print(dog)` 时，Python 会**自动调用**这个方法，用它返回的字符串来显示对象。

没有这个方法的话，`print(dog)` 只会显示一个难看的内存地址，比如 `<__main__.Animal object at 0x123456>`。

---

### 3.2 定义「狗」，让它继承自动物（子类）

```python
class Dog(Animal):
    """狗类，继承自动物类"""

    def __init__(self, name, breed):
        super().__init__(name, "汪汪")
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} ({self.breed}) 叫道: {self.sound}!")

    def fetch(self):
        print(f"{self.name} 正在接飞盘!")
```

#### 1. `class Dog(Animal):` — 继承

括号里写 `Animal`，意思是：**"Dog 是 Animal 的儿子，它自动拥有 Animal 的一切能力。"**

- `Animal` 叫做 **父类 / 基类**（爸爸）
- `Dog` 叫做 **子类 / 派生类**（儿子）

儿子天生就会爸爸会的一切，比如 `Dog` 自动就拥有 `make_sound` 方法和 `name`、`sound` 属性，不用重新写一遍！

#### 2. `super().__init__(name, "汪汪")` — 叫爸爸帮忙

`super()` 的意思是「调用爸爸（父类）」。这里的逻辑是：

> "爸爸，我知道你已经有一套初始化流程了，你先帮我设置好 `name` 和 `sound`，`sound` 我帮你填死成 '汪汪'，然后我自己再加个 `breed`（品种）属性。"

这就是 OOP 的魅力：**复用 + 扩展**。

#### 3. 子类中再次定义 `make_sound` — 方法重写（Override）

儿子觉得爸爸的 `make_sound` 不够酷，就自己写了一个新版本。  
以后调用 `dog.make_sound()`，会用儿子（Dog）自己的版本，而不是爸爸的。

这叫做「**方法重写**」或「**多态**」——同一个方法名，不同的对象有不同的表现。

#### 4. `def fetch(self):` — 子类扩展新能力

爸爸（Animal）不会接飞盘，但儿子（Dog）会！  
子类可以自由添加父类没有的新能力。

---

### 3.3 真正「造」一个对象出来用

```python
if __name__ == "__main__":
    dog = Dog("旺财", "金毛")
    dog.make_sound()
    dog.fetch()
    print(dog)
```

#### `if __name__ == "__main__":` 是什么？

这是 Python 的惯例：**"只有当这个文件被直接运行时，才执行下面的代码。"**  
如果这个文件被别的文件 `import` 了，下面的代码就不会执行。

简单说：它就像你在文件末尾写的「**测试区**」。

#### 运行时发生了什么？

让我们跟着代码一步步走：

```python
dog = Dog("旺财", "金毛")
```

执行流程：

```
调用 Dog("旺财", "金毛")
       ↓
进入 Dog 的 __init__(self="旺财", breed="金毛")  ← self 此时就是正在创建的那只狗
       ↓
super().__init__("旺财", "汪汪")          ← 调用爸爸 Animal 的构造函数
       ↓  ↳ 在这个对象身上贴上：self.name = "旺财"
       ↓  ↳ 在这个对象身上贴上：self.sound = "汪汪"
       ↓
self.breed = "金毛"                      ← 狗自己的属性
       ↓
对象创建完成，返回给变量 dog 🐕
```

现在 `dog` 这个对象身上，带着 3 个属性：

```
dog.name   = "旺财"
dog.sound  = "汪汪"
dog.breed  = "金毛"
```

接下来执行方法：

```python
dog.make_sound()    # 旺财 (金毛) 叫道: 汪汪!
#                    ↑ 调用 Dog 自己的 make_sound（因为子类重写了父类的版本）

dog.fetch()         # 旺财 正在接飞盘!
#                    ↑ 调用 Dog 新增的方法

print(dog)          # <动物: 旺财>
#                    ↑ 自动调用 __str__ 方法（爸爸的，儿子没重写）
```

---

## 四、运行代码，亲眼看看

```bash
python3 /workspace/01_basic_syntax/04_oop/oop_inheritance_demo.py
```

输出：

```
旺财 (金毛) 叫道: 汪汪!
旺财 正在接飞盘!
<动物: 旺财>
```

---

## 五、你已经掌握的知识清单

到这里，你已经理解了 OOP 的 **四大核心概念**：

| 概念 | 含义 | 在本代码中的体现 |
|------|------|-----------------|
| **封装** | 把数据（属性）和操作数据的函数（方法）打包在一起 | `Animal` 类把 `name`、`sound` 和 `make_sound()` 包在一起 |
| **继承** | 子类复用父类的属性和方法，不用重复写代码 | `Dog` 继承 `Animal`，自动拥有了 `name`、`sound` |
| **多态** | 同一个方法名，不同的子类表现不同 | `Dog` 重写了 `make_sound()`，叫声不一样 |
| **抽象** | 隐藏复杂的内部实现，只暴露简单的接口 | 你只需要 `dog.make_sound()`，不用管里面怎么打印 |

---

## 六、动手练习（检验你是否真的懂了）

**题目**：创建一只猫，它继承自动物，发出「喵喵」的声音，并且有一个新方法 `scratch()` 表示猫会抓人。

**参考答案**：

```python
class Cat(Animal):
    """猫类，继承自动物类"""

    def __init__(self, name, color):
        super().__init__(name, "喵喵")    # 猫的叫声固定为"喵喵"
        self.color = color                 # 猫自己的属性：毛色

    def make_sound(self):
        print(f"{self.name} ({self.color}) 喵道: {self.sound}!")

    def scratch(self):
        print(f"{self.name} 正在抓沙发!")


# 测试
cat = Cat("咪咪", "橘色")
cat.make_sound()    # 咪咪 (橘色) 喵道: 喵喵!
cat.scratch()       # 咪咪 正在抓沙发!
print(cat)          # <动物: 咪咪>
```

如果你能看懂这个答案，说明你已经掌握了 Python 面向对象编程的入门知识！🎉

---

## 七、记住这几条「铁律」，以后看任何 OOP 代码都不怕

1. **看到 `class` 就想「蓝图/模板」**，看到 `变量 = 类名()` 就想「造东西」
2. **看到 `__init__` 就想「初始化流程」**，造新对象时自动调用
3. **看到 `self` 就想「我自己」**，指当前这个对象
4. **看到 `class 儿子(爸爸):` 就想「继承」**，儿子天生拥有爸爸的一切
5. **看到 `super()` 就想「叫爸爸帮忙」**，复用父类已写好的代码
6. **父子有同名方法时，用儿子的版本**（这就是方法重写 / 多态）

掌握这些，你就可以开始阅读和编写更复杂的面向对象代码了！🚀

---

## 八、参考文件

- [oop_inheritance_demo.py](file:///workspace/01_basic_syntax/04_oop/oop_inheritance_demo.py) - 示例代码
