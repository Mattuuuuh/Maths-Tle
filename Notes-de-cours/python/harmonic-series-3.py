def seuilH(M):
	S = 0
	k=1
	while S < M:
		S += 1/k
		k += 1
	return k

print(seuilH(10))
