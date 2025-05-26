#JONATHAN DURON GONZALEZ   
num = 1
while num < 1000:
    text =""
    if num %3 == 0:
        text+="FIZZ"
    if num %5 == 0:
        text+="BUZZ"
    if len(text) >0:
        print(text)
    else:
        print(num)
    num+=1