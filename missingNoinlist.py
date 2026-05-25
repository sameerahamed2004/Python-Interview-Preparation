lst=[1,2,3,5,6,8,10]
large=lst[0]
out=[]
for i in lst:
    if large<i:
        large=i
for j in range(1,large+1):
    if j not in lst:
        out.append(j)
print(",".join(map(str,out)))