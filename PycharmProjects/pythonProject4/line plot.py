import matplotlib.pyplot as plt

# Sample data (you can replace with your own)
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 14, 11]

# Create the line plot
plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Sales Over Days')

# Add labels and title
plt.title('Line Plot Example')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
