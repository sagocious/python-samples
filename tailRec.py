def tailRec(num):
	if num == 0:
		return
	else:
		print(num)
	tailRec(num-1)
	
tailRec(10)


