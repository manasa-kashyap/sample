import matplotlib.pyplot as plt

# Get user input
try:
    numbers = input("Enter numbers separated by spaces: ")
    number_list = [int(num) for num in numbers.split()]
except ValueError:
    print("Please enter only integers.")
    exit()

# Plotting the histogram
plt.hist(number_list, bins=10, color='skyblue', edgecolor='black')

# Add labels and title
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Display the chart
plt.show()
