import numpy as np

list = [20, 30, 40, 50 ]
array =np.array(list)
print (type(array ))

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array2 = np.array(list2)
print(type([array2]))
print(array2.shape)


array1 = np.arange(1,10)
print(type(array1))
print(array1.shape)

#2d array
import numpy as np
array2d = np.arange(1,13).reshape(2,6)
print(array2d)

#use double brackets tocreate 2d array
import numpy as np
array3 = np.arange(1,13)
print(array3.shape)
print(type(array3))

#indexing
import numpy as np
a = np.arange(1,9)
print(a)

import numpy as np 
b = np.array([[1,2,3,5,6,9],
              [1,2,3,4,6,6],
              [1,2,3,5,6,7]])
print(b.ndim)
print(b)
print(b[1,4])


