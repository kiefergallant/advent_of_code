f = open("locations.txt")
left_list = []
right_list = []

for line in f:
    left,right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()

print(left_list)

print(right_list)
s = 0
for i in range(len(left_list)):
    diff = left_list[i] - right_list[i]
    diff = abs(int(diff))
    s+=diff

print(s)

sum(left_list)
