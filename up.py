a=int(input())
b=int(input())
c=int(input())
d=int(input())
print('enter the string')
s=input()
if s<=200:
	print(s[a:b+1]+' '+s[c:d+1])
else:
	print('invalid string')