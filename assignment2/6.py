from math import pi, sin, exp

def compute_integral(f, x0: float, xn: float, divs: int) -> float:
	assert divs != 0
	assert x0 < xn

	h:float = (xn - x0) / divs

	total:float = f(x0) + f(xn)

	for i in range(1, divs):
		xi = x0 + i * h
		total += 2 * f(xi)

	return h / 2 * total

if __name__ == "__main__":
	x0, xn = (0, pi)
	def f(x): return sin(x) / exp(x)
	divs:int = 20
	result = compute_integral(f,x0,xn,divs)

	print(f"Approximated integral: {result:.8f}")
	
