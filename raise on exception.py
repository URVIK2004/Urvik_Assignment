try:
    x=int(input("Enter a Age:-15  "))
    if x >18:
        raise ValueError(x)
except ValueError:
    print(x,"is grater than 18")
else:
    print(x,"is not grater than 18")            