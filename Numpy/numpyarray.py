import numpy as np
a = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(a)
print(a.ndim)

#3 dimensional array to create  use ([[[this]]]) the more square 
# brackets you use the more dimensions it will have
import numpy as np
b = np.array([[[1,2,3,5,6],[1,2,3,5,5],[1,2,3,5,6], [1,2,3,4,5]])
print(b)
print(b.ndim)
#use ndim to check dimensions of array

#shape method to chek shape of the array
import numpy as np
c = np.array([[1,2,3,5,6],
              [1,2,3,5,6]])
print(c.shape)
print(c)

#use size methood 
import numpy as np
d = np.array([[1,3,4,6],
              [1,3,5,6,]])
print(d.size)
print 