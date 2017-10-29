a=int(input())
b=int(input())
sum=0
if a and b >10000:
	print('plz put value in range')
for i in range(a,b):
	if(i%2!=0):
		sum=sum+i
print(sum)