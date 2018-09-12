def c_to_f(t):
	return t*9/5 + 32

def f_to_c(t):
	return (t - 32)*5/9
	
s = raw_input("Temperature reading : ")

d = s[len(s)-1]

if d=='C' or d=='c':
	print c_to_f(int(s[:-1])),"F"
else:
	print f_to_c(int(s[:-1])),"C"
	
