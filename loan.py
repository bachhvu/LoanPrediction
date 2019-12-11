# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:25:18 2019

@author: Bach-PC
"""

import pandas as pd
import numpy as np
import matplotlib as plt

pd.set_option('display.max_columns', None)

#Reading the dataset in a dataframe using Pandas
df = pd.read_csv('C:/Users/Admin/Downloads/loan_train.csv') 

#printing first 10 rows of dataset
df.head(10)

#get summary of numerical variables
df.describe()

df['Property_Area'].value_counts()

df['ApplicantIncome'].hist(bins=50)

temp1 = df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
print ('Frequency Table for Credit History:') 
print (temp1)

print ('\nProbility of getting loan for each Credit History class:')
print (temp2)

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121)
ax1.set_xlabel('Credit_History')
ax1.set_ylabel('Count of Applicants')
ax1.set_title("Applicants by Credit_History")

fig = plt.figure(figsize=(8,4))
ax2 = fig.add_subplot(121)
ax2.set_xlabel('Credit_History')
ax2.set_ylabel('Probability of getting loan')
ax2.set_title("Probability of getting loan by credit history")

temp1.plot(kind='bar')
temp2.plot(kind = 'bar')