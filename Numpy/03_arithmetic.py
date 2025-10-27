import numpy as np
#arithmetic operations on numpy arrays
array = np.array([[1,2],
                  [2,3]])
array2 = np.array([[2,3],
                   [5,6]])
array3 = array + array2
print(array.ndim)
print(array3)

# matrix multiplication
import numpy as np
x = np.array([[1,3],
              [1,2]])
y = np.array([[5,6],
              [5,5]])
z = x*y
print(z)
#will make rows to columns and columns to rows
import numpy as np
x = np.array([[1,3],
              [1,2]])
y = np.array([[5,6],
              [5,5]])
print(x.transpose())
#sorting 2d arrays in numpy
import numpy as np
x = np.array([[1,3,5,6],
              [5,6,5,3],
              [2,5,6,7]])
x.sort(axis=0)
print(x)
 