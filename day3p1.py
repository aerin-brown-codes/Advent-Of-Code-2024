with open("day3_input.txt", "r") as f:
    data = f.read()

#data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

total = 0
instructions = data.split("mul(")
for instruction in instructions:
    if instruction[0] == " ":
        continue
    params = instruction.split(",")
    if len(params) < 2:
        continue
    if params[0][-1] == " ":
        continue
    try:
        a = int(params[0])
    except:
        continue
    if params[1][0] == " ":
        continue
    if params[1].count(")") == 0:
        continue
    second_param = params[1].split(")")
    if second_param[0][-1] == " ":
        continue
    try:
        b = int(second_param[0])
    except:
        continue
    total += a * b

print(total)   