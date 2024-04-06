# Practical 9: Mini Project - Implementation using above Data Structure
# Name: Shivam Maisuriya
# Enrollment No: 202203103510303
# Batch:B.Tech CSE
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate random data
def generate_data(size=50):
    return np.random.rand(size)

# Function to perform bubble sort
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                yield data

# Function to update the plot
def update(frame):
    ax.clear()
    ax.bar(range(len(data)), data, color='b')

# Generate random data
data = generate_data()

# Create a figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, len(data))
ax.set_ylim(0, 1)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=bubble_sort(data), blit=False, interval=50)

# Show the plot
plt.show()

