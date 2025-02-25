import numpy as np
from scipy import stats
# sample data
class1_scores=[760,82,85,90,880,78,100]
class2_scores=[880,91,95,900,92,95,900]
# perform independent t-test
t_stat, p_value=stats.ttest_ind(class1_scores,class2_scores)

print("T-statistic:",t_stat)
print("p-value",p_value)

if p_value < 0.05:
  print("significant difference found between the two classes")
else:
  print("no significant difference between the two classes")
