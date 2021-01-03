# string methods in python.
# 1. capitalize() --  method.
# it converts the first letter of the string as capital.
name =  input("Enter the String: ") # input the string from command prompt.
print(name.capitalize()) # capitalize method returns the first letter of the string as capital.
# capitalize method does not take any argument.
# 2. casefold() -- method
# casefold method & lower method are similar.
# casefold method is stronger it convertes more chars.
print(name.casefold()) # casefold method returns the all the chars to lower case in the given string.
#  it will not make any changes with the original string.
#  it will not take any argument.
# 3. center() -- method
# it takes two arguments one is required & other is optional.
# first argument is compalsary & second argument is optional.
# with the first argument it takes lenth & send argument is character.
# as second argument is optional if it is not given it takes " " by default with the missing char.
print (name.center(30, '-')) # returns the string to the center. 
print(name.center(10,'0'))  # return the string in the middile.
# 4. count() -- method.
# it takes 3 arguments value, start & end.
# it return the number of times the values appering in the string.
print(name.count("i"))
