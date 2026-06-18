"""栈与队列示例"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("栈为空")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("队列为空")

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    stack = Stack()
    for item in ["A", "B", "C"]:
        stack.push(item)
    print("栈弹出顺序:", stack.pop(), stack.pop(), stack.pop())

    queue = Queue()
    for item in ["1号", "2号", "3号"]:
        queue.enqueue(item)
    print("队列出队顺序:", queue.dequeue(), queue.dequeue(), queue.dequeue())
