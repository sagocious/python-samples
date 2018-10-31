def fibonacchi_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacchi_recursive(n-1) + fibonacchi_recursive(n-2)

print(fibonacchi_recursive(3))
