# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:37:14 2021

@author: Arman
"""

import matplotlib.pyplot as plt
# this makes the index the x axis
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# plot x vs y
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

# puts red circles instead of a line using the ro
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# x axis 0-6 , y axis 0-20
plt.axis([0, 6, 0, 20])
plt.show()

import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# using categorical variables
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()