from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.chisquare(df=2,size=(1000)),label='exponential')
sns.distplot(random.rayleigh(scale=1,size=(1000)),label='poisson')
plt.show()