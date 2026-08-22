'''
Data Analysis
-------------
--> Data Analysis is the process of collecting, cleaning, transforming, organizing, and analysing data to convert into useful information
and also used for making decisions to get the better outcome...

library used
------------
Numpy
Pandas
matplotlib
seaborn


Numpy
-----
--> This refers to Numberical python
--> It is a python library used for calculations and operations
--> This python library is more faster then the list to perform operations
--> And also supports multi-dimensional arrays

eg--
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr.ndim)

eg--
import numpy as np
arr_1=np.array([1,2,3,4,5])
print(arr_1.ndim)
arr_2=np.array([[1,2,3],[4,5,6]])
print(arr_2.ndim)
arr_3=np.array([[[1,2],[3,4],[5,6]]])
print(arr_3.ndim)

eg--
import numpy as np
arr_1=np.array([1,2,3,4,5])
print(arr_1.shape)
arr_2=np.array([[1,2,3],[4,5,6]])
print(arr_2.shape)
arr_3=np.array([[[1,2],[3,4],[5,6]]])
print(arr_3.shape)

Functions
---------
ndim
----
--> The function is used to find out the dimensions of an array
syntax --> array.ndim
eg--
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr.ndim)

shape
-----
--> The shape functions is used to find the row & col of an array
syntax --> array.shape
eg--
import numpy as np
arr_1=np.array([1,2,3,4,5])
print(arr_1.shape)

reshape
-------
--> The function is used to convert one dimention to another if the elements are there convert into the any dimention
syntax --> array.reshape(row,col)
eg--
import numpy as np
arr_1=np.array([1,2,3,4,5])
print(arr_1.reshape(5,1))
print(arr_1.reshape(1,5))
arr2=np.array([1,2,3,4,5,6,7,8,9])
print(arr2.reshape(3,3))

size
----
--> The size function is used to find out number of elements present in an array
syntax --> array.size
eg--
import numpy as np
arr2=np.array([1,2,3,4,5,6,7,8,9])
print(arr2.size)

arange
------
--> The arange function is used to generate number in a sequence upto a limit and it forms 1D array
--> And this array can be convert into 2D arrays by using reshape
syntax  --> np.arange(range)
eg--
import numpy as np
arr=np.arange(1,10)
print(arr)

eg--
import numpy as np
arr=np.arange(1,10)
print(arr.reshape(3,3))
print(arr)



Operations
----------
--> same as list we can also perform some operations on arrays
1.Indexing
----------
eg--
import numpy as np
arr2=np.array([3,8,5,1,7,2,4,9,6])
print(arr2[5])

2.sciling
---------
eg--
import numpy as np
arr2=np.array([3,8,5,1,7,2,4])
print(arr2[2:5])

3.sum
-----
eg--
import numpy as np
arr2=np.array([3,8,5,1,7,2,4])
print(arr2.sum())

4.add
-----
eg--
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(arr1+arr2)
print(arr1+5)

5.sub
-----
eg--
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(arr2-arr1)
print(arr2-3)

6.mul
-----
eg--
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(arr2*arr1)
print(arr1*2)

7.power
-------
eg--
import numpy as np
arr1=np.array([1,2,3,4,5])
print(arr1**2)

8.div
-----
eg--
import numpy as np
arr1=np.array([1,2,3,4])
print(arr1/2)

9.max
-----
eg--
import numpy as np
arr1=np.array([5,3,1,9,6,12,4,7])
print(arr1.max())

10.min
------
eg--
import numpy as np
arr1=np.array([5,3,1,9,6,12,4,7])
print(arr1.min())

'''
import numpy as np
arr=np.arange(1,10)
print(arr.reshape(3,3))
print(arr)






























































