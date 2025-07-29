import os
import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, x0, y0, xn, n):
    h = (xn - x0) / n
    x_vals = np.linspace(x0, xn, n + 1)
    y_vals = np.zeros(n + 1)
    y_vals[0] = y0
    
    for i in range(n):
        y_vals[i + 1] = y_vals[i] + h * f(x_vals[i], y_vals[i])
    
    return x_vals, y_vals

def display_results(x_vals, y_vals):
    print("-" * 24)
    print(f"{'Step':<6} {'x':<8} {'y':<10}")
    print("-" * 24)
    for i, (x, y) in enumerate(zip(x_vals, y_vals)):
        print(f"{i:<6} {x:<8.2f} {y:<10.3f}")
    

def plot_solution(x_vals, y_vals):
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, 'o-', color='#FF6B35', linewidth=2, 
             markersize=6, markerfacecolor='white', markeredgewidth=2,
             label="Euler's Method")
    
    plt.title("Euler's Method", fontsize=14, fontweight='bold')
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    plt.tight_layout()
    
    os.makedirs('figures', exist_ok=True)
    plt.savefig('figures/8.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved as 'figures/8.png'")
    plt.close()  

def main():
    def f(x, y): return x**2 + x
    
    x0, y0 = 0, 1
    xn = 2
    n = 20
    
    x_vals, y_vals = euler_method(f, x0, y0, xn, n)
    display_results(x_vals, y_vals)
    plot_solution(x_vals, y_vals)
    
    print(f"\nFinal approximation: y({xn}) = {y_vals[-1]:.6f}")

if __name__ == "__main__":
    main()