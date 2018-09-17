from stack import *

def ans(op, opr1, opr2):
    if op == "+":
        return opr1 + opr2
    elif op == "-":
        return opr1 - opr2
    elif op == "*":
        return opr1 * opr2
    elif op == "/":
        return opr1 / opr2

def evaluate(exp):
    s = Stack()
    operands = ["+", "-", "*", "/"]
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for i in exp:
        if i in nums:
            s.push(i)
        elif i in operands:
            opr2 = int(s.pop())
            opr1 = int(s.pop())
            s.push(ans(i, opr1, opr2))

    print s

evaluate("23*6+")
