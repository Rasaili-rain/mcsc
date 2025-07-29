from math import exp

x0:float = 1.0
dp = 20

def f(x: float) -> float:
	return exp(x) - 4*x
def fd(x:float)-> float:
	return exp(x) - 4

def evaluateRoot(x: float ,step: int = 1) -> float:
	if step == 1:
		print(f"{'Step':<5} {'x':<15} {'f(x)':<15} {'fd(x)':<15} {'xn':<15}")
		print("-" * 70)

	if (fd(x)!= 0):
		xn = x - (f(x)/fd(x))
		print(f"{step:<5} {x:<15.{dp}f} {f(x):<15.{dp}f} "
			f"{fd(x):<15.{dp}f} {xn:<15.{dp}f}")
		
		if abs(f(xn)) <= 10**(-dp): 
			return round(xn, dp)
		else:
			return evaluateRoot(xn, step+1)
	else:
		print("error ")
		return x
	
print (f"root is " ,evaluateRoot(x0))
