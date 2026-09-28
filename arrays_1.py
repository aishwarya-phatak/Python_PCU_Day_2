import array as a

arr_1 = a.array('i',[11,11,13,14,15])
print("array elements : ")
for each_element in arr_1:
    print(each_element)

for x in arr_1:
    print(x * 10)

print("accessing single element : ")
print(arr_1[3])

print("creating an array from existing array : ")
arr_2 = a.array(arr_1.typecode,[x + 5 for x in arr_1])
for each_element in arr_2:
    print(each_element)

#slicing of an array with start, stop, stride & negative indices

print(arr_1[0:5:2])
print(arr_1[:4])
print(arr_1[-3:])
print(arr_1[-4:-2])

#methods on array
arr_1.append(10)            #appending elements to an array
print(arr_1)

arr_1.insert(2,99)     #inserting at a specific position
print(arr_1)

arr_1.pop()                 #pop
print(arr_1)

arr_1.pop(3)                #index based pop
print(arr_1)

arr_1.reverse()             #reversing an array
print(arr_1)

cnt = arr_1.count(11)             #counting the occurrences of element in a array
print(cnt)

arr_1.extend([32,11,88,44])     #extending an array with iterable
print(arr_1)

arr_1.insert(3,161)
print(arr_1)