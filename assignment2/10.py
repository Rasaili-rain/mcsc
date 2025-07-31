import numpy as np
import matplotlib.pyplot as plt
import os


def solve_bvp(p, q, r, xa, xb, ya, yb, h=0.1):
    x = np.arange(xa, xb + h, h)
    n = len(x)
    A = np.zeros((n, n))
    b_vec = np.zeros(n)

    # Boundary rows
    A[0, 0], b_vec[0]   = 1.0, ya
    A[-1, -1], b_vec[-1] = 1.0, yb

    # Interior rows
    for i in range(1, n - 1):
        xi = x[i]
        A[i, i - 1] = 1 / h**2 - p(xi) / (2*h)
        A[i, i]     = -2 / h**2 + q(xi)
        A[i, i + 1] = 1 / h**2 + p(xi) / (2*h)
        b_vec[i]    = r(xi)

    y = np.linalg.solve(A, b_vec)
    return x, y

def plot_solution(x, y):
    plt.plot(x, y, marker='x', label='FDM')
    plt.xlabel('x'); plt.ylabel('y')
    plt.title("y'' – 6 y' + 10 y = 0 (FDM, h=0.1)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    os.makedirs('figures', exist_ok=True)
    plt.savefig('figures/10.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved as 'figures/10.png'")
    plt.close()

if __name__ == "__main__":
    # y'' – 6 y' + 10 y = 0,
    p = lambda x: -64         # coefficient of y'
    q = lambda x: 10          # coefficient of y
    r = lambda x: 0           # RHS
    x, y = solve_bvp(p, q, r, xa=0, xb=1, ya=0, yb=0, h=0.1)
    plot_solution(x, y)
