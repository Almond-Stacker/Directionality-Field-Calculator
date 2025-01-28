

# import numpy as np
# import matplotlib.pyplot as plt

# def emample_function(x ,y):
#     return x - y

# def calculate_n_points(function, distance_between_points, min_x, max_x, min_y, max_y):
#     x_set = np.linspace(min_x, max_x, distance_between_points)
#     y_set = np.linespace(min_y, max_y, distance_between_points)
#     X, Y = np.meshgrid(x_set, y_set) 

#     # Calculate the slopes
# U = 1
# V = f(X, Y)

# # Normalize the vectors
# N = np.sqrt(U**2 + V**2)
# U = U / N
# V = V / N

# # Plot the direction field
# plt.quiver(X, Y, U, V, color='r')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Direction Field')
# plt.grid(True)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x, y) = dy/dx
def f(x, y):
    return x - y  # Example function

# Generate a grid of points
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# Calculate the slopes
U = 1
V = f(X, Y)

# Normalize the vectors
N = np.sqrt(U**2 + V**2)
U = U / N
V = V / N

# Plot the direction field
plt.quiver(X, Y, U, V, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Direction Field')
plt.grid(True)
plt.show()