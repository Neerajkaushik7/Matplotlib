"""
Program Name: Line Graph with Multiple Data Series
Author: Neeraj Kaushik
Description:
    Creates a line graph for two data series using Matplotlib.
    The graph displays the axes at the origin, grid lines, labels,
    title, markers, colors, and a legend.
"""

# Implementation:

import matplotlib.pyplot as plt


# Data
a = [1, 2, 4, 5]
b = [1, 4, 16, 25]

c = [0, 2, 3, 4, 6]
d = [0.5, 2.5, 4.5, 6.5, 8.5]


# Create graph and move axes to the origin
ax = plt.gca()
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")

# Plot data
graph = plt.plot(a, b, label="Square of num")
graph += plt.plot(c, d, label="Rapid increase")


# Format graph
plt.grid()
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.title("Graph")

plt.setp(graph[0], color="r", linewidth=2, marker="o")
plt.setp(graph[1], color="g", linewidth=0.5, marker="^")

plt.legend()


# Display Result
plt.show()