import seaborn as sns
import matplotlib.pyplot as plt
toys=['cars','bikes','balls','train']
counts=[5,3,7,2]
custom_colors=['green','blue','pink','yellow']
sns.barplot(x=toys,y=counts,palette=custom_colors)
plt.title("Toy Counts")
plt.xlabel("Toy Type")
plt.ylabel("count")
plt.show()
