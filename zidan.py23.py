# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 22:21:13 2024

@author: ASUS
"""

import pandas as pd

df = pd.read_csv("negara.csv")

print("Berikut Data Framenya:\n")
print(df)

mean_values = df.groupby("Benua")[['Luas', 'Populasi']].mean()
std_dev_values = df.groupby("Benua")[['Luas', 'Populasi']].std()

print("\nBerikut Data Mean:\n")
print(mean_values)
print("\nBerikut Data Standard Deviation:\n")
print(std_dev_values)

mean_values.to_csv("output/NegaraMean.csv")

std_dev_values.to_csv("output/NegaraStandarDeviasi.csv")

print("\nFile Berhasil Dibuat")
