# Set variable cars to 100
cars = 100

# Set variable space_in_a_car to 4.0
space_in_a_car = 4.0

# Set variable drivers to 30
drivers = 30

# Set variable passengers to 90
passengers = 90

# Set variable cars_not_driven to cars - drivers
cars_not_driven = cars - drivers

# Set variable cars_driven to drivers
cars_driven = drivers

# Set variable carpool_capacity to cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car

# Set variable average_passengers_per_car to passengers / cars_driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."