# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:04:58 2024

@author: Jose M. de Miguel
"""
import numpy as np
import matplotlib.pyplot as plt

# Constants
Sin = 1
# D = 1 entonces D < mu(si)
# D = 1.5 entonces D = mu(si)
# D = 2 entonces D > mu(si)
D = 2
a = 1
muMax = 3

# Function to calculate mu
def mu(s):
    return (muMax * s) / (s + a)

# Define your functions f1(s, x) and f2(s, x)
def f1(s, x):
    return (Sin - s) * D - mu(s) * x

def f2(s, x):
    return -D * x + mu(s) * x

# Define additional functions
def x_func(s):
    return (D * (Sin - s)) / mu(s)

s_func = (D * a) / (muMax - D)


# Define the grid
s = np.linspace(0, 2, 11)
x = np.linspace(0, 2, 11)
S, X = np.meshgrid(s, x)

# Calculate the vector components using the functions
U = f1(S, X)
V = f2(S, X)

s_values = np.linspace(0, 2, 100)
x_values = x_func(s_values)


# Plot the vector field with shorter vectors and additional functions
fig, ax = plt.subplots()
ax.quiver(S, X, U, V, scale=10, color='blue', alpha=0.6)  # Adjust the scale parameter
ax.plot(s_values, x_values, color='red')
ax.plot([s_func] * len(x), x, color='green')  # Plot vertical line
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(color='gray', linestyle='--', linewidth=0.5)
ax.set_xlabel('s(t)')
ax.set_ylabel('x(t)')
ax.set_title('Plano de fases')
ax.legend()
ax.set_ylim(0, 2)  # Limit vertical axis
plt.show()
