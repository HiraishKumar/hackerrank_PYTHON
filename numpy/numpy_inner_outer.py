'''
inner

The inner tool returns the inner product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4
outer

The outer tool returns the outer product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]
'''

import numpy as np

arr1=np.array(list(map(int, input().split())))
arr2=np.array(list(map(int, input().split())))

print(np.inner(arr1,arr2))
print(np.outer(arr1,arr2))



