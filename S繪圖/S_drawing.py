import matplotlib.pyplot as plt
from numpy import array
import pandas as pd
import numpy as np

df = pd.read_excel('豐榮(3).xlsx')
plt.scatter(df['S'],df['Level change'])
plt.xlabel("S") 
plt.ylabel("Watertable change(m)") 
plt.xlim(xmin = -0.002)
plt.xlim(xmax = 0.004)
plt.show()