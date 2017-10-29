#import numpy as np  
#csv=np.loadtxt('mushrooms.csv',dtype=str)
#print(csv)#imported in 1d array
import csv
import numpy
reader = csv.reader(open("mushrooms.csv"), delimiter=",") #read csv file from txt file
x = list(reader)
result = numpy.array(x).astype("str")#convert string into numpy array i have give str in astype as my dataset is in string format imported as 2d array
print(result)
print(result[ :,1])#to print 1st index of colums
print(result[1:3,:])
print(result.shape)# represent shape of data
c=result.reshape(5,1625,23)#converted into 3d array
print(c)
for row in result:#this line indicate iterating through each array in result
	i=row
''' for e in result.flat:
	print(e)'''
a=numpy.arange(4)
#print(a)
b=numpy.arange(4)
#print(b)
r=a.reshape(2,2)
#print(r)
t=b.reshape(2,2)
h=numpy.vstack((r,t))#vertical stacking of different array
#print(h)
y=numpy.hstack((r,t))#horizontal stacking of different array
#print(y)
print(numpy.hsplit(result,3))
