with open("day11_input.txt", "r") as f:
    data = f.read().strip()

stones = [int(i) for i in data.split()]

for i in range(75):
    index = 0
    while index < len(stones):
        stone = stones[index]
        stone_str = str(stone)
        if stone == 0:
            stones[index] = 1
        elif len(stone_str) % 2 == 0:
            stones[index] = int(stone_str[:len(stone_str) // 2])
            stones.insert(index + 1, int(stone_str[len(stone_str) // 2:]))
            index += 1
        else:
            stones[index] = stone * 2024
        index += 1

print(len(stones))