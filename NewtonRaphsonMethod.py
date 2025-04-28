import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivative
def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

# Initial guess
x0 = 1.0
iterations = [x0]
for _ in range(4):  # 4 steps of Newton-Raphson
    x1 = x0 - f(x0) / df(x0)
    iterations.append(x1)
    x0 = x1

# Plot settings
x_vals = np.linspace(0.5, 2.5, 400)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = x³ - x - 2', color='blue')
plt.axhline(0, color='black', linewidth=0.5)

# Plot tangents
for i in range(len(iterations) - 1):
    x = iterations[i]
    y = f(x)
    slope = df(x)
    tangent_x = np.linspace(x - 0.5, x + 0.5, 100)
    tangent_y = slope * (tangent_x - x) + y
    plt.plot(tangent_x, tangent_y, '--', label=f'Tangent at x={x:.4f}', alpha=0.7)
    plt.plot(x, y, 'ro')  # Point on the curve
    plt.plot(iterations[i+1], 0, 'go')  # Next root approximation (intersection with x-axis)

plt.title('Newton-Raphson Method: Tangents Converging to Root')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()