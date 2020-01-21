from classes import wheel,engine,body

class vehicle(wheel, engine, body,):
	def __init__(self, horsepower, cylinders, color, w_size=18, num_doors=4):
		self.engine = engine(horsepower,cylinders)

		self.front_right_wheel = wheel(w_size)
		self.front_left_wheel = wheel(w_size)
		self.back_right_wheel = wheel(w_size)
		self.back_left_wheel = wheel(w_size)


		self.body = body(color,num_doors)

	def drive(self, num_miles):
		print(f"You just drove {num_miles}")
		self.engine.mileage += num_miles
		self.engine.trip_counter += num_miles

	def repair(self):
		print(f"Thanks for your repair!")
		self.engine.change_oil()
		self.engine.max_mileage +=100

	def check_mileage(self):
		mileage = self.engine.mileage
		print(f"Your car has {mileage} miles")

camry = vehicle(180, 4, "Silver")
santa_fe = vehicle(280,4,"blue", w_size=20)

camry.check_mileage()
santa_fe.check_mileage()

camry.drive(160)
santa_fe.drive(10)

camry.check_mileage()
santa_fe.check_mileage()