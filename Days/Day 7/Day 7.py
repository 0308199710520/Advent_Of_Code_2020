import re
with open("Day 7 input") as Day_7_input:
    Input_Data = [line.strip() for line in Day_7_input.readlines()]

colour_value_dict = {}

for line in Input_Data:
    bag_name, bag_content = re.split(r"contain", line)
    bag_name = (re.split("bag", bag_name)[0]).strip()
    colour_value_dict[bag_name] = []
    split_bag_content = list(re.split(r",", bag_content))

    for content in split_bag_content:
        content = (re.split("bag", content)[0]).strip(" ")
        #print(content)
        if content == "no other":
            colour_value_dict[bag_name] = None
        else:
            colour_value_dict[bag_name].append(content.strip())
            colour_value_dict[bag_name][-1] = re.split(" ", colour_value_dict[bag_name][-1], maxsplit=1)



def counter(bag_colour=None, depth_tracker=None, running_total=0):
    if depth_tracker is None:
        depth_tracker = []
    bag_content = colour_value_dict[bag_colour]
    if bag_content is None:
        temp_value = 1
        for x in depth_tracker:
            temp_value *= x
        return running_total + temp_value

    for balls in bag_content:
        depth_tracker.append(int(balls[0]))
        running_total += counter(balls[1], depth_tracker, running_total)

    return running_total


print(counter("shiny gold"))
'''



def search(bag_colour):




    #is the current bag shiny gold ?

    #yes return true
    if bag_colour == "shiny gold":
        return True
    else:
        if colour_value_dict[bag_colour] is None:
            return
        for colour in colour_value_dict[bag_colour]:
            if search(colour):
                return True
            else:
                continue
        return False



total = 0
for bag in colour_value_dict.keys():
    if search(bag):
        total += 1
    else:
        continue

print(total)
'''