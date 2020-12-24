import math
import matplotlib.pyplot as plt

class ArbitraryInsertion:
	def __init__(self, coords):
		self.coords = coords
		self.subtour = []
		self.in_subtour = [False] * (len(self.coords))

	def algo(self):
		self.in_subtour[0] = True
		self.subtour.append(0)
		print(self.subtour)
		min_distance = float('inf')
		nearest_coord = 0
		for coord in range(1, len(self.coords)):
			curr_distance = self.calculate_distance(self.coords[0], self.coords[coord])
			if (curr_distance < min_distance):
				min_distance = curr_distance
				nearest_coord = coord
		print(nearest_coord)

		self.subtour.append(nearest_coord)
		self.in_subtour[nearest_coord] = True

		next_coord = 0
		for a in range(len(self.coords) - 2):
			next_coord = self.arbitrary_selection()
			min_arc = float('inf')
			conn_coord = 0
			for b in range(len(self.subtour) - 1):
				if self.in_subtour[b] == True:
					curr_arc = self.calculate_distance(self.coords[self.subtour[b]], self.coords[next_coord]) + self.calculate_distance(self.coords[next_coord], self.coords[self.subtour[b + 1]]) - self.calculate_distance(self.coords[self.subtour[b]], self.coords[self.subtour[b + 1]])
					if (curr_arc < min_arc):
						min_arc = curr_arc
						conn_coord = self.subtour[b]
			self.in_subtour[next_coord] = True
			self.subtour.insert(self.subtour.index(conn_coord) + 1, next_coord)

		#add point to connect back to
		self.subtour.append(0)

	def arbitrary_selection(self):
		coord = 0
		while self.in_subtour[coord] == True:
			coord += 1
		return coord
	
	def calculate_distance(self, coord_a, coord_b):
		return math.sqrt((coord_a[0] - coord_b[0]) ** 2 + (coord_a[1] - coord_b[1]) ** 2)

	def print_plot(self):	
		x = []
		y = []
		for i in self.subtour:
			x.append(self.coords[i][0])
			y.append(self.coords[i][1])

		#calculates total distance and prints
		distance = 0
		for i in range(len(self.coords)):
			distance += self.calculate_distance(self.coords[self.subtour[i]], self.coords[self.subtour[i + 1]])

		print()
		print('*******************************')
		print('Arbitrary Insertion information:')
		print('Distance: ', distance)
		print('Total points connected: ', len(self.coords))
		print('Points connected: ')
		for i in range(len(self.subtour)):
			print(self.subtour[i], '--> ', end =" ")
		print('*******************************')

		plt.plot(x, y)
		plt.show()
		
