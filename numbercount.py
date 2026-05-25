lst = [1,2,2,3,1,4,2]
out = []

for i in lst:
    if i not in out:
        count = 0
        for j in lst:
            if i == j:
                count += 1
        print(i, ":", count)
        out.append(i)