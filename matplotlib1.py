
import numpy as np
import matplotlib.pyplot as plt

days = [ 'Saturday', 'Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

temperatures = [22, 24, 23, 25, 26, 27, 28]

plt.plot(days, temperatures, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)

plt.title("Temperature Variation Over a Week")
plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")

plt.grid(True)

plt.show()
