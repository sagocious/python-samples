def Factorial(n):
    if n == 0: 
		return 0
    elif n == 1: 
		return 1
    else: 
		return Factorial(n-1)+Factorial(n-2)

Factorial(3):
