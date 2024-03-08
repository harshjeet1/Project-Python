#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df= pd.read_csv('E:/Dataset/IPL2022PlayerAuction_List_Sets-converted.csv',index_col= 'List Sr.No.')
df.head()


# In[3]:


df.info()


# In[4]:


df.shape


# In[5]:


df.describe()


# In[6]:


df.columns


# In[7]:


df.Country.unique()


# In[8]:


df.Country.value_counts()


# In[9]:


plt.figure(figsize=(20,10))
sns.countplot(df.Country,order = df.Country.value_counts().index)
plt.show()


# In[10]:


df.Specialism.value_counts()


# In[11]:


sns.countplot(df.Specialism,order = df.Specialism.value_counts().index)
plt.show()


# # Top overseas All Rounder

# In[12]:


df[(df.Specialism == 'ALL-ROUNDER' )& (df.Country != 'India')].sort_values(by=['Reserve Price Rs Lakh'],ascending=False).head(40)


# # Top Indian ALL-ROUNDER

# In[13]:


df[(df.Specialism == 'ALL-ROUNDER' )& (df.Country == 'India')].sort_values(by=['Reserve Price Rs Lakh'],ascending=False).head(30)


# # Top Overseas Bowler

# In[14]:


df[(df.Specialism == 'BOWLER')&(df.Country != 'India')].sort_values(by= 'Reserve Price Rs Lakh').head(40)


# # Top Indian Bowlers

# In[15]:


df[(df.Specialism == 'BOWLER')&(df.Country == 'India')].sort_values(by= 'Reserve Price Rs Lakh').head(40)


# # Top Overseas Batsman

# In[16]:


df[(df.Specialism == 'BATSMAN')&(df.Country != 'India')].sort_values(by= 'Reserve Price Rs Lakh').head(40)


# # Top Indian Batsman

# In[17]:


df[(df.Specialism == 'BATSMAN')&(df.Country == 'India')].sort_values(by= 'Reserve Price Rs Lakh').head(40)


# # Top Overseas Wicketkeeper

# In[18]:


df[(df.Specialism == 'WICKETKEEPER' )& (df.Country != 'India')].sort_values(by=['Reserve Price Rs Lakh'],ascending=False).head(20)


# # Top Indian Wicketkeeper

# In[19]:


df[(df.Specialism == 'WICKETKEEPER' )& (df.Country == 'India')].sort_values(by=['Reserve Price Rs Lakh'],ascending=False).head(20)


# # Most T20 Experience Overseas Player in this Auction

# In[20]:


df[df['T20 caps']== df['T20 caps'].max()]


# # Most T20 Experience Indian Player in this Auction

# In[21]:


df_in= df[df.Country == 'India']

df_in[df_in['T20 caps']== df_in['T20 caps'].max()]


# # Most IPL Experience Indian Player in this Auction

# In[22]:


df[df['IPL']== df['IPL'].max()]


# # Most IPL Experience Overseas Player in this Auction

# In[23]:


df_ov = df[df.Country != 'India']
df_ov[df_ov['IPL']== df_ov['IPL'].max()]


# # Oldest Overseas Player in this Auction

# In[27]:


df[df.Age==df.Age.max()]


# # Oldest Indian Player in this Auction

# In[28]:


df_in[df_in.Age==df_in.Age.max()]


# # Youngest Overseas Player in this Auction

# In[25]:


df[df.Age==df.Age.min()]


# # Youngest Indian Player in this Auction

# In[26]:


df_in[df_in.Age==df_in.Age.min()]


# In[ ]:




