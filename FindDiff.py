#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install datacompy


# In[3]:


import datacompy, pandas as pd


# In[4]:


d1 = pd.read_excel('C:/Users/abdullayevc/Desktop/eMANAT/test1.xlsx')


# In[5]:


d2 = pd.read_excel('C:/Users/abdullayevc/Desktop/eMANAT/test2.xlsx')


# In[10]:


compare = datacompy.Compare(
d1,
d2,
join_columns=['TransactionID'],  #You can also specify a list of columns eg ['policyID','statecode']
abs_tol=0, #Optional, defaults to 0
rel_tol=0, #Optional, defaults to 0
)


# In[13]:


print(compare.report())

