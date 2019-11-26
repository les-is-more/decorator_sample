import numpy as np
from matplotlib import pyplot as plt
import inspect

# sampling from a two normally distributed datasets
mu1, mu2, sigma = 0, 1, 3
norm1 = np.random.normal(mu1, sigma, 1000)
norm2 = np.random.normal(mu2, sigma, 1000)

# Note: get the MLE of the generated mixture model

# Goal is to determine the approximate distribution of each dataset and estimate the values of the distribution parameters

# Generative Mixture distribution
delta = 0.2
mixed_norm = norm1 * delta + norm2 * (1 - delta)

# Plot start
plt.figure(figsize=(10,4))
count1, bins1, ignored1 = plt.hist(norm1, 30, alpha = 0.5, density = True, label = "N(mu = {}, sigma = {})".format(mu1, sigma))
count2, bins2, ignored2 = plt.hist(norm2, 30, alpha = 0.5, density = True, label = "N(mu = {}, sigma = {})".format(mu2, sigma))
count3, bins3, ignored3 = plt.hist(mixed_norm, 30, alpha = 0.5, density = True, label = "Mixed Gaussian Distribution")

plt.plot(bins1, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins1 - mu1) ** 2 / (2 * sigma**2) ),
          linewidth = 2, color = 'r')
plt.plot(bins2, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins2 - mu2) ** 2 / (2 * sigma**2) ),
          linewidth = 2, color = 'b')

plt.title("$N(\mu$ = {}, $\sigma$ = {}) and $N(\mu$ = {}, $\sigma$ = {}), plus the Generated Mixed Gaussian ".format(mu1, sigma, mu2, sigma))
plt.legend()
# plt.title('Mixed Gaussian Distribution with $\delta$ = 0.2')

# saves the plot into a .png file instead of displaying it
# plt.savefig('normal_compare.png')
plt.show()
plt.close()

# practice RFE (recursive feature elimination) and other pre-processing steps
