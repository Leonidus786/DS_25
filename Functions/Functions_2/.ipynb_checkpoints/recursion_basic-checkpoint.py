# Recursion --> mtlb function khud ko definition me hi bula lega 


##Recursion -- Factorial of a number 

# n = int(input("Enter a number: "))

## creating a function with name factorial
# def factorial(n):  
#   if n == 0 or n == 1:
#     return 1
#   else:
#     ## Calling function (factorial) itself --- Recursive function
#     return n * factorial(n-1)
  

# result = factorial(n)


n = int(input("Enter a number: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else :
        return n * factorial(n-1)
    
result = factorial(n)

print(f"The factorial of {n} is : {result}")
  
