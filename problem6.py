adTime = int(input().split()[1])
times = [int(i) for i in input().split()]
# DONT NEED tSum = sum([int(i) for i in times])

# SOME MAX NEEDED


#for n in range(len(times)):
#   print((tSum - int(times[(n - 1) % len(times)])) // adTime, end=" ")


# AFTER THESE INDEXES
splits = []
gVals = []

wTot = 0
for n in range(len(times)):
    wTot += times[n]
    if wTot >= adTime:
        splits.append(n)
        gVals.append(wTot)
        wTot = 0

tail = wTot

curSplit = 0

for n in range(len(times)):

    prev = (n - 1 + len(times)) % len(times)

    # start of group
    if prev in splits:
        print(len(splits) - 1, end=" ")
        #print(f"prev {prev} n {n} curSplit {curSplit}")
        if n in splits:
            curSplit += 1
        #print("PREV IN SPLITS")
        continue
    
    if n in splits:
        print(len(splits), end=" ")
        #print(f"prev {prev} n {n} curSplit {curSplit}")
        curSplit += 1
        #print("N IN SPLITS")
        continue

    if gVals[(curSplit - 1 + len(gVals)) % len(gVals)] - times[n] > adTime:
        print(len(splits), end=" ")
        #print(f"prev {prev} n {n} curSplit {curSplit}")
        #print("GVALS1 IN SPLITS")
        continue

    if (n <= splits[0]) or (n > splits[-1]) and ((gVals[(curSplit - 1 + len(gVals)) % len(gVals)] - times[n] < adTime) and (gVals[(curSplit - 1 + len(gVals)) % len(gVals)] - times[n] + tail >= adTime)):
        print(len(splits), end=" ")
        #print("FUNKY IN SPLITS")
        continue

    print(len(splits) - 1, end=" ")
    #print(f"prev {prev} n {n} curSplit {curSplit}")
    


    # tRAILING ENDS FFS