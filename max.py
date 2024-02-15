n = []

for i in range(10):
    value = int(input("enter a value "))
    n.append(value)

largest = n[0]

for x in n:
    if x > largest:
        largest = x

print("largest in number is: ", largest)
