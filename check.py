#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
df = pd.read_csv("org_nendo_summary.csv")
df.set_index(['org_id','nendo'], inplace=True)
# ptはpivot_tableの略。組織を横持ちする
pt = df.unstack(level='org_id')
print(pt)


# In[ ]:


# 前年度との差分の閾値
THRESHOLD_LAST_NENDO_DIFF = 0.20

# 前年度との差分
last_nendo_diff_pt = abs(pt - pt.shift()).dropna()

print(last_nendo_diff_pt)

last_nendo_diff_df = last_nendo_diff_pt.stack(level='org_id').reset_index()

print(last_nendo_diff_df)

print(last_nendo_diff_df[last_nendo_diff_df['no_data_ratio'] >= THRESHOLD_LAST_NENDO_DIFF])


# In[ ]:




