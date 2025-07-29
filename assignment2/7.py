from math import sqrt, pi, exp

def simpsons_one_third(f, a: float, b: float, n: int) -> float:
	assert n % 2 == 0, "Number of divisions (n) must be even."
	assert a < b 
	

	h = (b - a) / n

	total = f(a) + f(b)

	for i in range(1, n):
		x = a + i * h
		if i % 2 == 0:
			total += 2 * f(x)
		else:
			total += 4 * f(x)

	return h / 3 * total

if __name__ == "__main__":
	def f(x):
		return (1 / sqrt(2 * pi)) * exp(-x ** 2 / 2)
	result = simpsons_one_third(f, -4, 4, 50)
	print(f"Approximated integral: {result:.8f}")
