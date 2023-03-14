#!/usr/bin/env python
# coding: utf-8

# # Welcome to Covid19 Data Analysis Notebook
# ------------------------------------------

# ### Let's Import the modules 

# In[27]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# ## Task 2 

# ### Task 2.1: importing covid19 dataset
# importing "Covid19_Confirmed_dataset.csv" from "./Dataset" folder. 
# 

# In[28]:


df=pd.read_csv("C:/Users/DELL/Desktop/covid19_Confirmed_dataset.csv")
df.head()


# #### Let's check the shape of the dataframe

# In[29]:


df.shape


# ### Task 2.2: Delete the useless columns

# In[30]:


df.drop(["Lat","Long"],axis=1,inplace=True)


# In[31]:


df.head()


# ### Task 2.3: Aggregating the rows by the country

# In[32]:


aggregating=df.groupby("Country/Region").sum()


# In[33]:


aggregating.head()


# In[34]:


aggregating.shape


# ### Task 2.4: Visualizing data related to a country for example China
# visualization always helps for better understanding of our data.

# In[35]:


aggregating.loc["China"].plot()
aggregating.loc["Italy"].plot()
aggregating.loc["Spain"].plot()
plt.legend()


# ### Task3: Calculating a good measure 
# we need to find a good measure reperestend as a number, describing the spread of the virus in a country. 

# In[36]:


aggregating.loc['China'].plot()


# In[37]:


aggregating.loc['China'][:3].plot()


# ### task 3.1: caculating the first derivative of the curve

# In[38]:


aggregating.loc['China'].diff().plot()


# ### task 3.2: find maxmimum infection rate for China

# In[39]:


aggregating.loc['China'].diff().max()


# In[40]:


aggregating.loc['Italy'].diff().max()


# In[41]:


aggregating.loc['Spain'].diff().max()


# ### Task 3.3: find maximum infection rate for all of the countries. 

# In[42]:


countries=list(aggregating.index)
max_infection_rates=[]
for c in countries:
    max_infection_rates.append(aggregating.loc[c].diff().max())
aggregating["max_infection_rates"]=max_infection_rates


# In[43]:


aggregating.head()


# ### Task 3.4: create a new dataframe with only needed column 

# In[44]:


data=pd.DataFrame(aggregating["max_infection_rates"])


# In[45]:


data.head()


# ### Task4: 
# - Importing the WorldHappinessReport.csv dataset
# - selecting needed columns for our analysis 
# - join the datasets 
# - calculate the correlations as the result of our analysis

# ### Task 4.1 : importing the dataset

# In[46]:


happiness=pd.read_csv("C:/Users/DELL/Desktop/worldwide_happiness_report.csv")


# In[47]:


happiness.head()


# ### Task 4.2: let's drop the useless columns 

# In[48]:


cols=["Overall rank","Score","Generosity","Perceptions of corruption"]


# In[49]:


happiness.drop(cols,axis=1,inplace=True)
happiness.head()


# ### Task 4.3: changing the indices of the dataframe

# In[50]:


happiness.set_index("Country or region",inplace=True)
happiness.head()


# ### Task4.4: now let's join two dataset we have prepared  

# #### Corona Dataset :

# In[51]:


data.head()


# #### wolrd happiness report Dataset :

# In[52]:


happiness.head()


# In[53]:


final=data.join(happiness,how="inner")
final.head()


# ### Task 4.5: correlation matrix 

# In[54]:


final.corr()


# ### Task 5: Visualization of the results
# our Analysis is not finished unless we visualize the results in terms figures and graphs so that everyone can understand what you get out of our analysis

# In[55]:


final.head()


# ### Task 5.1: Plotting GDP vs maximum Infection rate

# In[56]:


x=final["GDP per capita"]
y=final["max_infection_rates"]
sns.scatterplot(x,np.log(y))


# In[57]:


sns.regplot(x,np.log(y))


# ### Task 5.2: Plotting Social support vs maximum Infection rate

# In[58]:


x=final["Social support"]
y=final["max_infection_rates"]
sns.scatterplot(x,np.log(y))


# In[59]:


sns.regplot(x,np.log(y))


# ### Task 5.3: Plotting Healthy life expectancy vs maximum Infection rate

# In[60]:


x=final["Healthy life expectancy"]
y=final["max_infection_rates"]
sns.scatterplot(x,np.log(y))


# In[61]:


sns.regplot(x,np.log(y))


# ### Task 5.4: Plotting Freedom to make life choices vs maximum Infection rate

# In[62]:


x=final["Freedom to make life choices"]
y=final["max_infection_rates"]
sns.scatterplot(x,np.log(y))


# In[63]:


sns.regplot(x,np.log(y))


# In[ ]:





# In[ ]:




