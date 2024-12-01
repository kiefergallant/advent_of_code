f = open("locations.txt")
left_list = []
right_list = []

for line in f:
    left,right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()

my_dict = {}

for num in left_list:
    counter = 0
    for num2 in right_list:
        if num == num2:
            counter+=1
    my_dict[num]=counter

l = [key*value for key,value in my_dict.items()]

print(sum(l))

