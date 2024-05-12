"""I want to specify that at the position of x whatever
the value you're  passing to function should be there"""

def my_function(x, /):
  print(x)

# my_function(x = 3) #This gives a error
  
my_function(3)
