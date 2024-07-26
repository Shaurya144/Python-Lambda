# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# For Example
x = lambda a : a + 10 # takes the arguements a and adds 10 to it and returns the answer
print(x(5))

# This is useful as you can make multiple functions based of one lambda inside a function. Eg.
def Multiplier(n): # takes arguement n
    return lambda a : a * n # multiplies unknown number by unknown number

# Now We can use this to make multiple other functions
myDoubler = Multiplier(2)
myTripler = Multiplier(3)
myQuadrupler = Multiplier(4)

print(myDoubler(2))
print(myTripler(2))
print(myQuadrupler(2))