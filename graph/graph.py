# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# generate random data
df = pd.DataFrame(np.random.randint(0,100,size=(15, 2)), columns=list('AB'))
df_html = df.to_html()
print(df_html)

# plot the dataframe
fig, ax = plt.subplots()
ax.scatter(df.A, df.B, color='red')
fig