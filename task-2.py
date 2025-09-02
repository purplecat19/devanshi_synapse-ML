import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Asus\projects\devanshi_synapse-ML\vgsales.csv.zip")  #load dataset

print(df.head())  #peeking at first 5 rows
print(df.shape)    #checking rows and columns

print(df.info())  # info about columns
print(df.isnull().sum())  #counting missing values



