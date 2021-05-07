import numpy as np
import scipy.stats as stats

mu = 100 # mean
sigma = 2 # the standard deviation
size = 100000 # the population

#set random seed, the generator creates random number based on the seed value
np.random.seed(123)
pop = np.random.normal(loc=mu, scale=sigma, size=size)

# Displays dataset
print(pop)
#displays the population size
print(pop.size)
# prints the mean (should be close to 100)
print(pop.mean())
#standard deviation- should be close to 2
print(pop.std())

#Define a sample size out of the population
sample_size = 50 
np.random.seed(123)#set random seed generator
sample = np.random.choice(pop, sample_size, replace=False)

# Displsy sample statisticss
print(sample) # Dataset
print(sample.size) # Displays 50
print(sample.mean()) # close to 100

#This method describes the sample result 
#This result is use to support or not support the htpothesis
print(stats.describe(sample))
