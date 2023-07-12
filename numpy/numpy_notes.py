'''
uses of numpy 
    the porpose is efficient data storage 
    it is faster
    ??supposedly easy to learn??
    reletivly less memory dependent

uses of jupyter 
    uses for data utilisation 
    and data sharing 
    
'''
import numpy as np

#CONVERSION FROM PYTHON STRUCTURES 
my_arr=np.array([[1,2,3],[4,5,6],[7,8,9]],np.int32)
print(my_arr.size)
print(my_arr.shape)
print(my_arr.dtype)
print(my_arr[0,0],my_arr[1,1],my_arr[2,2])

tes_arr=np.array({1,2,3})
print(tes_arr.size)
print(tes_arr.shape)
print(tes_arr.dtype)
print(tes_arr)

#INTRINSIC NUPY CREATION OBJECTS
zeros=np.zeros((3,3))
print(zeros)
print(zeros.dtype)
print(zeros.shape)

rng=np.arange(15)
print(rng)
print(rng.dtype)
print(rng.shape)

lspace=np.linspace(1,50,5)
print(lspace)
print(lspace.dtype)
print(lspace.shape)

emp=np.empty((5,5))
print(emp)
print(emp.dtype)
print(emp.shape)

emp_like=np.empty_like(lspace)
print(emp_like)
print(emp_like.dtype)
print(emp_like.shape)

ide=np.identity(5)
print(ide)
print(ide.dtype)
print(ide.shape)
import numpy as np
arr=np.arange(15)
print(arr)
print(arr.reshape(3,5))
print((arr.reshape(3,5)).ravel())


