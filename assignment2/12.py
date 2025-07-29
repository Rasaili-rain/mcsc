import os
import numpy as np
import matplotlib.pyplot as plt

def exponential_least_squares(x_data, y_data):
    # Transform y = ae^(bx) to ln(y) = ln(a) + bx
    ln_y = np.log(y_data)
    
    n = len(x_data)
    sum_x = np.sum(x_data)
    sum_ln_y = np.sum(ln_y)
    sum_x2 = np.sum(x_data**2)
    sum_x_ln_y = np.sum(x_data * ln_y)
    
    A = np.array([[n, sum_x],
                  [sum_x, sum_x2]])
    B = np.array([sum_ln_y, sum_x_ln_y])
    
    print("Normal equations for ln(y) = ln(a) + bx:")
    print(f"{n}*ln(a) + {sum_x}*b = {sum_ln_y:.3f}")
    print(f"{sum_x}*ln(a) + {sum_x2}*b = {sum_x_ln_y:.3f}")
    
    coefficients = np.linalg.solve(A, B)
    ln_a, b = coefficients
    a = np.exp(ln_a)
    
    return a, b

def plot_fit(x_data, y_data, a, b):
    plt.figure(figsize=(10, 6))
    
    plt.scatter(x_data, y_data, color='red', s=80, zorder=5, 
                label='Data Points', edgecolors='black', linewidth=1)
    
    x_line = np.linspace(min(x_data) - 1, max(x_data) + 1, 100)
    y_line = a * np.exp(b * x_line)
    plt.plot(x_line, y_line, color='blue', linewidth=2, 
             label=f'y = {a:.3f}e^({b:.3f}x)')
    
    x_pred = 9
    y_pred = a * np.exp(b * x_pred)
    plt.scatter([x_pred], [y_pred], color='green', s=120, zorder=6,
                marker='*', label=f'Prediction at x=9: y={y_pred:.3f}')
    
    plt.title('Exponential Curve Fitting', fontsize=14, fontweight='bold')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    plt.tight_layout()
    
    os.makedirs('figures', exist_ok=True)
    plt.savefig('figures/12.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved as 'figures/12.png'")

    plt.close()

def main():
    x_data = np.array([2, 4, 6, 8, 10])
    y_data = np.array([4.077, 11.084, 30.128, 81.897, 222.62])
    
    a, b = exponential_least_squares(x_data, y_data)
    
    print(f"Fitted curve equation: y = {a:.6f}e^({b:.6f}x)")

    x_estimate = 9
    y_estimate = a * np.exp(b * x_estimate)
    print(f"y({x_estimate}) = {y_estimate:.6f}")
    
    plot_fit(x_data, y_data, a, b)

if __name__ == "__main__":
    main()