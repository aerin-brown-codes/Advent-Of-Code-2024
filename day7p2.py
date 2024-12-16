def eval(nums, ops): 
    for op in ops:
        if op == 0: #plus
            nums = [nums[0] + nums[1]] + nums[2:]
        elif op == 1: #mult
            nums = [nums[0] * nums[1]] + nums[2:]
        else: #concat
            nums = [int(str(nums[0]) + str(nums[1]))] + nums[2:]
    return nums[0]

def test_set(target, nums):
    ops = [0 for i in range(len(nums) - 1)]
    possibilities = 3 ** len(ops)
    for i in range(possibilities):
        if eval(nums, ops) == target:
            return True
        ops = increment_binary(ops)
    return False
        
def increment_binary(bin):
    cout = 0
    result = []
    first = True
    for b in bin[::-1]:
        if first:
            result.append((b + 1) % 3)
            if b == 2:
                cout = 1
            first = False
        else:
            result.append((b + cout) % 3)
            if b == 2 and cout == 1:
                cout = 1
            else:
                cout = 0
    return result[::-1]

with open("day7_input.txt", "r") as f:
    data = f.read()

data = data.split("\n")
total = 0

for row in data:
    partition = row.split(": ")
    target = int(partition[0])
    nums = [int(num) for num in partition[1].split(" ")]
    if test_set(target, nums):
        total += target

print(total)