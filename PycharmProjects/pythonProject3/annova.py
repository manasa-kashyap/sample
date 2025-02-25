import numpy as np
from scipy import stats

from ttest import p_value

region1=[135,130,125,140,135,128,132]
region2=[150,160,158,162,155,149,157]
region3=[180,175,172,180,178,176,174]

f_stat,p_value =stats.f_oneway(region1,region2,region3)

print("F-statistic:",f_stat)
print("p-value",p_value)

alpha=0.05
if p_value < alpha:
    print("at least one group has a significantly different mean")
else:
    print("there is no significant different mean")
