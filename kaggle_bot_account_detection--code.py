#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


# In[2]:


df=pd.read_csv('D:\data sets\kaggle_bot_accounts.csv')


# ### Explore Data 

# In[3]:


df


# In[4]:


df.head(10)


# In[5]:


df.tail()


# In[6]:


df.describe()


# In[7]:


print("num of rows is -> ",df.shape[0])
print("num of columns is -> ",df.shape[1])


# In[8]:


df.info()


# In[9]:


df.count() 


# In[10]:


df.dtypes.value_counts()


# In[11]:


df.shape


# In[12]:


df.columns


# In[13]:


df['GENDER'].value_counts()


# In[14]:


con = df['REGISTRATION_LOCATION'].value_counts()
con


# In[15]:


con.max()


# ### Data Cleaning

# In[16]:


df.rename(columns={'Unnamed: 0':'Acc_Num '},inplace = True)


# In[17]:


df.isnull().sum()


# In[18]:


df.isna().sum().sum()


# In[19]:


df.replace([np.inf,-np.inf],np.nan , inplace = True )
df.replace(np.nan,'Emp_Cell',inplace=True)
df.replace(0,'Emp_Cell',inplace=True)
df


# In[20]:


df.fillna(method='ffill').fillna('xx')


# In[21]:


df.isnull().sum()


# In[22]:


df.dropna(subset=['EMAIL_ID'],inplace = True)
df


# In[23]:


print('the num of null mails as will be unknown cuts is ->',1321188-1243374)


# In[24]:


print('the perecentage of missing is ' , (77814/1321188)*100 )


# In[25]:


df.drop_duplicates(inplace = True)


# In[26]:


df=df.replace("", np.nan)


# In[27]:


df.dtypes


# In[28]:


pd.isna(df['NAME']).value_counts()


# ### Data Processing

# In[29]:


df.describe()


# In[30]:


df.replace('Emp_Cell',0,inplace=True)
df['ISBOT']=df['ISBOT'].astype(str)
df['TOTAL_VOTES_GAVE_NB']=df['TOTAL_VOTES_GAVE_NB'].astype(float)
df['REGISTRATION_LOCATION']=df['REGISTRATION_LOCATION'].astype(str)
argantina=df[df['REGISTRATION_LOCATION'] == 'Argentina'][['GENDER','ISBOT']][df['TOTAL_VOTES_GAVE_NB']>16.0]
Costa_Rica=df[df['REGISTRATION_LOCATION'] == 'Costa Rica'][['GENDER','ISBOT']][df['TOTAL_VOTES_GAVE_NB']>16.0]
argantina.head(20)


# In[31]:


ex1=df.groupby(['NAME'])[[
    'FOLLOWER_COUNT',
    'FOLLOWING_COUNT',
    'REGISTRATION_LOCATION']].mean()


# In[32]:


ex1.head(10)


# In[33]:


# the percentage of true \ false \ no ans at all .. due to 'isBot'
df['ISBOT'].value_counts()


# In[34]:


# total answers 
df['ISBOT'].value_counts().sum()


# In[35]:


"""
if ture
"""
if_true = (313217 / 1243374)*100
if_false = (856254 / 1243374)*100
if_no_ans = (73903 / 1243374) * 100 
print(if_true,"\\",if_false,"\\",if_no_ans)


# In[36]:


df


# ### Data Visulisation

# In[37]:


df.replace('Emp_Cell',0,inplace=True)
df.rename(columns={'Unnamed: 0':'Acc_Num '},inplace = True)
df['CODE_COUNT']=df['CODE_COUNT'].astype(float)
df['DATASET_COUNT']=df['DATASET_COUNT'].astype(float)
df['FOLLOWER_COUNT']=df['FOLLOWER_COUNT'].astype(float)
df['FOLLOWING_COUNT']=df['FOLLOWING_COUNT'].astype(float)
df['DISCUSSION_COUNT']=df['DISCUSSION_COUNT'].astype(float)
df['AVG_NB_READ_TIME_MIN']=df['AVG_NB_READ_TIME_MIN'].astype(float)
df['TOTAL_VOTES_GAVE_NB']=df['TOTAL_VOTES_GAVE_NB'].astype(float)
df['TOTAL_VOTES_GAVE_DS']=df['TOTAL_VOTES_GAVE_DS'].astype(float)
df.hist(figsize=(20,15))
plt.show()


# In[38]:


"""
most_follwed_accounts
"""
high = df['FOLLOWER_COUNT'].mean()
highest = df[df['FOLLOWER_COUNT']>high]
highest


# In[39]:


con.plot()
plt.show()


# In[40]:


"""
the intersection point that related to the (ISBOT) cloumn 
And declearing the percentage or the rolle of each value 
"""
if_true = (313217 / 1243374)*100
if_false = (856254 / 1243374)*100
if_no_ans = (73903 / 1243374) * 100 
# print(if_true,"\\",if_false,"\\",if_no_ans)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
x = if_true
y = if_false
z =if_no_ans
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z,
           linewidths=1, alpha=.8,
           edgecolor='k',
           s = 200,
           c=z)
plt.show()


# In[41]:


highest.describe()


# In[42]:


"""
The Highest 50 Country 
"""
h=df['REGISTRATION_LOCATION'].value_counts().head(50)
h


# In[43]:


"""
a graph that decleat the increasing of the bot accounts aspair the time 
"""
h.plot()
plt.show()


# In[44]:


df['IS_GLOGIN'].value_counts()


# In[45]:


"""
depending on each Country the results will be 
with the same fields of bot & male & if it logging or not 
"""

con_gender_bot = df.groupby('REGISTRATION_LOCATION')['IS_GLOGIN','GENDER','ISBOT'].value_counts().head(50)
con_gender_bot


# In[46]:


df.replace('Emp_Cell',0 , inplace = True)
sns.lineplot(x='TOTAL_VOTES_GAVE_NB' , y ='TOTAL_VOTES_GAVE_DS' , data=df)
plt.show()


# In[47]:


"""
 TOTAL_VOTES_GAVE_NB: The total number of votes the individual has given to notebooks.
 and if it male or fe male && bot or not 
 calc all cases and with recpect to all fields with all values 
"""
vots_gender_bot= df.groupby('TOTAL_VOTES_GAVE_NB')['IS_GLOGIN','GENDER','ISBOT'].value_counts().head(50)
vots_gender_bot


# In[48]:


"""
try to count all cases and maybe collecting
"""
df.groupby('REGISTRATION_LOCATION')['IS_GLOGIN','GENDER','ISBOT'].value_counts()


# In[49]:


"""
AVG_NB_READ_TIME_MIN: The average time spent reading notebooks in minutes.
the num of data sets that user has created before && depending on this u can judge which one is fake or not 
and coverd with the option the if it bot or not that will help to decide if it fake or not 
"""
df.groupby('NAME')['DATASET_COUNT','ISBOT','AVG_NB_READ_TIME_MIN'].value_counts()


# In[50]:


df.columns.tolist()


# In[51]:


import matplotlib.pyplot as plt
plt.scatter(con_gender_bot, vots_gender_bot,color='b' , linewidth = 1 , marker = '*' ,linestyle = 'dashed')
plt.xlabel('con_gender_bot - axis')
plt.ylabel('vots_gender_bot - axis')
plt.legend()
plt.title('the separation ')
plt.show()


# In[52]:


df=pd.read_csv('D:\data sets\kaggle_bot_accounts.csv')
plt.title("the relationship bettween vots_gender_bot & con_gender_bot ")
plt.plot(vots_gender_bot,con_gender_bot,'r.-'  )
plt.xticks(vots_gender_bot)
plt.yticks(con_gender_bot)
print(vots_gender_bot[::7])
print(con_gender_bot[::7])
# plt.show()


# In[53]:


for REGISTRATION_LOCATION in df :
    if REGISTRATION_LOCATION in ['Korea' , 'Afghanistan','Algeria']:
        plt.plot(df['TOTAL_VOTES_GAVE_NB'] , marker = '.')


# In[54]:


df['CODE_COUNT']=df['CODE_COUNT'].astype(float)
df['DATASET_COUNT']=df['DATASET_COUNT'].astype(float)


# In[55]:


"""
A Histogram that declear the relationship or the sides bettwen 
num of persons thet visits this note books which had been created by this user 
who are in this data set 
"""
plt.hist(df.CODE_COUNT , color = 'black' )
plt.xlabel('Num Of NoteBooks')
plt.ylabel('Num Of persons')
plt.title("The number of notebooks the individual has created")
plt.show()


# In[56]:


"""
ths piechart declear the relation & the precentage of the location that has the most accounts created in 
compared bettwern the biggest 4 countreies
"""
Argentina = df.loc[df['REGISTRATION_LOCATION'] == 'Argentina'].count()[0]
Korea = df.loc[df['REGISTRATION_LOCATION'] == 'Korea'].count()[0]
Costa_Rica = df.loc[df['REGISTRATION_LOCATION'] == 'Costa Rica'].count()[0]
Italy= df.loc[df['REGISTRATION_LOCATION'] == 'Italy'].count()[5]
labels = ['Argentina','Korea','Costa_Rica','Italy']
colors = ['b','r','g','y']
plt.pie([Argentina,Korea,Costa_Rica,Italy],labels=labels, colors=colors )
plt.title("a random sample from she contries to clear what i`m doing")
plt.show()


# In[57]:


"""
 this graph consumed that the relation bettwen the The total number 
 of votes the individual has given to notebooks.&
 The total number of votes the individual has given to datasets.
"""
sns.set_theme(style="darkgrid")

df['TOTAL_VOTES_GAVE_NB']=df['TOTAL_VOTES_GAVE_NB'].astype(float)
df['TOTAL_VOTES_GAVE_DS']=df['TOTAL_VOTES_GAVE_DS'].astype(float)

sns.relplot(
    data=df,
    x=df['TOTAL_VOTES_GAVE_NB'], y=df['TOTAL_VOTES_GAVE_DS'],kind = 'line'
)


# In[58]:


"""
a graph that detect which one is more fake or has biiger num of bots due to another 
"""
sns.relplot(data=df, x=df['GENDER'], y=df['ISBOT'] , kind = 'line')


# In[59]:


df.replace(0,'Emp_Cell',inplace=True)
df.replace(np.nan,'Emp_Cell',inplace=True)
df.replace("",'Emp_Cell',inplace=True)
df.rename(columns={'Unnamed: 0':'Acc_Num '},inplace = True)


# In[60]:


df


# In[61]:


# df.to_csv('kaggle_bot_account_detection_final.csv',encoding = 'UTF-8' ,index=False)

