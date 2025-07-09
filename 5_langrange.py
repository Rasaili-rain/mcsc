from tabulate import tabulate

# Given data
x = [0, 1, 3, 4, 5]
y = [0, 1, 81, 256, 625]

# Display the data table
table = {"x": x, "y": y}
print("Given Data:")
print(tabulate(table, headers="keys", tablefmt="grid"))

# Lagrange's interpolation formula
def lagrange_interpolation(x, y, x_val):
    result = 0
    n = len(x)
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_val - x[j]) / (x[i] - x[j])
        result += term
    return result

# Estimate y(2)
x_val = 2
y_2 = lagrange_interpolation(x, y, x_val)
print(f"\nEstimated y(2) using Lagrange's interpolation: {y_2:.4f}")