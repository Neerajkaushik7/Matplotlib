"""
Program Name: Virat Kohli and Suresh Raina Year-Wise Runs
Author: Neeraj Kaushik
Description:
    This program uses Matplotlib to create a grouped bar chart
    comparing Virat Kohli's and Suresh Raina's year-wise runs.
    The exact run values are displayed above each bar.
"""

# Implementation:

import numpy as np
import matplotlib.pyplot as plt


# User Input
years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

kohli_runs = [330, 750, 1995, 1585, 2186, 1960, 2286, 1164,
              2595, 2818, 2735, 2455, 842, 964, 1348, 2048]

raina_runs = [680, 751, 1323, 1174, 807, 789, 627, 553,
              220, 104, 345, 0, 0, 160, 0, 0]


# Create X-axis Positions
x = np.arange(len(years))
width = 0.2


# Create Bars
bar1 = plt.bar(x - width, kohli_runs, width, label="Kohli")
bar2 = plt.bar(x + width, raina_runs, width, label="Raina")


# Display Exact Values Above Bars
plt.bar_label(bar1, padding=3)
plt.bar_label(bar2, padding=3)


# Add Labels and Title
plt.xlabel("Years")
plt.ylabel("Runs")
plt.title("Virat Kohli and Suresh Raina Year-Wise Runs")


# Display Actual Years on X-axis
plt.xticks(x, years, rotation=45)


# Display Legend
plt.legend()


# Display Result
plt.tight_layout()
plt.show()