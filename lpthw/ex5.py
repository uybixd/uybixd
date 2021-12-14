# Name a variable called "name", assign the sting 'ZhangHongXiang' to it.
name = 'ZhangHongXiang'
# Name a variable called "age", assign 23 to it.
age = 23 # not a lie
# Name a variable called "height", assign 66 to it.
height = 66 # inches
# Name a variable called "height_cm", assign the calculation result of round height * 2.54
height_cm = round(height * 2.54)
# Name a variable called "weight", assign 156.7 to it.
weight = 156.7 # lbs # 磅
# Name a variable called "weight_kg", and assign the calculation result of round(weight * 0.453)
weight_kg = round (weight * 0.453)
# Name a variable called "eyes", assign the string 'Brown' to it.
eyes = 'Brown'
# Name a variable called "teeth", assign the string 'White' to it.
teeth = 'White'
# Name a variable called "hair", assign the string 'Black' to it.
hair = 'Black'
# Show the "Let's talk about" and the value of var name on the screen
print(f"Let's talk about {name}.")
# Show the "He's" then the value of var {height_cm} and the "centimetres tall." on the screen.
print(f"He's {height_cm} centimetres tall.")
# 在屏幕上 Show the "He's" 然后加上变量 {weight} 的值，再在后面接上 "kilogram heavy."
print(f"He's {weight_kg} kilograms heavy.")
# Show the "Actually that's a little heavy." on the screen.
print("Actually that's a little heavy.")
# Show the "He's got" then the value of var {eyes} then "and" then the value of var {hair} then "hair" on the screen.
print(f"He's got {eyes} eyes and {hair} hair.")
# Show the "His teeth are usually" then the value of var {teeth} then "depending on the coffee or tea." on the screen
print(f"His teeth are usually {teeth} depending on the coffee or tea.")
# Name a variable called "total" and assign the calculation result of (age + height_cm + weight_kg)
# this line is tricky, try to get it exactly right
# 我其实没有看出来 tricky 在哪里 
total = age + height_cm + weight_kg
# Show the "If I add" then the value of var {age} then "," then the value of var {height_kg} then ", and" then the value of var {weight_kg} then "I get" then then value of var {total}.
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total}.")
