def addIntOnly(a, b):
    if(type(a) == type(1) and type(b) == type(1)):
        return a+b
    else:
        return "Hag diye tum"


print(addIntOnly(5, 3))
print(addIntOnly("Hello", "World"))
print(addIntOnly(4.3, 5.7))
