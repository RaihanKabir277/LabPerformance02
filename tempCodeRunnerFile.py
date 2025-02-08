
import matplotlib.pyplot as plt
import numpy as np

regions = ['North', 'South', 'East', 'West']
sales_revenue = [25000, 30000, 22000, 27000]

plt.bar(regions, sales_revenue, color='skyblue', width=0.6)
plt.title("Sales Revenue Across Different Regions")
plt.xlabel("Regions")
plt.ylabel("Sales Revenue (in $)")
plt.show()
