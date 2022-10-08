try:
    print("try block")
    num1=int(input("Enter first number"))
    num2=int(input("Enter Another number")) 
    res=num1/num2
except:
    print("Except block")
    print("Number is not divisible by zero")
else:
    print("Else block")
    print("Output   ",res)
finally:
    print("Exceptional handling Program")            