Num=int(input("How many integers would you like to enter?"))
print("Please enter",Num, "integers.")
min=int(input())
max=min
for i in range(1,Num):
    number=int(input())
    if number > max:
        max=number
    if number < min:
        min=number
print("min:", min)
print("max:", max)