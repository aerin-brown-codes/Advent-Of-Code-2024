with open("day1_input.txt", "r") as f:
    data = f.read()

lines = data.split("\n")
l1 = []
l2 = []

for line in lines:
    pair = line.split("   ")
    l1.append(int(pair[0]))
    l2.append(int(pair[1]))

similarity_score = 0
for num in l1:
    similarity_score += num * l2.count(num)
print(similarity_score)