# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:06:28 2021

@author: Arman
"""

import numpy as np
a = np.arange(6)
a2 = a[np.newaxis, :]
a2.shape

array_example = np.array([  [   [0, 1, 2, 3],
                                [4, 5, 6, 7]      ],
                          [     [0, 1, 2, 3],
                                [4, 5, 6, 7]      ],
                          [     [0 ,1 ,2, 3],
                                [4, 5, 6, 7]      ]   ])
print(array_example.shape)

# resizing dims
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(a.shape)

b = np.expand_dims(a, axis=0)
print(b)
print(b.shape)

b = np.expand_dims(a, axis=1)
print(b)
print(b.shape)

b = np.expand_dims(array_example, 2)
print(array_example)
print(b)
print(b.shape)

# powerful indexing
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

five_up = (a >= 5)
print(a[five_up])

divisible_by_2 = a[a%2==0]
print(divisible_by_2)

five_up = (a > 5) | (a == 5)
print(five_up)