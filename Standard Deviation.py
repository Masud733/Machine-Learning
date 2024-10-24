import numpy as np
dt =[12,33,65,77,10,99,45]
stdn = np.std(dt)
mdn = np.median(dt)
print("Median=",mdn)
print("Standard Deviation:",stdn)

dt2 =[86,87,88,86,87,85,86]
stdn2 = np.std(dt2)
print(stdn2)
# Meaning that most of the values are within the range of 0.9 from the mean value, which is 86.4.


# The variance is the average number of these squared differences:
dt3 = [32,111,138,28,59,77,97]
variance= np.var(dt3)
print("Variance: ",variance)

# As we have learned, the formula to find the standard deviation is the square root of the variance:
std3=np.std(dt3)
print("Standard Deviation:",std3)