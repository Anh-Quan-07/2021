#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ĐỒ ÁN KẾT THÚC HỌC PHẦN
THỐNG KÊ MÔ TẢ VS TỆP DỮ LIỆU Inc_Exp_Data.csv


# In[28]:


import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
from matplotlib import pyplot as plt
import statsmodels.api as sm


# In[29]:


df = pd.read_csv('Inc_Exp_Data .csv')


# In[30]:


df.sample(20)


# In[31]:


#Kiểu định tính
dinh_luong = {}
columns_dinh_luong = ['Mthly_HH_Income', 'Mthly_HH_Expense', 'Emi_or_Rent_Amt', 'Annual_HH_Income']
for column in columns_dinh_luong:
    print(column)
    mo_ta = df[column].describe()
    print(mo_ta)
    dinh_luong[column] = df[column]
    print('')


# In[32]:


#Kiểu định tính
dinh_tinh = {}
columns_dinh_tinh = ['No_of_Fly_Members', 'Highest_Qualified_Member', 'No_of_Earning_Members']
for column in columns_dinh_tinh:
    print(column)
    dinh_tinh[column] = df[column]
    print('')


# In[33]:


df['No_of_Fly_Members'].value_counts()


# In[34]:


df['No_of_Earning_Members'].value_counts()


# In[35]:


df['Highest_Qualified_Member'].describe()


# In[36]:


#Vẽ Biểu Đồ
data_dinh_luong = pd.DataFrame(dinh_luong)
data_dinh_tinh = pd.DataFrame(dinh_tinh)


# In[37]:


#Sử dụng Bar Chart với kiểu dữ liệu định tính 

for column in data_dinh_tinh.columns:
    p = {}
    so_luong = []
    #print(data_dinh_tinh[column].value_counts())
    dem_data = data_dinh_tinh[column].value_counts()
    trinh_do = dem_data.index
    for i in dem_data:
        so_luong.append(i)
    p = {'trinh_do':trinh_do, 'so_luong':so_luong}
    data = pd.DataFrame(p)
    plt.title(column)
    sns.barplot(y = 'trinh_do', x= 'so_luong', data = data)
    plt.show()


# In[38]:


data_dinh_tinh_2 = df[['No_of_Fly_Members','No_of_Earning_Members']]

for column in data_dinh_tinh_2.columns:
    p = {}
    so_luong = []
    levels = []
    #print(data_dinh_tinh[column].value_counts())
    dem_data = data_dinh_tinh_2[column].value_counts()
    levels_0 = dem_data.index
    for level in levels_0:
        levels.append(str(level))
    for i in dem_data:
        so_luong.append(i)
    p = {'levels':levels, 'so_luong':so_luong}
    data = pd.DataFrame(p)
    plt.title(column)
    sns.barplot(y = 'levels', x = 'so_luong', data = data)
    plt.show()


# In[39]:


#VẼ HISTOGRAM ĐỐI VỚI KIỂU DỮ LIỆU ĐỊNH TÍNH
for column in data_dinh_luong.columns:
    data = data_dinh_luong[column]
    # kiem tra data co chuan hay khong?
    mean = np.mean(data)
    # ddof = 1 :: hiệu chỉnh
    std = np.std(data,ddof=1)
    domain = np.linspace(np.min(data),np.max(data))
    plt.plot(domain, stats.norm.pdf(domain, mean, std))
    # density = True :: chuẩn hóa dữ liệu vè normal
    plt.hist(data, edgecolor='black', density = True)
    plt.title(column)
    plt.show()


# In[ ]:




