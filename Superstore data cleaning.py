#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("Superstore_Dataset.csv",encoding='ANSI')


# In[4]:


df


# In[5]:


df.info()


# In[6]:


df.isnull()


# In[7]:


df.dropna(inplace=True)


# In[8]:


df


# In[9]:


df.duplicated()


# In[10]:


df.drop_duplicates()


# In[ ]:




