import numpy as np          #pip install numpy or install package directly
from numpy.ma.core import add

arr_1 = np.array([1,2,4,523,12],dtype=int)
print(arr_1)

arr_2 = np.array([11,12,13,14,15],dtype=int)
print(arr_2)

arr_res_1 = add(arr_1,arr_2)
print(arr_res_1)

print(arr_1 * 10)