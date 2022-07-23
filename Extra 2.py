def simpleinterest(x,y,z):
    sinterest = (x*y*z)/100
    return sinterest


x=int(input("Enter the principal amount: "))
y=int(input("Enter the rate: "))
z=int(input("Enter the term: "))

print("Simple Interest: "+str(simpleinterest(x,y,z)))