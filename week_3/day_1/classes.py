class wheel:
	def __init__(self, diameter, wtype="all-weather"):
		self.size = diameter
		self.type = wtype


class engine:
	def __init__(self, horsepower, n_cylinders):
		self.horsepower = horsepower
		self.n_cylinders = n_cylinders

		self.is_healthy = True
		self.need_oil_change = False
		self.trip_counter = 0
		self.mileage = 0
		self.max_mileage = 150000

	def check_health(self):
		if self.mileage > self.max_mileage:
			self.is_healthy = False
			print("Our engine is braeaking")

		if self.trip_counter >=3000:
			self.is_healthy = False
			self.need_oil_change = True
			if self.trip_counter >=15000:
				print("Im dead")
				self.mileage = self.max_mileage
			elif self.trip_counter >=6000:
				print("Im Going to die")

			print("Change your Oil")


	def change_oil(self):
		print("Thanks for changing oil")
		self.trip_counter = 0
		self.need_oil_change = False
		self.is_healthy = True

class body:
	def __init__(self, color, num_doors=4):
		self.color = color
		self.num_doors = num_doors
		if self.num_doors == 0:
			self.trunk_size = "tiny"
		elif self.num_doors == 2:
			self.trunk_size = "small"
		elif self.num_doors == 4:
			self.trunk_size = "med"
		elif self.num_doors == 5:
			self.trunk_size = "large"



















