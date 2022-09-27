cubes = [number**3 for number in range(1, 11)]
print(cubes)


for num in range(2, 101):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


age = int(input("What is your age."))
if age in range(1, 17):
    print("Sorry Kid! ")
else:
    print("Adults Only")
if age in range(18, 65):
    print("Hello adults! ")
else:
    print('Senior citizans')
