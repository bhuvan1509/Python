#!/usr/bin/env python
# coding: utf-8

# # Comprehensive Analysis of Vehicle Repair Trends and Costs

# In[43]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_name = 'DA -Task 2..xlsx'
df = pd.read_excel(file_name)

# Display the total number of rows (excluding the header)
print("Total rows (excluding header):", len(df))

# Display the column headers
print("Column Headers:", df.columns.tolist())

# Display summary statistics
print(df.describe())

# Display the first few rows of the DataFrame
print(df.head())



# # Visualizations

# ## Important KPIs we are analysing here are:
#     
# Average Kilometers Driven by Vehicle Platform
# 
# Vehicle Repair Age Distribution
# 
# Total Repair Cost Distribution
# 
# Repair Costs by Platform - Box plot
# 
# Count of Repairs by Platform
# 
#  Average Repair Costs by Dealer
# 
# Distribution of Repair Costs for Top Dealers (Scatter Plot)
# 
# 
# 

# # 1. Average KM by Platform (Horizontal Bar Chart)

# In[35]:


plt.figure(figsize=(12, 8))
average_km_by_platform = df.groupby('PLATFORM')['KM'].mean().sort_values()
bars = average_km_by_platform.plot(kind='barh', color='gray', edgecolor='black')
plt.title('Average Kilometers by Vehicle Platform')
plt.xlabel('Average Kilometers Driven')
plt.ylabel('Vehicle Platform')
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Adding red trend line
plt.plot(average_km_by_platform.values, range(len(average_km_by_platform)), 'ro-', linewidth=2.5)

plt.show()


# # 2. Repair Age Distribution

# In[36]:


plt.figure(figsize=(10, 6))
sns.histplot(df['REPAIR_AGE'], kde=True, color='gray',edgecolor='black')
plt.title('Distribution of Repair Age')
plt.xlabel('Repair Age (years)')
plt.ylabel('Frequency')
plt.show()



# # 3. Total Repair Cost Distribution
# 

# In[37]:


plt.figure(figsize=(10, 6))
sns.histplot(df['TOTALCOST'], kde=True, color='blue')
plt.title('Distribution of Total Repair Costs')
plt.xlabel('Total Cost')
plt.ylabel('Frequency')
plt.show()


# # 4. Repair Costs by Platform - Box plot

# In[38]:


plt.figure(figsize=(12, 8))
sns.boxplot(x='PLATFORM', y='TOTALCOST', data=df)
plt.title('Repair Costs by Platform')
plt.xlabel('Platform')
plt.ylabel('Total Cost')
plt.xticks(rotation=45)
plt.show()


# # 5. Count of Repairs by Platform

# In[42]:


plt.figure(figsize=(12, 8))
sns.countplot(y='PLATFORM', data=df, color='gray', edgecolor='black')
plt.title('Count of Repairs by Platform')
plt.xlabel('Count')
plt.ylabel('Platform')
plt.xticks(rotation=0)
plt.show()


# # 6. Average Repair Costs by Dealer

# In[57]:


plt.figure(figsize=(14, 8))
avg_repair_cost_by_dealer = df.groupby('DEALER_NAME')['TOTALCOST'].mean().sort_values(ascending=False).head(10)  # Top 10 dealers
sns.barplot(y=avg_repair_cost_by_dealer.index, x=avg_repair_cost_by_dealer.values, color = 'grey', edgecolor = 'black')
plt.title('Top 10 Dealers by Average Repair Cost')
plt.xlabel('Average Repair Cost')
plt.ylabel('Dealer Name')
plt.show()



# # 7.Distribution of Repair Costs for Top Dealers (Scatter Plot)

# In[56]:


plt.figure(figsize=(14, 8))
top_dealers = df['DEALER_NAME'].value_counts().head(5).index  # Top 5 dealers

# Scatter plot
for dealer in top_dealers:
    dealer_data = df[df['DEALER_NAME'] == dealer]
    plt.scatter(dealer_data['TOTALCOST'], [dealer] * len(dealer_data), label=dealer, alpha=0.7)

plt.title('Distribution of Repair Costs for Top 5 Dealers')
plt.xlabel('Total Repair Cost')
plt.ylabel('Dealer Name')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


# In[ ]:




