class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if not self.s:
            self.s.append((val, val))
        else:
            self.s.append((val, min(self.getMin(), val)))

    def pop(self) -> None:
        if self.s:
            self.s.pop()[0]

    def top(self) -> int:
        return self.s[-1][0]
        

    def getMin(self) -> int:
        return self.s[-1][-1]
        
