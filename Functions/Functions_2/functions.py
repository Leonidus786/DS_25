"""
Function --> Koi Khas Kaam.
A block of code written to perform a particular task.
Also it runs only when it is called.

def mera_naam_function_hai():
  print("Ye m krne wala hu but name leke bulao hmko")

-- Specially bulane k liye

mera_naam_Function_hai()



Ex---1 
#Writing a function ---> Defining a function.
def fun_name(P1, P2, ......, Pn):
    do this:
    while condition is this

    print(and) 
    return (this.value)

# def --> keyword 

# fun_name --> name of the function

# P1....Pn --> Parameters -->A parameter is the variable listed 
# inside the parentheses in the function definition. --- Also called
default values of a function.


Ex---1.1 --->

# Calling a function ---> using arguments

fun_name(A1, A2,........., An)



"""

# def my_function(p1, p2): #p1 & p2 are parameters
#     t = p1+p2
#     print(t) # t is the value of function

# my_function(2,3)

def my_function (a1,a2):
    t = a1+a2
    print(t)

b = my_function(4,5)
print(b)


# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

#Arbitrary Arguments, *args
'''If you do not know how many arguments that will be passed into
 your function, add a * before the parameter name in the function 
 definition.'''



# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

