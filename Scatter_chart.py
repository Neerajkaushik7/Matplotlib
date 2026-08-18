"""
Program Name : Monthly Customer vs Sales Scatter Plot
Author       : Neeraj Kaushik
Description  :
    This program uses Matplotlib to create a scatter plot
    showing the relationship between the number of customers
    and sales for each month. The color of each point
    represents the sales value, and each point is annotated
    with its corresponding month.
"""

# Implementation:

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep"]

customers = [120, 150, 135, 180, 200, 220, 190, 250, 280]

sales = [25000, 32000, 28000, 40000, 45000, 51000,
         43000, 58000, 65000]

# Create scatter plot
plt.scatter(customers, sales, c=sales, cmap="coolwarm")

# Annotate each point with its corresponding month
for i in range(len(months)):
    plt.annotate(f"{months[i]}", (customers[i], sales[i]))

# Add colorbar to represent sales
plt.colorbar(label="Sales")

plt.grid()
plt.show()