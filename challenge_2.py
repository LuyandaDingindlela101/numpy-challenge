#   Write a NumPy program to compute the histogram of nums against the bins. Label your x-axis with nums and y-axis
#   with bins. Add a title to the histogram: Histogram of nums against bins.

import numpy as numpy
import matplotlib.pyplot as plt

#   CREATE THE NUMPY ARRAYS
nums = numpy.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = numpy.array([0, 1, 2, 3])

#   PRINT THE DETAILS
print("nums: ", nums)
print("bins: ", bins)
print("Result:", numpy.histogram(nums, bins))

#   ADD THE TITLE
plt.title("Histogram of nums against bins.")
#   ADD THE X-AXIS LABEL
plt.xlabel("nums")
#   ADD THE Y-AXIS LABEL
plt.ylabel("bins")
#   PLOT THE GRAPH WITH THE VALUES
plt.hist(nums, bins=bins)
#   SHOW THE GRAPH
plt.show()