# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:25:19 2024

@author: ASUS
"""

import pandas as pd

df = pd.read_csv(r'C:/Users/ASUS/OneDrive/Desktop/Algoritma/Negara - Negara.csv')


numeric_cols = df.select_dtypes(include=['number']).columns
rata = df.groupby(['Benua'])[numeric_cols].mean()  
std = df.groupby(['Benua'])[numeric_cols].std()  

print('DATA NEGARA, BENUA, SEMUANYA DAH LENGKAP')
print(df)
print('---BERIKUT DATA MEAN---')
print(rata)
print('---BERIKUT DATA STANDARD---')
print(std)

