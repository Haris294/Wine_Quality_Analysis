import numpy as np
import pandas as pd
import warnings #ignore warnings
warnings.filterwarnings('ignore')

red_wine_data = pd.read_csv('https://raw.githubusercontent.com/btkhimsar/DataSets/master/winequality-red.csv',sep=";")

"""white_wine_data = https://raw.githubusercontent.com/btkhimsar/DataSets/master/winequality-white.csv"""

red_wine_data.head()
red_wine_data.shape
red_wine_data.describe()
red_wine_data.columns
red_wine_data['quality'].unique()
red_wine_data['quality'].nunique()
red_wine_data['quality'].value_counts()
red_wine_data.rename(columns= {'fixed acidity':'fixed_acidity', 'volatile acidity':'volatile_acidity', 'citric acid':'citric_acid', 'residual sugar':'residual_sugar',
      'free sulfur dioxide':'free_sulfur_dioxide', 'total sulfur dioxide':'total_sulfur_dioxide',})

red_wine_data.isna()
red_wine_data.isna().sum()
red_wine_data.info()
duplicate = red_wine_data[red_wine_data.duplicated()]
duplicate.shape

import matplotlib.pyplot as plt
import seaborn as sns

y = red_wine_data['quality']
X = red_wine_data.drop(red_wine_data['quality'],inplace= True)

red_wine_data.corr()
plt.figure(figsize=(16,12))
sns.heatmap(red_wine_data.corr(),cmap='bwr',annot=True)
sns.pairplot(red_wine_data)
sns.boxplot(y,red_wine_data['alcohol'],palette='GnBu_d')
plt.title("Boxplot of quality and alcohol")
plt.show()