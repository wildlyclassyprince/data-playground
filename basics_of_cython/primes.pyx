def primes(int kmax):
	cdef int n, k, i
	cdef int p[1000]
	result = list()
	if (kmax > 1000):
		kmax = 1000
	k, n = 0, 2
	while (k < kmax):
		i = 0
		while (i < k) and (n % p[i] != 0):
			i = i + 1
		if (i == k):
			p[k] = n
			k = k + 1
			result.append(n)
		n = n + 1
	return result
