# creat a variable named 'types_of_people' and set it = 10
#### assign 10 to types_of_people
types_of_people = 10
# creat a variable named 'x' set it a f-string and embed variable 'types_of_people' 
# like "There are {types_of_people} types of people."
#### assign the f-string to x (insert types_of_people in the string)
x = f"There are {types_of_people} types of people."

# Creat a variable named 'binary' set it = (equal) "binary"
#### assign "binary" to binary
binary = "binary"
# Creat a variable named 'do_not' =(equal) "don't"
do_not = "don't"
# Creat a variable named 'y' set it =(equal) a f-string and embed the variables 'binary' and 'do_not' in it
# like this: f"Those who know {binary} and those who {do_not}."
#### assign the f-string to y(insert binary and do_not in the string)
y = f"Those who know {binary} and those who {do_not}."
# show the 'value' of var 'x' on the screen

print(x)
# show the 'value' of variable 'y' on the screen
print(y)
# 在屏幕上打印一个 f-string 并将 变量 x 嵌入其中 like this: f"I said : {x}"
# 效果就是python interpreter 先识别到了 'f' 知道了这里有一个变量需要 format ，先正常的打印前面的内容 遇到花括号后会将里面的变量值打印出来
print(f"I said :{x}")
# show the "I also said:" first then embed the variable {y} between the "''" on the screen. 
print(f"I also said : '{y}'")
# Creat a variable named 'hilarious' set it =(equal) False
hilarious = False
# creat a variable named 'joke_evaluation' set it =(equal) "Isn't that joke so funny?! {}"
# there is a brackets for the .format to embed variable in the string
joke_evaluation = "Isn't that joke so funny?! {}"
# show the value of variable 'joke_evaluation' on the screen and embed the variable hilarious in it 
#by using the '.format()' 

print(joke_evaluation.format(hilarious))
# creat a variable named 'w' and set it =(equal) "This is the left side of ..."
w = "This is the left side of ..."
# creat a variable named 'e' and set it =(equal) "a string with a right side."
e = "a string with a right side."
# show the value of variable w and e together
print(w + e)
# drill 中让我解释一下为什么 "+" 会让两个strings 拼接在一起，但这不就是设计这门语言的人的规定吗，也挺符合直觉的。
