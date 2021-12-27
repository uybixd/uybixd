# assign string "{} {} {} {}" to variable formatter
formatter = "{} {} {} {}"
# print formatter and embed 1, 2, 3, 4 in the variable
print(formatter .format(1, 2, 3, 4))
# print formatter and embed "one", "two", "three","four" in the variable
print(formatter.format("one", "two", "three", "four"))
# print formatter and embed True, False, False, True those boolean value in it.
print(formatter.format(True, False, False, True))
# print formatter and pass four arguments(formatter * 4) to it 
print(formatter.format(formatter, formatter, formatter, formatter))
# print formatter and pass four strings in it.
print(formatter.format(
    "She ask",
    "what's the poit", 
    "of", 
    "learning programing language. What a nard."
    ))
# 所谓的 format函数 可以把 format() 括号里的参数传递给. 之前的字符串的花括号里
