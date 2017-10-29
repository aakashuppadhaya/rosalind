f=open('aakash.txt','r')
i=1
l=f

for line in f.readlines():
	#d=f.readlines()[2]
	#print(d)
	if i%2==0:
		print(line)
	i=i+1
