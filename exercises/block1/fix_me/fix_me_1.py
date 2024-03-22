print("Make this work")
print("Make this " + "work") # added a space after "this" to match first print
print("Make", "this", "work") # wrapped the parameters into a bracket so it is sent to the function

x = 10
x = x + 5 # the original line was just adding 5 to x, i fixed it by re-declaring the variable
x_doubled = x * 2 # fixed this by changing the variable name to "x_doubled" as you cannot start a variable name with a number
x_squared = x ** 2 # fixed this by changing the dash to an underscore in the variable name

y = 25.0 # changed the variable to be a float by adding a decimal to it
half_y = x / 2 # changed the floor division to regular division as the variable should be a float
y = y + 20 # the original line was just adding 20 to y, i fixed it by re-declaring the variable
root_y = y ** 1/2

print("x + y =", x+y)
print("x + y = " + str(x+y)) # this line didn't originally work because the x+y are not strings, therefore they can't be concatenated. you can fix this by type casting it to a string using the str function 