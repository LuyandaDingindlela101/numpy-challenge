#   Write a NumPy program to compute the mean, standard deviation, and variance of a given array along the second axis.
#   Use np.arrange function to generate 20 numbers starting from 0.
import numpy as numpy
import matplotlib.pyplot as plt

data = numpy.arange(0, 21, 1, int)
#   CALCULATE THE MEAN
mean = numpy.mean(data)
#   CALCULATE THE MEDIAN
median = numpy.median(data)
#   CALCULATE THE STANDARD DEVIATION
standard_deviation = numpy.std(data)
#   CALCULATE THE VARIANCE
variance = numpy.var(data)

print("mean: " + str(mean))
print("median: " + str(median))
print("variance: " + str(variance))
print("standard deviation: " + str(standard_deviation))

