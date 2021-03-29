import re

with open("Day 13 input.txt") as Day_13:
    Input = [line.strip("\n") for line in Day_13]
Input[0] = int(Input[0])
Input[1] = Input[1].split(",")

try:
    while True:
        Input[1].remove("x")

except ValueError:
    pass


for i in range(len(Input[1])):
    Input[1][i] = int(Input[1][i])


print(Input)