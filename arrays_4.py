from numpy import *

arr_1 = array([[11,12],[13,14]])
arr_2 = array([[10,20],[30,21]])
print(arr_1)
print(arr_2)

print("addition : ",arr_1 + arr_2)

mat_mul = matmul(arr_1, arr_2)
print("multiplication : ",mat_mul)
