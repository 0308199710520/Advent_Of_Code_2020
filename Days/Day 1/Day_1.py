numbers_list = []

with open("Day 1 1 Numbers") as numbers:
    for line in numbers:
        numbers_list.append(int(line.rstrip("\\n")))

def combination_finder_3(numbers):
    a = 0
    b = 1
    while True:
        if 2020 - (numbers[a]+numbers[b]) in numbers:
            return a, b
        else:
            if b < len(numbers)-1:
                b +=1
            else:
                a+=1
                b = a+1


a,b = combination_finder_3(numbers_list)
print(a)
print(b)
print(2020 - a - b)
print(1846 in numbers_list)
print(numbers_list[a] * numbers_list[b] * (2020 - numbers_list[a]-numbers_list[b]))


'''
def combination_finder(numbers):
    for number in numbers:
        if (2020-number) in numbers:
            return number
        else:
            continue

a = combination_finder(numbers_list)
b = 2020-a

print(a*b)
'''
