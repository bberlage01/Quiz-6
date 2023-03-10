#Bethany Berlage
#Problem 1
while 1==True:
    print("Hello")
#press control c to exit the loop

#Problem 2
i=2
sum=0
while i<12:
    sum+=i
    i+=2
print("The sum of all positive even numbers less than 12 is", sum)

#Problem 4
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(4))
