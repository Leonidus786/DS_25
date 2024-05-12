'''A lambda function is a small 
anonymous (bina naam wala) function.
A lambda function can take any number of arguments, 
but can only have one expression.


Syntax ----> 
lambda arguments : expression

'''
# x = lambda a : a + 10
# print(x(5))

'''The power of lambda is better shown when you use them 
as an anonymous function inside another function.'''

# def myfunc(n):
#   return lambda a : a * n

# # mydoubler = myfunc(2) 

# mytripler = myfunc(3)

# # a = int(input("Enter a number: "))

# # print(mydubleor(a))


# # print(mytripler(a))



def myfunc(n):
  return lambda a : a ** n

 

mycube = myfunc(3)

a = int(input("Enter a number: "))

print(mycube(a))



