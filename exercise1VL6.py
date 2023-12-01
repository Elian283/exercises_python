
import numpy
m=numpy.eye(5)
m[:2,3:]=3
m[3: , :2]=2
print(m)


