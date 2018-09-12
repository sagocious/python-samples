def countUpTo(n):
	if n > 1: 
		countUpTo(n-2)
	print(n)

countUpTo(1000) 
