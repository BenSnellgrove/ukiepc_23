# timelimit then two wrong answers so dont know
# needs more fast


input()
data = input().split()
data = [int(i) for i in data]
data.sort()

out = 0
e = len(data) - 1

for n in range(len(data) // 3):
    out += data[e-1]
    e -= 2

print(out)




"""
for n in range(len(data) // 3, len(data), 2):
    out += int(data[n])
    # data = data[1:-2]
"""