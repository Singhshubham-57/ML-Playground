#!/usr/bin/env python
# coding: utf-8

# In[1]:


# So we have to clean our data set and keep the best variable whih will help us to analyis the data for the result


# ### so our objective is to find the most popular content on the social buzz platfoem. 

# ### we are using 3 data set to find out our objective , 
# ##### now we have to clean our data set and merge it as a one data set ,

# In[2]:


# we will import our 1st data set now , I m using jupyter notebook for the task.


# In[3]:


import pandas as pd
import numpy as np


# In[4]:


df = pd.read_csv('ReactionTypes.csv') 


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.rename(columns={'Type':'ReactionType'},inplace=True)


# In[8]:


df.head()


# In[9]:


#so lets chaeck for the null values in data set


# In[10]:


df.isnull().sum()


# In[11]:


print('--------------'*25)


# In[12]:


#so we have the new data set now with us
#lets work on content data set


# In[13]:


df2 = pd.read_csv('Content.csv')


# In[14]:


df2.head(10)


# In[15]:


df2.shape


# In[16]:


df2.isnull().sum()


# In[17]:


#so in url we have 199 null values lets clean that


# In[18]:


df3 = df2.drop(['URL'],axis=1)


# In[19]:


df3 = df3.drop(['User ID'],axis=1)


# In[20]:


df3.isnull().sum()


# In[21]:


df3.info()


# In[22]:


df3['Category'].replace('', )


# In[23]:


df3.head()


# In[24]:


df3.rename(columns={'Type':'ContentType'},inplace=True)


# In[25]:


df3.head(2)


# In[26]:


print('--------------'*25)


# In[27]:


#lets work on 3rd data set


# In[28]:


df0 = pd.read_csv('Reactions.csv')


# In[29]:


df0.head()


# In[30]:


df0.isnull().sum()


# In[31]:


df0.shape


# In[32]:


df1 = df0.drop(['User ID'],axis=1)


# In[33]:


df1.rename(columns={'Type':'ReactionType'},inplace=True)


# In[34]:


df1.head()


# In[35]:


df1.isnull().sum()


# In[36]:


df1.dropna(axis=1)


# In[37]:


df1.dropna(axis=0)


# In[38]:


df1.shape


# In[39]:


# so our clean data aere df , df3 , df0


# In[40]:


# df1 = reactions
# df3 = content type
# df = reaction type


# In[41]:


#lets merge the data set


# In[42]:


new_data  = pd.merge(df1,df3,on='Content ID')


# In[43]:


new_data.shape


# In[44]:


new_data.head()


# In[45]:


Fd = pd.merge(new_data,df,on='ReactionType')


# In[46]:


Fd.head()


# In[47]:


Fd.isnull().sum()


# In[48]:


Fd.columns


# In[49]:


Fd.to_csv('FinalDataset')


# In[50]:


Fd.to_excel('output.xlsx')


# In[51]:


print('---------------'*25)


# In[52]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[53]:


df = pd.read_csv('FinalDataset')


# In[54]:


df.info()


# In[55]:


df.head()


# In[56]:


df = df.drop(['Unnamed: 0_x'],axis=1)


# In[57]:


df = df.drop(['Unnamed: 0_y'],axis=1)


# In[58]:


df = df.drop(['Unnamed: 0'],axis=1)


# In[59]:


df = df.drop(['Unnamed: 0.1'],axis=1)


# In[60]:


df.head()


# In[61]:


#so we have removed the unwanted columns 


# In[62]:


df.iloc[:,-3] = df.iloc[:,-3].str.replace('"', '')


# In[63]:


df['Category'].unique()


# In[64]:


df.iloc[:,-3] = df.iloc[:,-3].str.capitalize()


# In[65]:


df.head()


# In[66]:


df.to_csv('Finalset')


# In[67]:


df.head()


# In[68]:


df.groupby(['Category'])['Score'].agg('sum')


# In[69]:


x =pd.DataFrame(df.groupby(['Category'])['Score'].agg('sum'))
 


# In[70]:


x.plot(kind='bar', title='Score', ylabel='Score',
         xlabel='Category', figsize=(6, 5))


# In[ ]:





# In[71]:


plt.plot(x)
plt.xticks(rotation=90)
plt.grid()
plt.show()


# #### So coming to the conlusion for my analysis for top 5 catogery are
# #### 1) Animals
# #### 2) Science 
# #### 3) Healthy Eating 
# #### 4) Technology 
# #### 5) Food

# In[72]:


#Lets plot pie chart for catoegry wise 


# In[74]:


#lets see unique values 
df['Category'].unique()


# In[75]:


reaction = df.groupby(['Category'])['ReactionType'].agg('value_counts')


# In[76]:


reaction


# In[77]:


#so our most popular catogary is aniamls lets check how many recation anials have 


# In[78]:


reaction['Animals'].sum()


# In[79]:


x =reaction['Animals']


# In[80]:


x


# In[81]:


y =reaction['Animals'].value_counts()


# In[82]:


plt.plot(x)
plt.xticks(rotation=90)
plt.grid()
plt.show()


# In[83]:


x.plot(kind='bar', title='Reaction', ylabel='value_counts',
         xlabel='ReactionType', figsize=(6, 5))


# In[84]:


df.head()


# In[88]:


df['month'] = pd.DatetimeIndex(df['Datetime']).month


# In[89]:


df.head()


# In[98]:


df.groupby(['month']).count()


# In[101]:


df.groupby(['month'])['Content ID'].agg('count')


# In[106]:


x = df.groupby(['month'])['Content ID'].agg('count')
plt.plot(x)
plt.xticks(df['month'],rotation=90)
plt.grid()
plt.show()


# In[ ]:




