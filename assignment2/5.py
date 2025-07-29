def langrange_interpolate(xs: list[float], ys: list[float], x0: float) -> float:
	assert len(xs) == len(ys)
	res: float = 0
	for i, xi in enumerate(xs):
		prod = 1.0
		for j, xj in enumerate(xs):
			if i != j:
				prod *= (x0 - xj) / (xi - xj)
		res += prod * ys[i]
	return res


if __name__ == "__main__":
	xs: list[float] = [0, 1,  3,   4,   5]
	ys: list[float] = [0, 1, 81, 256, 625]
	x0 = 2

	print(langrange_interpolate(xs, ys, x0))
