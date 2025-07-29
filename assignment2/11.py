import os
import numpy as np
import matplotlib.pyplot as plt

def least_squares_fit(x_data, y_data):
    n = len(x_data)
    sum_x = np.sum(x_data)
    sum_y = np.sum(y_data)
    sum_x2 = np.sum(x_data**2)
    sum_xy = np.sum(x_data * y_data)
    
    A = np.array([[n, sum_x],
                  [sum_x, sum_x2]])
    B = np.array([sum_y, sum_xy])
    
    print("Normal equations:")
    print(f"{n}*a0 + {sum_x}*a1 = {sum_y:.1f}")
    print(f"{sum_x}*a0 + {sum_x2}*a1 = {sum_xy:.1f}")
    
    coefficients = np.linalg.solve(A, B)
    a0, a1 = coefficients
    
    return a0, a1


def plot_fit(x_data, y_data, a0, a1):
    plt.figure(figsize=(10, 6))
    
    plt.scatter(x_data, y_data, color='red', s=80, zorder=5, 
                label='Data Points', edgecolors='black', linewidth=1)
    
    x_line = np.linspace(min(x_data) - 0.5, max(x_data) + 0.5, 100)
    y_line = a0 + a1 * x_line
    plt.plot(x_line, y_line, color='blue', linewidth=2, 
             label=f'y = {a0:.3f} + {a1:.3f}x')
    
    x_pred = 2.5
    y_pred = a0 + a1 * x_pred
    plt.scatter([x_pred], [y_pred], color='green', s=120, zorder=6,
                marker='*', label=f'Prediction at x=2.5: y={y_pred:.3f}')
    
    plt.title('Least Squares Linear Regression', fontsize=14, fontweight='bold')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    plt.tight_layout()
    
    os.makedirs('figures', exist_ok=True)
    plt.savefig('figures/11.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved as 'figures/11.png'")
    plt.close()

def main():
    x_data = np.array([1, 2, 3, 4, 5, 6])
    y_data = np.array([2.4, 3.1, 3.5, 4.2, 5.0, 6.0])
    
    a0, a1 = least_squares_fit(x_data, y_data)
    
    print(f"Fitted line equation: y = {a0:.6f} + {a1:.6f}x")

    x_estimate = 2.5
    y_estimate = a0 + a1 * x_estimate
    print(f"y({x_estimate}) = {y_estimate:.6f}")
    
    plot_fit(x_data, y_data, a0, a1)
    

if __name__ == "__main__":
    main()