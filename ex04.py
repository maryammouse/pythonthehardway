cars = 100  # assigns a value to car
space_in_a_car = 4.0  # assigns a value to space in a car
drivers = 30  # the number of drivers
passengers = 90  # the number of passengers
cars_not_driven = cars - drivers  # the number of cars not driven
cars_driven = drivers  # the number of cars driven
carpool_capacity = cars_driven * space_in_a_car  #the amount of people
#that can be transported
average_passengers_per_car = passengers / cars_driven  # approx.
# number of passengers per car.

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
