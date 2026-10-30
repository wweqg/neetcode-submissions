class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if self.s:
            curr_min = self.s[-1][-1]
            new_min = min(val, curr_min)
        else:
            new_min = val  # If the stack is empty, the new element is the min
        self.s.append((val, new_min))

    def pop(self) -> None:
        self.s.pop()[0]

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][-1]
