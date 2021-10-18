x = [7235] #this is the number, just input a number into the array, don't have to do each digit seperatetly

print(sum(x))
num = sum(x)

number_string = str(num)
for q in range(4):
    x = []

    for z in range(len(number_string)):
        thing = number_string[z]
        thing = int(thing)
        x.append(thing)

    print(sum(x))
    num = sum(x)

    number_string = str(num)
