def inAscOrder(text):
	for i in range(len(text)-2):
		if ord(text[i])>ord(text[i+1]):
			return False
	return True
	
def inDescOrder(text):
	for i in range(len(text)-2):
		if ord(text[i])<ord(text[i+1]):
			return False
	return True
	
def allAlpha(s):
	for c in s:
		if not c.isalpha():
			return False
	return True
	
text = raw_input("Enter Text: ")

if allAlpha(text):
	if inAscOrder(text.upper()):
		print text+" IN ORDER"
	elif inDescOrder(text.upper()):
		print text+" REVERSE ORDER"
	else:
		print text+" NOT IN ORDER"
else:
	print "ERROR"
	
