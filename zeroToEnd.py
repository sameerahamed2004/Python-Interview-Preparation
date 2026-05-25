lst=[1,0,2,0,3,0,4]
out=[]
for i in lst:
    if i<1:
        lst.remove(i)
        lst.append(i)
print(lst)
