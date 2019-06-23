#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:03:09 2019

@author: Kevin Chan

Objective: Pandas Dataframe testing and capabilities

"""

import pandas as pd
import numpy as np

df = pd.read_excel("champions_test.xlsx")
print(df.to_string(index=False))

print(df['Champion'])

print("=======================================")
print("Viewing Data")
print("=======================================")

print(df.head())
print("=======================================")
print(df.tail())
print("=======================================")
print(df.index)
print(df.columns)
print("=======================================")

### DataFrame.to_numpy() gives a NumPy representation of the 
### underlying data. Note that his can be an expensive operation 
### when your DataFrame has columns with different data types, 
### which comes down to a fundamental difference between pandas 
### and NumPy: NumPy arrays have one dtype for the entire array,
### while pandas DataFrames have one dtype per column. When you 
### call DataFrame.to_numpy(), pandas will find the NumPy dtype 
### that can hold all of the dtypes in the DataFrame. This may end 
### up being object, which requires casting every value to a Python object.

print(df.to_numpy())
# prints this out into a list version of the data
 
print("================== 1 =====================")
print(df.sort_values(by='Base HP '))
print("================= 2 ======================")

print(df['Base HP '])
print(df['Champion'])

print("================ 3 =======================")
print(".loc function is formatted via [ _rows_ , _columns_ ]")
print("================= 4 ======================")

print(df.loc[0,:])

print("================== 5 =====================")
print("I want to get the cross section of just champions and their BASE HP...\n")
print("USE .loc[_row_,_column_]")

print(df.loc[:,['Champion','Base HP ']])
print("================= 6 - 8 ======================")

print(".iloc[ _row_ ]) slices the whole row..\n") 

print("I want to get a specific row...for Alistar\n")
print(df.iloc[3],"\n")

print("I want to get a specific row...for Amumu\n")
print(df.iloc[4])
print("================= 9 ======================")
print("I want to get the slice of all Base Stats of Ahri and Jinx")

print(df.iloc[[0,2],[2,3,4]])
print("=================== 10 ====================")

print("Another method of sorting values is using Boolean Indexing which requires you to use the .isin method\n")

print("Using the .isin function, you can sort through columns with the specific name/value")
print(" df[df['_Column_'].isin(['_Value_'])]\n") 

df2 = df.copy()
df2['Viable?'] = ['Yes','Maybe','Maybe','Maybe','Nah']
print(df2)

print("\n")

print(df2[df2['Viable?'].isin(['Maybe'])])

print("================= 11 =====================")

print("There are various methods in adding column values...\n")
print("mostly, it consists of defining a series as a variable and 'calling' it on the dataframe, either as a column or row\n")


df2['Crowd Control'] = [1,2,1,3,2]
print(df2,"\n")

print("There are also ways to 'set' values on certain locations of a dataframe...eg: \n")

print("...value by specific position...(using .iat [_row #_, _column #_]...)\n")
df2.iat[1,4] = 0
print(df2,"\n")

print("...value by label...(using .at [_row #_, _column name_]...)\n")
df2.at[2,'Base AP'] = 0
print(df2,"\n")

print("...value by setting via parameters with a 'where' function...\n")
#df2.loc[(df.Viable? == "Maybe") & (df.Base AP >0), 'Base AP'] == "Derp"
#print(df2)

df2.loc[(df2['Viable?'] == "Maybe") & (df2['Base AP'] == 0),df2['Base AP']] == "Derp"





print("=================== 12 ====================")

df = pd.DataFrame(dict(side=['A']*3+['B']*3, nominal = [1, -2, -2, 2, 6, -5]))
print(df)
df.loc[(df.side == 'B') & (df.nominal < 0), 'nominal'] = 1000
print(df) 








# SyntaxError: unexpected EOF while parsing = probably missing a parenthesis or the string is wrong somehow...








