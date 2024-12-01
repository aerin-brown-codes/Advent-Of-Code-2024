with open("day1_input.txt", "r") as f:
    txt = f.read()

lines = txt.split("\n")
l1 = []
l2 = []

for line in lines:
    pair = line.split("   ")
    l1.append(int(pair[0]))
    l2.append(int(pair[1]))

l1.sort()
l2.sort()
difference = 0
for i in range(len(l1)):
    difference += abs(l1[i] - l2[i])

print(difference)