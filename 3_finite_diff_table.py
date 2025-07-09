from math import floor, exp
from tabulate import tabulate

#################
#control parameters
a = -1
b =  1
h = 0.1
###################

steps = floor((b-a)/h)
x_vals = [round(a + i * h, b) for i in range(steps+1)]
fx_vals = [exp(x) for x in x_vals]

# Initialize table with zeroth differences (f(x))
table = [fx_vals]

# Generate higher order differences
for order in range(1, len(x_vals)):
    prev = table[-1]
    diff = [round(prev[i+1] - prev[i], 6) for i in range(len(prev) - 1)]
    table.append(diff)

# Format for printing
headers = ["x", "f(x)"] + [f"Δ^{i}" for i in range(1, len(table))]
rows = []

for i in range(len(x_vals)):
    row = [x_vals[i]]
    for col in table:
        row.append(col[i] if i < len(col) else "")
    rows.append(row)

# Print table
print(tabulate(rows, headers=headers, tablefmt="grid"))
