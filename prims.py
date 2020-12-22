import math
import matplotlib.pyplot as plt

class Prim:
	def __init__(self, coords):
		self.coords = coords
		self.k = [False] * len(coords)
		self.d = [float('inf')] * len(coords)
		self.v = list(range(0, len(coords) - 1))

	def algo(self):
		self.d[0] = 0.0
		vertex = 0
		for a in range(len(self.coords)):
			distance = float('inf')
			min_distance = float('inf')
			for b in range(len(self.coords) - 1):
				if self.k[b] is False:
					distance = self.d[b]
					if distance < min_distance:
						min_distance = distance
						vertex = b

			self.k[vertex] = True

			for c in range(len(self.coords) - 1):
				if self.k[c] is False:
					distance = self.calculate_distance(self.coords[vertex], self.coords[c])
					if distance < self.d[c]:
						self.d[c] = distance
						self.v[c] = vertex

	def calculate_distance(self, coord_a, coord_b):
		return math.sqrt((coord_a[0] - coord_b[0]) ** 2 + (coord_a[1] - coord_b[1]) ** 2)

	def print_plot(self):
		x = []
		y = []
		d = 0
		for coord in range(len(self.coords) - 1):
			x.append(self.coords[coord][0])
			x.append(self.coords[self.v[coord]][0])
			y.append(self.coords[coord][1])
			y.append(self.coords[self.v[coord]][1])
			plt.plot(x, y)
			x.clear()
			y.clear()
			d += self.d[coord]
		print()
		print('*******************************')
		print('MST information:')
		print('Distance: ', d)
		print('Total points connected: ', len(self.coords))
		print('Points connected: ')
		for coord in range(1, len(self.coords) - 1):
			print(coord, '-->', self.v[coord])
		print('*******************************')
		plt.show()
		
