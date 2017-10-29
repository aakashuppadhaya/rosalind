m=int(input())
off=int(input())
def rabbit_count(w,n):
				if(w==0):
					return 0
				if(w==1):
					return 1
				if(w==2):
					return n
				g1=rabbit_count(w-1,n)
				g2=rabbit_count(w-2,n)
				if(w<=40):
					return g1+g2
rt=rabbit_count(m,off)
print(rt)

