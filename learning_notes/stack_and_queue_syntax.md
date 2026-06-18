# 栈与队列示例 — 核心语法详解

> 通过 `stack_and_queue_demo.py` 理解 Python 类定义、方法、列表操作等核心语法。

---

## 一、文件概览

本文件实现了两种经典数据结构：

| 数据结构 | 特点 | 操作方法 |
|---------|------|---------|
| **栈（Stack）** | 后进先出（LIFO） | `push()`、`pop()`、`peek()`、`is_empty()` |
| **队列（Queue）** | 先进先出（FIFO） | `enqueue()`、`dequeue()`、`is_empty()` |

---

## 二、核心语法详解

### 2.1 类定义

```python
class Stack:
    """栈类"""
```

**语法要点**：

- `class` 关键字：用于定义一个类（蓝图/模板）
- 类名首字母大写：这是 Python 的命名规范（PascalCase）
- 类体缩进：类内的所有代码必须缩进（通常用 4 个空格）

---

### 2.2 构造函数 `__init__`

```python
def __init__(self):
    self.items = []
```

**语法要点**：

| 元素 | 说明 |
|------|------|
| `__init__` | 双下划线包围的特殊方法，称为「构造函数」或「初始化方法」 |
| `self` | 必须作为第一个参数，代表当前对象本身 |
| `self.items = []` | 创建一个空列表，并将其绑定为对象的属性 |

**执行时机**：

```python
stack = Stack()    # 创建对象时，Python 自动调用 __init__
```

**为什么不需要提前声明 `items`？**

Python 是动态语言，属性的声明和赋值合二为一。`self.items = []` 这句话同时完成了：
1. 创建一个空列表
2. 将这个列表作为属性绑定到对象上

---

### 2.3 实例方法（需要 `self` 参数）

```python
def push(self, item):
    self.items.append(item)
```

**语法要点**：

| 元素 | 说明 |
|------|------|
| `def push(self, item):` | 定义一个方法，第一个参数必须是 `self` |
| `self.items.append(item)` | 通过 `self` 访问对象的属性，并调用列表方法 |

**为什么 `self` 必须作为参数？**

当你调用 `stack.push(1)` 时，Python 内部会自动转换成：

```python
Stack.push(stack, 1)    # self 就是 stack 对象
```

**如果省略 `self` 会怎样？**

```python
def push(item):    # ❌ 错误
    self.items.append(item)    # ❌ NameError: name 'self' is not defined
```

---

### 2.4 条件判断

```python
def pop(self):
    if not self.is_empty():
        return self.items.pop()
    raise IndexError("栈为空")
```

**语法要点**：

| 元素 | 说明 |
|------|------|
| `if not self.is_empty():` | 判断栈是否不为空 |
| `not` | 逻辑非运算符，取反 |
| `self.is_empty()` | 调用对象的另一个方法 |

**执行流程**：

```
调用 stack.pop()
       ↓
检查 stack.is_empty() 返回 True 还是 False
       ↓
如果不为空 → 返回 self.items.pop()
如果为空 → 抛出异常
```

---

### 2.5 异常抛出 `raise`

```python
raise IndexError("栈为空")
```

**语法要点**：

| 元素 | 说明 |
|------|------|
| `raise` | 关键字，用于主动抛出异常 |
| `IndexError` | 异常类型，表示索引错误 |
| `"栈为空"` | 异常消息，描述错误原因 |

**作用**：

当用户试图从空栈中弹出元素时，程序不会默默失败，而是明确告诉用户"栈为空"，方便调试和错误处理。

**不抛异常的后果**：

```python
def pop(self):
    return self.items.pop()    # 如果列表为空，会自动抛出 IndexError: pop from empty list
```

虽然列表的 `pop()` 方法会自动抛异常，但自定义异常消息更友好、更清晰。

---

### 2.6 列表操作

#### 2.6.1 `append()` — 在末尾添加元素

```python
def push(self, item):
    self.items.append(item)    # 在列表末尾添加元素
```

**效果**：

```
初始: []
push("A") → ["A"]
push("B") → ["A", "B"]
push("C") → ["A", "B", "C"]
```

#### 2.6.2 `pop()` — 删除并返回末尾元素

```python
def pop(self):
    return self.items.pop()    # 删除并返回最后一个元素
```

**效果**：

```
初始: ["A", "B", "C"]
pop() → 返回 "C"，列表变为 ["A", "B"]
pop() → 返回 "B"，列表变为 ["A"]
pop() → 返回 "A"，列表变为 []
```

#### 2.6.3 `pop(0)` — 删除并返回第一个元素

```python
def dequeue(self):
    return self.items.pop(0)    # 删除并返回第一个元素
```

**效果**：

```
初始: ["1号", "2号", "3号"]
dequeue() → 返回 "1号"，列表变为 ["2号", "3号"]
dequeue() → 返回 "2号"，列表变为 ["3号"]
dequeue() → 返回 "3号"，列表变为 []
```

#### 2.6.4 `len()` — 获取列表长度

```python
def is_empty(self):
    return len(self.items) == 0    # 判断列表是否为空
```

**效果**：

```python
len([]) == 0    # True，空列表
len([1, 2]) == 0    # False，非空列表
```

#### 2.6.5 负索引 `self.items[-1]` — 获取最后一个元素

```python
def peek(self):
    return self.items[-1]    # 返回最后一个元素，但不删除
```

**效果**：

```python
["A", "B", "C"][-1]    # "C"
["A", "B", "C"][-2]    # "B"
["A", "B", "C"][-3]    # "A"
```

---

### 2.7 程序入口 `if __name__ == "__main__"`

```python
if __name__ == "__main__":
    stack = Stack()
    for item in ["A", "B", "C"]:
        stack.push(item)
    print("栈弹出顺序:", stack.pop(), stack.pop(), stack.pop())
```

**语法要点**：

| 元素 | 说明 |
|------|------|
| `__name__` | 特殊变量，Python 自动设置 |
| `"__main__"` | 当文件被直接运行时，`__name__` 的值 |

**两种运行方式**：

```
方式一：直接运行文件
  python3 stack_and_queue_demo.py
  → __name__ == "__main__"
  → 执行 if 块内的测试代码

方式二：被其他文件 import
  from stack_and_queue import Stack
  → __name__ == "stack_and_queue"
  → 跳过 if 块，只提供类供其他模块使用
```

---

### 2.8 for 循环遍历

```python
for item in ["A", "B", "C"]:
    stack.push(item)
```

**语法要点**：

| 元素 | 说明 |
|------|------|
| `for item in 可迭代对象:` | 遍历可迭代对象（列表、字符串、元组等） |
| `item` | 每次循环时，代表当前元素 |

**执行流程**：

```
第一次循环: item = "A" → stack.push("A")
第二次循环: item = "B" → stack.push("B")
第三次循环: item = "C" → stack.push("C")
```

---

## 三、栈与队列的核心区别

### 3.1 栈（Stack）— 后进先出（LIFO）

```
                    栈顶
                     ↓
push("A") → ["A"]
push("B") → ["A", "B"]
push("C") → ["A", "B", "C"]
pop()     → ["A", "B"]      返回 "C"
pop()     → ["A"]           返回 "B"
pop()     → []              返回 "A"
```

**生活类比**：堆叠的盘子，只能从最上面拿。

### 3.2 队列（Queue）— 先进先出（FIFO）

```
队头 ←                    ← 队尾
     ↓
enqueue("1号") → ["1号"]
enqueue("2号") → ["1号", "2号"]
enqueue("3号") → ["1号", "2号", "3号"]
dequeue()      → ["2号", "3号"]        返回 "1号"
dequeue()      → ["3号"]               返回 "2号"
dequeue()      → []                    返回 "3号"
```

**生活类比**：排队买奶茶，先来的先买。

---

## 四、运行结果

```bash
python3 /workspace/02_data_structures/02_stack_queue/stack_and_queue_demo.py
```

输出：

```
栈弹出顺序: C B A
队列出队顺序: 1号 2号 3号
```

**分析**：

- 栈：先进后出，所以弹出顺序是 `C B A`（与入栈顺序相反）
- 队列：先进先出，所以出队顺序是 `1号 2号 3号`（与入队顺序相同）

---

## 五、关键语法速查表

| 语法 | 用途 | 示例 |
|------|------|------|
| `class 类名:` | 定义类 | `class Stack:` |
| `__init__(self)` | 构造函数 | `def __init__(self):` |
| `self.属性 = 值` | 设置对象属性 | `self.items = []` |
| `def 方法名(self, 参数):` | 定义实例方法 | `def push(self, item):` |
| `if not 条件:` | 条件判断（取反） | `if not self.is_empty():` |
| `raise 异常类型(消息)` | 抛出异常 | `raise IndexError("栈为空")` |
| `list.append(item)` | 在末尾添加元素 | `self.items.append(item)` |
| `list.pop()` | 删除并返回末尾元素 | `self.items.pop()` |
| `list.pop(0)` | 删除并返回第一个元素 | `self.items.pop(0)` |
| `len(list)` | 获取列表长度 | `len(self.items)` |
| `list[-1]` | 获取最后一个元素 | `self.items[-1]` |
| `if __name__ == "__main__":` | 程序入口 | 测试代码放在这里 |
| `for item in 列表:` | 遍历列表 | `for item in ["A", "B", "C"]:` |

---

## 六、常见错误及解决方法

### 错误 1：方法忘记写 `self` 参数

```python
def push(item):    # ❌
    self.items.append(item)    # NameError
```

**解决**：在方法参数中添加 `self`：

```python
def push(self, item):    # ✅
    self.items.append(item)
```

### 错误 2：访问属性忘记写 `self`

```python
def is_empty(self):
    return len(items) == 0    # ❌ NameError: name 'items' is not defined
```

**解决**：加上 `self.`：

```python
def is_empty(self):
    return len(self.items) == 0    # ✅
```

### 错误 3：从空栈/队列中弹出元素

```python
stack = Stack()
stack.pop()    # IndexError: 栈为空
```

**解决**：先检查是否为空：

```python
if not stack.is_empty():
    stack.pop()
```

---

## 七、参考文件

- [stack_and_queue_demo.py](file:///workspace/02_data_structures/02_stack_queue/stack_and_queue_demo.py) - 示例代码
