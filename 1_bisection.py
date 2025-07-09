from math import sin

a: float = 0.5
b: float = 1.0
dp = 10

def f(x: float) -> float:
    return x**2 - sin(x)

def evaluateRoot(a: float, b: float, step: int = 1) -> float:
    c = (a + b) / 2
    fc = f(c)
    if step == 1:
        print(f"{'Step':<5} {'a':<15} {'b':<15} {'c (mid)':<15} {'f(c)':<15}")
        print("-" * 70)
        
    print(f"{step:<5} {a:<15.{dp}f} {b:<15.{dp}f} "
          f"{c:<15.{dp}f} {fc:<15.{dp}f}")

    if abs(fc) <= 10**(-dp): 
        return round(c, dp)
    elif f(a) * fc < 0:
        return evaluateRoot(a, c, step + 1)
    else:
        return evaluateRoot(c, b, step + 1)

print (f"root is " ,evaluateRoot(a, b))
