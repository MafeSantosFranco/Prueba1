#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt

import lasio

las = lasio.read("data_01JAN2014_18JAN2015.las")


# In[2]:


las.keys()


# In[3]:


df = las.df()


# In[4]:


import seaborn as sb


# In[5]:


df.columns


# In[6]:


df.head()


# In[7]:


df.columns = ['Dia', 'Mes', 'Año', 'Tot depth', 'Bit depth',
       'ROP', 'HK Hght', 'WOH', 'WOB', 'FLWpmps',
       'SPP', 'UNKNOWN:13', 'T Revol', 'UNKNOWN:15']


# In[8]:


df.columns


# In[9]:


df2 = df.rename(columns={'UNKNOWN:13':'TORQUE',
                        'UNKNOWN:15':'T GAS main'},
               inplace=True)


# In[10]:


df.columns


# In[11]:


df.head()


# In[12]:


df2 = pd.DataFrame(df,columns=['Dia', 'Mes', 'Año', 'Tot depth', 'Bit depth', 'ROP', 'HK Hght', 'WOH',
       'WOB', 'FLWpmps', 'SPP', 'TORQUE', 'T Revol', 'T GAS main'])


# In[13]:


df2['Fecha']=df2.apply(lambda x:'%s%s%s' % (x['Dia'],x['Mes'],x['Año']),axis=1)


# In[14]:


df3 = pd.DataFrame(df2,columns=['Fecha', 'Tot depth', 'Bit depth', 'ROP', 'HK Hght', 'WOH',
       'WOB', 'FLWpmps', 'SPP', 'TORQUE', 'T Revol', 'T GAS main'])


# In[15]:


df3.head()


# In[16]:


a = range(0,1554599,10)


# In[17]:


df3.insert(0, "TIME", a, allow_duplicates=False)
print(df3)


# In[18]:


a = range(0,1554610,10)


# In[19]:


df3.insert(0, "TIME", a, allow_duplicates=False)
print(df3)


# In[20]:


df3.head()


# In[ ]:




