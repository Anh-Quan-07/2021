#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ĐỒ ÁN KẾT THÚC HỌC PHẦN
THỐNG KÊ SUY DIỄN VS TỆP DỮ LIỆU Diet_R.csv


# In[5]:


import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
from matplotlib import pyplot as plt
import statsmodels.api as sm


# In[6]:


df = pd.read_csv('Diet_R .csv')


# In[10]:


print(df.sample(15))


# In[ ]:


TÍNH CÂN NẶNG GIẢM


# In[11]:


df['losingweight'] = df['pre.weight'] - df['weight6weeks']


# In[12]:


df_diet_losing = df[['Diet','losingweight']].copy()


# In[13]:


df_diet_losing


# In[14]:


SỰ KHÁC NHAU VỀ HIỆU QUẢ CỦA CÁC PHƯƠNG PHÁP GIẢM CÂN

Phát biểu giải thuyết thống kê

H0: không có sự khác biệt về hiệu quả giảm cân giữa 3 phương pháp
H1: có ít nhất hai kiểu phương pháp khác nhau về hiệu quả giảm cân


# In[15]:


sns.boxplot(x='Diet',y='losingweight',data = df_diet_losing, color='green')
sns.swarmplot(x='Diet',y='losingweight', data = df_diet_losing, color='orange')
plt.show()


# In[16]:


from statsmodels.formula.api import ols
import statsmodels.api as sm


# In[17]:


model = ols('losingweight ~ C(Diet)', data=df_diet_losing).fit()
anova_table = sm.stats.anova_lm(model, typ=2)


# In[18]:


anova_table


# In[19]:


def results(p, alpha=0.05):
    cols=['f_score', 'p_value', 'KetLuan']
    if p['p_value'] < alpha:
        p['KetLuan'] = f"Chấp nhận H1 với mức ý nghĩa {alpha}"
    if p['p_value'] >= alpha:
        p['KetLuan'] = f"Chấp nhận H0 với mức ý nghĩa {alpha}"
    df = pd.DataFrame(p, index=[''])
    return df[cols]


# In[20]:


p = {}
p['f_score'] = anova_table['F'][0]
p['p_value'] = anova_table['PR(>F)'][0]
results(p)


# In[21]:


Kiểm tra hậu nghiệm 


# In[22]:


from statsmodels.stats.multicomp import pairwise_tukeyhsd


# In[23]:


tukey = pairwise_tukeyhsd(endog=df_diet_losing['losingweight'],
                         groups=df_diet_losing['Diet'],
                         alpha=0.05)


# In[24]:


tukey.summary()


# In[25]:


Kiểm tra các điều kiện cho kiểm định Anova


# In[26]:


fig, ax = plt.subplots(1,2)
sm.qqplot(model.resid,line='s', ax=ax[0])
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Residuals")

plt.hist(model.resid, bins='auto', histtype='bar', ec='k')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()


# In[27]:


p_v = stats.shapiro(model.resid)[1]


# In[28]:


Kiểm tra sự phân phối chuẩn


# In[29]:


print('''Phát biểu giả thiết thống kê:
    H0: Mẫu tuân theo phân phối chuẩn
    H1: Mẫu khống tuân theo phân phối chuẩn''')
if p_v > 0.05:
    print(f'Không có bằng chứng thống kê để bác bỏ giả thiết H0. Điều này ngụ ý Mẫu tuân theo phân phối chuẩn')
else:
    print(f'Có bằng chứng thống kê để bác bỏ giả thiết H0. Điều này ngụ ý Mẫu không tuân theo phân phối chuẩn (H1)')


# In[30]:


df_gen_losingweight = df[['gender','losingweight']].copy()


# In[31]:


df_gen_losingweight = df_gen_losingweight.replace(r'^\s*$', np.nan, regex=True)


# In[32]:


df_gen_losingweight = df_gen_losingweight.dropna()


# In[33]:


df_gen_losingweight


# In[34]:


SỰ KHÁC NHAU VỀ HIỆU QUẢ GIẢM CÂN VỚI CÁC GIỚI TÍNH KHÁC NHAU

Phát biểu giải thuyết thống kê

H0: không có sự khác biệt về hiệu quả giảm cân đối với các giới tính khác nhau
H1: Các giới khác nhau về hiệu quả giảm cân


# In[35]:


sns.boxplot(x='gender',y='losingweight',data = df_gen_losingweight, color='green')
sns.swarmplot(x='gender',y='losingweight', data = df_gen_losingweight, color='orange')
plt.show()


# In[36]:


model_2 = ols('losingweight ~ C(gender)', data=df_gen_losingweight).fit()
anova_table = sm.stats.anova_lm(model_2, typ=2)


# In[37]:


anova_table


# In[38]:


p = {}
p['f_score'] = anova_table['F'][0]
p['p_value'] = anova_table['PR(>F)'][0]
results(p)


# In[39]:


Không cần tiến hành kiểm tra hậu nghiệm

Kiểm tra các điều kiện cho kiểm định Anova


# In[40]:


fig, ax = plt.subplots(1,2)
sm.qqplot(model_2.resid,line='s', ax=ax[0])
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Residuals")

plt.hist(model_2.resid, bins='auto', histtype='bar', ec='k')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()


# In[41]:


p_v = stats.shapiro(model_2.resid)[1]


# In[42]:


print('''Phát biểu giả thiết thống kê:
    H0: Mẫu tuân theo phân phối chuẩn
    H1: Mẫu khống tuân theo phân phối chuẩn''')
if p_v > 0.05:
    print(f'Không có bằng chứng thống kê để bác bỏ giả thiết H0. Điều này ngụ ý Mẫu tuân theo phân phối chuẩn')
else:
    print(f'Có bằng chứng thống kê để bác bỏ giả thiết H0. Điều này ngụ ý Mẫu không tuân theo phân phối chuẩn (H1)')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




