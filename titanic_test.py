import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

filename = 'titanic-data.csv'
df = pd.read_csv(filename)
df.describe()

p_df=df[['Pclass','Survived']]
p_df.describe()