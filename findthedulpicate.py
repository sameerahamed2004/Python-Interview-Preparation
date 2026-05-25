lst=[1,2,3,2,4,5,1]
out=[]
for i in lst:
    if i not in out:
        out.append(i)
print(out)