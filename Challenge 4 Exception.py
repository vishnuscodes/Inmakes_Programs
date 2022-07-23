def Handle_Exception(x,y):
    try:
        ans = x/y
        return ans

    except:
        custom_exception = "There is a problem with your input"
        return custom_exception


x = int(input("Enter the first number"))
y = int(input("Enter the second number"))

answer = Handle_Exception(x,y)
print(answer)