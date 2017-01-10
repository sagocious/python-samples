def countUpTo(n):
	if n > 1:
		countUpTo(n-1)
	print(n)

countUpTo(100)
