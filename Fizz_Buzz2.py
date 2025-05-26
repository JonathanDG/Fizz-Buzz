#JONATHAN DURON GONZALEZ   
num = 1

while num <= 1000:
    text =""
    if num %15 == 0:
       print("FIZZBUZZ")
    elif num %5 == 0:
        print("BUZZ")
    elif num %3 == 0:
        print("FIZZ")
    else:
        print(num)

    num+=1