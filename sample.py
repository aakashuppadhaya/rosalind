'''def percent_gc(st):
	t=st.count('G')
	e=st.count('C')
	z=t+e/len(st)*100
	print(z)
st="GCEGRFGRFGC"
percent_gc(st)'''
'''with open("fasta.txt") as fs:
	li=fs.readlines()
for i in range(0,len(li)):
	q=''.join(str(li[i]))
	print(q)'''
'''f = open('fasta.txt', 'r')
lines = f.readlines()
mystr = '\t'.join([line.strip() for line in lines])
print(mystr)'''
def foo():
    string = ("this is an "
              "implicitly joined "
              "string","how are you"
              	"this is my home")
    print(string)
foo()
sr=input()
t=sr.count('G')
print(t)