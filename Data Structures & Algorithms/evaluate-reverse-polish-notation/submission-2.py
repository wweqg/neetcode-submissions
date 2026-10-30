class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for c in tokens:
            if c == "+":
                op2 = int(s.pop())
                op1 = int(s.pop())
                res = op1 + op2
                s.append(res)
            elif c == "-":
                op2 = int(s.pop())
                op1 = int(s.pop())
                res = op1 - op2
                s.append(res)
            elif c == "*":
                op2 = int(s.pop())
                op1 = int(s.pop())
                res = op1 * op2
                s.append(res)
            elif c == "/":
                op2 = int(s.pop())
                op1 = int(s.pop())
                res = op1 / op2
                s.append(int(res))
            else:
                s.append(int(c))
        
        return s[0]