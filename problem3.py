import math

spots = int(input())
posts = int(input())
angles = [int(i) for i in input().split()]

def cosRule(b, c, theta):
    return math.sqrt((b ** 2) + (c ** 2) - (2 * b * c * math.cos(math.radians(theta))))

def tringlArea(a, b, theta):
    return 0.5 * a * b * math.sin(math.radians(theta))


dists = []

for m in range(spots):
    temp = []
    for n in range(m + 1, spots):
        print(f"{angles[m]}({m+1}) to {angles[n]}({n+1}) is {cosRule(1, 1, abs(angles[n] - angles[m]))}")
        temp.append(cosRule(1, 1, abs(angles[n] - angles[m])))
    if temp != []:
        dists.append(temp)

for i in dists:
    print(i)
# print(dists)



triangles = []

triangles.sort()
# pick posts-2 best triangles and sum

