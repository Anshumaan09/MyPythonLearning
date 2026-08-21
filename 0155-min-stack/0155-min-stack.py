class MinStack:

    def __init__(self):
        self.lst = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.lst.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(
                min(value, self.min_stack[-1])
            )

    def pop(self) -> None:
        if len(self.lst) == 0:
            raise Exception("Empty Stack")
        else:
            self.lst.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if len(self.lst) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.lst[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()