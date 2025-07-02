def H(n):
	S = 0
	for k in range(1,n+1):
		S += 1/k
	return S

print(H(100))
