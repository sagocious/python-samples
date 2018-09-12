#!/usr/bin/python

n = 0;
for a in xrange(999, 100, -1):
	for b in xrange(999, 100, -1):
		pali1 = str(a*b)
		pali2 = pali1[::-1]
		if pali1 == pali2:
			if a*b >= n:
				n = a*b
				print pali1, pali2

print n
