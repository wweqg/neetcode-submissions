class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for i, t in enumerate(tokens):
            if t == "+":
                op1 = s.pop()
                op2 = s.pop()
                tmp = op1+op2
                s.append(tmp)

            elif t == "-":
                op1 = s.pop()
                op2 = s.pop()
                tmp = op2-op1
                s.append(tmp)

            elif t == "*":
                op1 = s.pop()
                op2 = s.pop()
                tmp = op1*op2
                s.append(tmp)
            
            elif t == "/":
                op1 = s.pop()
                op2 = s.pop()
                tmp = op2/op1
                s.append(int(tmp))
            
            else:
                s.append(int(t))
        
        return s[0]

    
    