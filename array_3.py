from numpy import *

arr_1 = array([15,2,3,4,5])
result_arr = where(arr_1 % 2 , arr_1 + 5 ,arr_1 - 5)
print(result_arr)

print(arr_1.shape)
print(arr_1.dtype)
print(arr_1.size)
print(arr_1.itemsize)
print(arr_1.ndim)

arr_2 = array([1,2,3,4,5])

arr_3 = arr_1 == arr_2      #checking with equality of two arrays
print(arr_3)

arr_4 = array([True,False,True,True,True])
print("any function ",any(arr_4))
print("all function",all(arr_4))

#logical_and
arr_5 = logical_and(arr_1<=5,arr_2>=5)
print(arr_5)