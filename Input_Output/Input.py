a =10; b=20
print("Value of a is {} and value of b is {}".format(a,b))


num = input("Enter a number")
print(num)



index1 = 10
index2 = 50
print("Prime numbers between {} and {} are :".format(index1, index2))
for num in range(index1, index2+1):
    if num > 1:
        isDivisible  = False
        for index in range(2, num):
            if num % index == 0:
                isDivisible = True
        if not isDivisible:
            print(num, end=" ")