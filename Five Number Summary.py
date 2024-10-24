import matplotlib.pyplot as plt
import numpy as np

data = [59, 60, 70, 61, 62, 62, 63, 63, 64, 64, 64, 65, 65, 65, 65, 65, 65, 65,
        66, 66, 67, 67, 68, 68, 69, 70, 70, 70, 70, 71, 71, 72, 72, 73, 74, 74,
        65, 65, 75, 77]

# Calculate the five-number summary
minimum = np.min(data)
q1 = np.percentile(data, 25)
median = np.median(data)
q3 = np.percentile(data, 75)
maximum = np.max(data)

plt.boxplot(data, vert=False, patch_artist=True)
plt.xlabel("Height")
plt.title("Box Plot of Student Heights")

# Show the five-number summary
print(f"Minimum: {minimum}")
print(f"Q1 (First Quartile): {q1}")
print(f"Median: {median}")
print(f"Q3 (Third Quartile): {q3}")
print(f"Maximum: {maximum}")
plt.show()
