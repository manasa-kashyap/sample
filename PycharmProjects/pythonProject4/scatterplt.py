import seaborn as sns
import matplotlib.pyplot as plt

x_position=[1,2,3,4,6]
y_position=[2,3,1,4,7]
sns.scatterplot(x=x_position,y=y_position,color='red')
plt.title("toy counts")
plt.xlabel("Toy Type")
plt.ylabel("count")
plt.show()
