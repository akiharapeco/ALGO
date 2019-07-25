class MinStack:
    stack = []
    stackmin = []

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stackmin = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.stackmin or self.stackmin[-1] >= x:
            print(x)
            self.stackmin.append(x)

    def pop(self) -> None:
        if self.stack:
            x = self.stack.pop()
        else:
            return
        if self.stackmin and self.stackmin[-1] == x:
            self.stackmin.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stackmin:
            return self.stackmin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()