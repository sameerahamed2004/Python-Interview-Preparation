number=153
temp=number
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp=temp//10
if number==sum:
    print(f"{number} is a armstrong number")
else:
    print(f"{number} is not a armstrong number")

    