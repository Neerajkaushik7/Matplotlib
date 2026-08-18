"""
Program Name: Stack Plot using Matplotlib
Author: Neeraj Kaushik
Description: Create a stack plot to visualize monthly sales of
             laptops, mobiles, and tablets.
Date: 17 August 2026
"""

#Implementation
import matplotlib.pyplot as plt

# Create data
months = ["Jan", "Feb", "Mar", "Apr"]

laptop = [12, 14, 29, 23]
mobile = [23, 34, 63, 53]
tablets = [5, 12, 23, 19]

# Create stack plot
plt.stackplot(
    months,
    laptop,
    mobile,
    tablets,
    labels=["Laptop", "Mobile", "Tablets"]
)


plt.legend()


plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Data Analysis")

plt.show()