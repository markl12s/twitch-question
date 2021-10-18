x = [5, 4, 5, 6, 7, 2, 7, 1, 8, 9, 4] #this is the number, input 1 digit per index

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
