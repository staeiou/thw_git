import numpy as np

from matplotlib import pyplot as plt

N = 1000
X = np.random.random(N)
Y = np.random.random(N)

scores = []
noscores = []
for n in range(N):
	x,y = X[n],Y[n]
	if x**2 + y**2 < 1:
		scores.append([x,y])
	else:
		noscores.append([x,y])
	if n%10 == 0:
		print(4*len(scores)/(len(scores)+len(noscores)))