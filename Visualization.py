#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
mpl.rcParams['figure.dpi'] = 500
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("/Users/aviramavivi/PycharmProjects/proj1/venv/fixed_DF.csv", index_col=[0])


# In[64]:


sns.relplot(x=df["points"],y=df["minutes"], data=df,hue=df['position'],size=df['position'], sizes=(20, 100),style=df['won'])


# In[65]:


sns.barplot(x=df['position'], y=df['PIR'], hue=df['won'],data=df,ci=0,estimator=np.mean)


# In[66]:


ax=plt.axes(projection='3d')
X_data=df["games"]
Y_data=df["minutes"]
Z_data=df["PIR"]
    
plt.xlabel('Amount of Games')
plt.ylabel('Minutes')
ax.scatter3D(X_data,Y_data,Z_data,c=Z_data,depthshade=False)


# In[67]:


sns.violinplot(x=df['position'], y=df['GS'], data=df, hue=df['won'])


# In[68]:


new_df = df[['height','Fv','R.offensive','R.defensive']].corr()

sns.heatmap(new_df, annot=True, cmap='cividis')


# In[ ]:




