#import numpy as np          #pip install numpy or install package directly
from numpy import *

arr_1 = array([1,2,3,4],dtype=int)
print(arr_1)
print(shape(arr_1))

arr_2 = array([10,20,30,40],dtype=int)
print(arr_2)
print(shape(arr_2))

print("array operations without using for loop")
arr_r_1 = arr_1 * 5
print(arr_r_1)

arr_r_2 = arr_1 - 10
print(arr_r_2)

arr_r_3 = arr_1 + 3
print(arr_r_3)

arr_res_1 = add(arr_1,arr_2)        #array addition
print(arr_res_1)

arr_res_2 = multiply(arr_1,arr_2)   #array multiply
print(arr_res_2)

arr_res_3 = split(arr_1,2)  #array split
print(arr_res_3)

arr_cp = copy(arr_1)        #array copy using numpy
print(arr_cp)

print(arr_1 * 10)

#linspace
arr_linspace = linspace(1,10,4)
print(arr_linspace)

#logspace
arr_logspace = logspace(1,5,5)
print(arr_logspace)

#arange
arr_arange = arange(1,10,2)
print(arr_arange)

arr_zeros = zeros(5)
print("all zeros array ",arr_zeros)

arr_ones = ones(5)
print("all ones array ",arr_ones)