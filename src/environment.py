import random
import math
import agent
import enum

class Environment:

	def __init__(self, dimension, rechargePoints, trashCans):
		self.dimension = dimension
		self.dirtPercentage = random.randint(40, 85)
		self.dirt = 0
		self.rechargePoints = rechargePoints
		self.trashCans = trashCans
		self.matrix = [[" " for i in range(dimension)] for j in range(dimension)]
		self.agent = agent.Agent(0, 0, 0, 0)

	def generate_env(self):
		self.matrix[0][0] = "A"
		for i in range(self.dimension):
			for j in range(self.dimension):
				if i == 2:
					if j == 2  or j == 3:
						self.matrix[i][j] = "W"
					if j == (self.dimension - 3)  or j == (self.dimension - 4):
						self.matrix[i][j] = "W"

				elif i == self.dimension - 3:
					if j == 2  or j == 3:
						self.matrix[i][j] = "W"
					if j == (self.dimension - 3)  or j == (self.dimension - 4):
						self.matrix[i][j] = "W"
				elif i >= 2 and i <= (self.dimension - 3):
					if j == 3 or j == (self.dimension - 4):
						self.matrix[i][j] = "W"
	
		self.allocate_points_of_interest()

	# Allocate trash cans, recharge points and dirt
	def allocate_points_of_interest(self):
		totalPositions = self.dimension * self.dimension
		occupiedPositions = 1

		aux = 0
		while aux < self.rechargePoints:
			i = random.randint(3, (self.dimension - 4))
			
			left_or_right = random.randint(0, 1)

			if left_or_right == 0:
				j_ini = 0
				j_end = 2
			else:
				j_ini = self.dimension - 3
				j_end = self.dimension - 1

			j = random.randint(j_ini, j_end)

			if self.matrix[i][j] == " ":
				aux = aux + 1
				self.matrix[i][j] = "R"
				occupiedPositions += 1

		aux = 0
		while aux < self.trashCans:
			i = random.randint(3, (self.dimension - 4))
			
			left_or_right = random.randint(0, 1)

			if left_or_right == 0:
				j_ini = 0
				j_end = 2
			else:
				j_ini = self.dimension - 3
				j_end = self.dimension - 1

			j = random.randint(j_ini, j_end)

			if self.matrix[i][j] == " ":
				aux = aux + 1
				self.matrix[i][j] = "T"
				occupiedPositions += 1

		self.dirt = math.floor((self.dirtPercentage * (totalPositions - occupiedPositions)) /  100)

		print("\nTotal positions in matrix: " + str(totalPositions))
		print("Occupied positions in matrix: " + str(occupiedPositions))
		print("Dirt percentage: " + str(self.dirtPercentage) + "%")
		print("Number of dirt positions: " + str(self.dirt))

		aux = 0
		while aux < self.dirt:
			i = random.randint(0, self.dimension - 1)
			j = random.randint(0, self.dimension - 1)

			if self.matrix[i][j] == " ":
				self.matrix[i][j] = "d"
				aux = aux + 1
	
	def valid_move(self, direction):
		new_x = self.agent.x + (direction.x)
		new_y = self.agent.y + (direction.y)

		if (new_x >= 0 and new_y >= 0 and
			new_x < self.dimension and 
			new_y < self.dimension):
			
			if (self.matrix[new_x][new_y] != "W" and
				self.matrix[new_x][new_y] != "R" and
				self.matrix[new_x][new_y] != "T"):

				return new_x, new_y
			else:
				return None

		return None

	def print_env(self):
		print("\n\nX X", end=" ")
		for j in range(self.dimension):
			print("X", end=" ")

		print("")

		for i in range(self.dimension):
			print("X ", end="")
			for j in range(self.dimension):
				print(str(self.matrix[i][j]), end=" ")
			print("X")

		print("X X", end=" ")
		for j in range(self.dimension):
			print("X", end=" " )
		print("\n\n")

class Direction(enum.Enum):
	NORTH 		= (0, -1)
	SOUTH 		= (0, 1)
	EAST		= (1, 0)
	WEST		= (-1, 0) 
	NORTHEAST 	= (1, -1)
	NORTHWEST 	= (-1, -1)
	SOUTHEAST 	= (1, 1)
	SOUTHWEST 	= (-1, 1)

	def __init__(self, x, y):
		self.x = x
		self.y = y