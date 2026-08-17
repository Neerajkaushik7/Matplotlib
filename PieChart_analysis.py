"""
Program Name: Pie Chart using Matplotlib
Author: Neeraj Kaushik
Description: Create a pie chart to visualize the percentage distribution
             of different programming languages.
Date: 16 August 2026
"""

#Implementation
import matplotlib.pyplot as plt


labels = ["Python", "C++", "Java", "C"]
values = [37, 23, 29, 11]

# Create pie chart
plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    explode=[0, 0.5, 0, 0],
    shadow=True,
    wedgeprops={
        "edgecolor": "black",
        "linewidth": 2,
        "linestyle": "--"
    }
)


plt.title("Programming Language Distribution")
plt.show()