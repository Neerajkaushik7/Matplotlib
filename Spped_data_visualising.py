"""
Program Name : Speed Graph
Author       : Neeraj Kaushik
Description  : Calculate speed from time and distance data stored
               in a NumPy 2D array and visualize it using Matplotlib.
               +---------+--------------------------+
| TIME(s) | DISTANCE FROM START(m)  |
+---------+--------------------------+
|    0    |           0              |
|    1    |          15              |
|    2    |          30              |
|    3    |          45              |
|    4    |          60              |
|    5    |          75              |
+---------+--------------------------+
"""

# Implementation:

import numpy as np
import matplotlib.pyplot as plt

# Create 2D array
data = np.array([
    [0, 0],
    [1, 10],
    [2, 20],
    [3, 40],
    [4, 60],
    [5, 120]
])

# Column extracted from array
time = data[:, 0]
distance = data[:, 1]

# Calculate speed
speed = np.diff(distance) / np.diff(time)

# Plot speed graph
plt.plot(time[1:], speed, marker="o")

# Add labels and title
plt.xlabel("Time")
plt.ylabel("Speed")
plt.title("Speed Graph Plot")

# Display Result
plt.show()