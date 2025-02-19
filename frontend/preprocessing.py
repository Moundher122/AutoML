import numpy as np
import pandas as pd
def preprocessing(df,type):
  if type=="Regression":
    numerical = df.select_dtypes(include=[np.number])
    categorical = df.select_dtypes(include=[object])
  elif type=="Classification":
    x = df.iloc[:, :-1]
    y = df.iloc[:, -1]   