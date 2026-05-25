lst=[18, 5, 8, 20, 15 ,19]
large=lst[0]
second=0
for i in lst:
    if large<i:
        second=large 
        large=i
    elif i>second and i!=large:
        second=i
print(second)
