#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 1. Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 2. Load the CSV file
df = pd.read_csv("Week-5-Student-Scores 1.csv")


# In[4]:


# 3. Basic info
print("Shape:", df.shape)
print("\nColumn Data Types:")
print(df.dtypes)


# In[5]:


# 4. Missing values per column
print("\nMissing Values per Column:")
print(df.isna().sum())


# In[6]:


# 5. Number of duplicates
print("\nNumber of duplicate rows:", df.duplicated().sum())


# In[7]:


# --- Diagnostics Table ---
diagnostics = pd.DataFrame({
    "Column": df.columns,
    "Data_Type": df.dtypes.values,
    "Missing_Values": df.isna().sum().values,
})
diagnostics.loc[len(diagnostics.index)] = ['TOTAL', '', diagnostics['Missing_Values'].sum()]
diagnostics


# In[8]:


before = len(df)
df = df.dropna()
after = len(df)
print(f"Dropped {before - after} rows with missing values.")


# In[9]:


# --- Diagnostics Table ---
diagnostics = pd.DataFrame({
    "Column": df.columns,
    "Data_Type": df.dtypes.values,
    "Missing_Values": df.isna().sum().values,
})
diagnostics.loc[len(diagnostics.index)] = ['TOTAL', '', diagnostics['Missing_Values'].sum()]
diagnostics


# In[10]:


# Select only numeric columns
numeric_df = df.select_dtypes(include='number')

# Compute summary stats
desc = numeric_df.describe(percentiles=[0.25, 0.5, 0.75]).T

# Rename columns for clarity
desc = desc.rename(columns={
    '25%': '25th_percentile',
    '50%': 'median',
    '75%': '75th_percentile'
})

# Keep only the requested columns
desc = desc[['mean', 'median', 'std', 'min', '25th_percentile', '75th_percentile', 'max']]
desc


# In[11]:


for col in ['Final_Score', 'Study_Hours_per_Week', 'Attendance_Rate']:
    plt.figure(figsize=(6,4))
    plt.hist(df[col], bins=15, edgecolor='black')
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()


# In[1]:


# Export the cleaned dataset
df.to_excel("Cleaned_Student_Data.xlsx", index=False)


# In[2]:


df.to_excel("Cleaned_Student_Data.xlsx", index=False)
print("✅ Cleaned dataset exported successfully to 'Cleaned_Student_Data.xlsx'")


# In[3]:


get_ipython().system('pip install openpyxl')


# In[4]:


df.to_excel("Cleaned_Student_Data.xlsx", index=False)


# In[ ]:




