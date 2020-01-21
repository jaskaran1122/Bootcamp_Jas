
def find_avg_year(years):
	sum = 0
	for year in years:
		sum += year
	return int(sum/len(years))

def find_avg_year_short(years):
	return int(sum(years)/len(years))



list_of_cars = ["Toyota", "Ford", "BMW", "Audi", "Benz"]
list_of_models =["Camry", "F150", "i8", "A4", "S550"]

car = {
	"make" : list_of_cars,
	"model" : list_of_models,
	"years" :[2010, 2017, 2020, 2006, 2020]

}

for key in car:
	#print(key)
	pass

car_years = car["years"]
#print(car_years)

avg_year = find_avg_year(car_years)
#print("The average year of all the cars is: {avg_year}")

car_color = ["red", "blue", "black", "blue", "silver"]
car["color"] = car_color
for key in car:
	#print(key)
	pass

for value in car.values():
	#print(value)
	pass


car_stock = [3, 5, 6, 1, 3]
car["stock"] = car_stock
for key in car:
	#print(key)
	pass
	
for value in car.values():
	#print(value)
	pass


inventory = car["stock"]
#print(f"We have {sum(inventory)} cars in stock!")	

car_dealer = ["Amy", "Bob", "Charlie", "Dylan", "Elephant"]
car["dealers"] = car_dealer
for value in car.values():
	print(value)
	pass

print("Firing all the dealers ...")
# car.pop("dealers")
# for key in car:
# 	print(key)

print(car)
print("\n we are going to close our dealership")
car.clear() # erase the content of the dictionary

print(car)
del car # delete the whole dictionary
#print(car)



















