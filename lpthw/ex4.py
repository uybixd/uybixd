# name a variable cars, and assign 100 to it
cars = 100
# Name a variable "space_in_a_car" means the space in a car, and assign 4.0 to it.
space_in_a_car = 4.0
# Name a variable "drivers", and assign 30 to it.
drivers = 30
# Name a variable "passengers", and assign 90 to it.
passengers = 90
# Name a variable "cars_not_driven", and assign 变量 'cars' - 变量'drivers'.
cars_not_driven = cars - drivers
# Name a variable "cars_driven", and assign the 变量 'drivers'的值 to it.
cars_driven = drivers
# Name a variable "carpool_capacity", and 赋值给它 赋 变量 'cars_driven' * 'space_in_a_car'.
carpool_capacity = cars_driven * space_in_a_car
# Name a variable "average_passengers_per_car", and assign the 结果 var 'passengers' / cars_driven.
average_passengers_per_car = passengers / cars_driven

# Show "There are" on the screen. print the value of var 'cars' 在句子的后面，then print"cars avaiable."
print("There are", cars, "cars available.")
# Show "There are only" then print the value of var 'drivers' and "drivers avaiable." on the screen.
print("There are only", drivers, "drivers avaiable.")
# Show "There will be" then the value of var 'cars_not_driven' and "empty cats today" on the screen.
print("There will be", cars_not_driven, "empty cars today.")
# Show "We can transport" then the value of var 'carpool_capacity' and "people today." on the screen.
print("We can transport", carpool_capacity, "people today.")
# Show "We have" then the value of var 'passengers' and "to carpool today." on the screen.
print("We have", passengers, "to carpool today.")
# Show "We need to put about" then the value of var 'average_passengers_per_car' and "in each car." on the screen.
print("We need to put about", average_passengers_per_car, "in each car.")
