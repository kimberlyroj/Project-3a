# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 1/19/2021
# Description: A program that asks the user how many integers they would like to enter. Once that integer is input it will list the min and max
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