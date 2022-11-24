import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1-D Ising

def grapher(lattice):
	fig, (ax1) = plt.subplots(figsize=(16,10))
	pos = ax1.imshow(lattice, cmap='binary')
	fig.colorbar(pos, ax = ax1)
	plt.show()


def change_lattice(lattice, pos):
	new = lattice.copy()
	new[pos] = (new[pos]+1)%2
	return new

def move(lattice, beta):
	a = np.random.randint(N)

def transpose(lattice, steps):
	new = lattice.copy()
	x,y = steps
	for i in range(len(lattice)):
		for j in range(len(lattice[0])):
			new[i,j] = lattice[i-x, j-y]
	return new

def rotate(lattice, point):
	pass


# -----------------------------------------------------------------------------
N = 100
lattice = np.random.randint(2, size = (10,N))
new = transpose(lattice, (0,5))


fig, (ax1, ax2) = plt.subplots(2, figsize=(16,10))
pos = ax1.imshow(lattice, cmap='binary')
pos2 = ax2.imshow(new, cmap='binary')
# fig.colorbar(pos, ax = ax1)
plt.show()

