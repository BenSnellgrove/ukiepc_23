adTime = int(input().split()[1])
times = [int(i) for i in input().split()]
# DONT NEED tSum = sum([int(i) for i in times])

# SOME MAX NEEDED


#for n in range(len(times)):
#   print((tSum - int(times[(n - 1) % len(times)])) // adTime, end=" ")






for n in range(len(times)):
    groups = []
    rTot = 0
    temp = []

    tTimes = times[n:] + times[:n]

    # print(tTimes)


    for i in tTimes:
        temp.append(i)

        if sum(temp) >= adTime:
            groups.append(temp)
            temp = []

    print(len(groups) - (1 if temp == [] else 0), end=" ")