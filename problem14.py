# done

import random

def createName():
    name = ""

    for c in str(len(names)):
        name += chr(ord('a') + int(c))

    return name

data = []
for n in range(int(input())):
    givenData = input()[:-1]
    data.append(float(givenData))

names = {0.75:"standard", 12:"balthazar", 15:"nebuchadnezzar"}

'''
For each bottle size, check if its in the dict, 
if it is print its name, if it isnt give it a name and add to dict
'''
for bottle in data:
    if bottle in names:
        print(names[bottle])
    else:
        names[bottle] = createName()
        print(names[bottle])