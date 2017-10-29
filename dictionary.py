str=input()
l= str.split(' ') 
d={}
for i in l:
	d[i]=l.count(i)
for i in d:
	print (i, d[i])
