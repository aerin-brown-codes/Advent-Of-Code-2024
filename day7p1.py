def eval(nums, ops): 
    for op in ops:
        if op: #plus
            nums = [nums[0] + nums[1]] + nums[2:]
        else:
            nums = [nums[0] * nums[1]] + nums[2:]
    return nums[0]

def test_set(target, nums):
    ops = [False for i in range(len(nums) - 1)]
    possibilities = 2 ** len(ops)
    for i in range(possibilities):
        if eval(nums, ops) == target:
            return True
        ops = increment_binary(ops)
    return False
        
def increment_binary(bin):
    cout = False
    result = []
    first = True
    for b in bin[::-1]:
        if first:
            result.append(not b)
            cout = b
            first = False
        else:
            result.append((b and not cout) or (cout and not b))
            cout = b and cout
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