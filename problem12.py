class Robot:
    def __init__(self, sting):
        split = sting.split()
        self.health = int(split[0])
        self.damage = int(split[1])
        self.max_reload = int(split[2])
        self.reload = 0

p1 = Robot(input())
p2 = Robot(input())

while p1.health > 0 and p2.health > 0:
    time = min(p1.reload, p2.reload)
    p1.reload -= time
    p2.reload -= time

    if p1.reload == 0:
        p2.health -= p1.damage
        p1.reload = p1.max_reload
    if p2.reload == 0:
        p1.health -= p2.damage
        p2.reload = p2.max_reload

if p1.health <= 0 and p2.health <= 0:
    print("draw")
elif p2.health <= 0:
    print("player one")
else:
    print("player two")