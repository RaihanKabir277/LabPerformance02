
import numpy as np

x = np.random.randint(0, 100, size=100)

normalized = (x - x.min()) / (x.max() - x.min())

print(normalized)
