import numpy as np
from tabulate import tabulate


# Given data
x = np.array([0.20, 0.22, 0.24, 0.26, 0.28, 0.30])
y = np.array([1.6596, 1.6698, 1.6804, 1.6912, 1.7024, 1.7139])

# Function to compute forward differences
def forward_differences(y):
    n = len(y)
    coef = np.zeros((n, n))
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = coef[i + 1][j - 1] - coef[i][j - 1]
    return coef

# Function to compute backward differences
def backward_differences(y):
    n = len(y)
    coef = np.zeros((n, n))
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[n - 1 - i][j] = coef[n - 1 - i][j - 1] - coef[n - 2 - i][j - 1]
    return coef

# Compute forward difference table
forward_diff = forward_differences(y)
print("Forward Difference Table:")
print(tabulate(forward_diff, headers=[f'Δ^{i}' for i in range(len(y))], showindex=[f'x={x[i]}' for i in range(len(x))], tablefmt='grid'))

# Compute backward difference table
backward_diff = backward_differences(y)
print("\nBackward Difference Table:")
print(tabulate(backward_diff, headers=[f'∇^{i}' for i in range(len(y))], showindex=[f'x={x[i]}' for i in range(len(x))], tablefmt='grid'))

# Newton's forward interpolation formula (for f(0.21))
h = x[1] - x[0]
u = (0.21 - x[0]) / h
p = 1
result_forward = y[0]
for i in range(1, len(x)):
    p *= (u - (i - 1)) / i
    result_forward += p * forward_diff[0][i]
print(f"\nEstimated f(0.21) using Newton's forward interpolation: {result_forward:.4f}")

# Newton's backward interpolation formula (for f(0.29))
u = (0.29 - x[-1]) / h
p = 1
result_backward = y[-1]
for i in range(1, len(x)):
    p *= (u + i - 1) / i
    result_backward += p * backward_diff[-1][i]
print(f"Estimated f(0.29) using Newton's backward interpolation: {result_backward:.4f}")