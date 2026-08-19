"""
Program Name : Salary Distribution Analysis
Author       : Neeraj Kaushik
Description  :
    This program uses Matplotlib to create a histogram
    showing the distribution of employee salaries across
    different salary ranges.
"""

# Implementation:

import matplotlib.pyplot as plt

salary = [25000, 32000, 18000, 45000,
          38000, 52000, 26000, 41000,
          61000, 35000, 62000, 69100]

bins = [10000, 20000, 30000, 40000, 50000, 60000, 70000]

# Create histogram
plt.hist(salary, bins=bins, edgecolor="black")

# Add title and axis labels
plt.title("Salary Analysis of a Company")
plt.xlabel("Salary Range")
plt.ylabel("Occurrence")

# Add grid
plt.grid("--", alpha=0.5)

# Display the plot
plt.show()