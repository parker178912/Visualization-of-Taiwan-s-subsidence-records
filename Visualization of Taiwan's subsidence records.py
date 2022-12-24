import matplotlib.pyplot as plt
from numpy import array
import pandas as pd
import numpy as np

def add_div_column(df_base, df, size):
    i = 2
    col_name = list(df_base.columns.values.tolist())
    while i < size:
        pre_col = col_name[i]
        df.insert(i - 1, pre_col, df_base.磁環深度 - df_base.iloc[:, i])
        i = i + 1
df = pd.read_excel('南光.xlsx')
df2 = pd.DataFrame(df.磁環深度)
add_div_column(df, df2, len(df.columns))
df2.set_index("磁環深度", inplace=True)
index_value = df2.index.values
for label, value in df2.items():
    plt.plot(value, index_value, label=label)
plt.xlabel("Comulative compaction (m)", fontsize=18)
plt.ylabel("Depth (m)", fontsize=18)
plt.legend()
plt.gca().invert_yaxis()
plt.show()
