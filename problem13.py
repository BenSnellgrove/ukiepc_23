squares, stiles, corners = input().split()
squares = int(squares)
stiles = int(stiles)
corners = int(corners)

finalResult = 0

if corners%2 == 1:
    corners -= 1

if corners >= 2:
    finalResult += 2*stiles

finalResult += squares*2
finalResult += (corners*3)//2

print(finalResult)