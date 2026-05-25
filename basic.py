# # Reverse a string
# s="sameer"
# space=""
# for i in s:
#     space=i+space
# print(space)
# # Check if a string is palindrome
# s="madam"
# space=""
# for i in s:
#     space=i+space
# if space==s:
#     print("its palindrome")
# else:
#     print("its not a palindrome")
# # Find factorial of a number
# num=5
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

# # Print Fibonacci series up to N

# a=0
# b=1
# for i in range(9):
#     print(a)
#     a,b=b,a+b


# Check if a number is prime

# Count vowels in a string

# Find sum of digits of a number

# Swap two numbers without using third variable

# Check Armstrong number

# Find largest of three numbers



# lst=[1,2,3,4,5,6,7,8,9]
# target=6
# sample=lst[0]
# out=[]
# for i in lst:
#     if i+sample==target:
#         out.append((i,sample))
# print(int(out))














class bank:
    pin=1234
    
    
    while True:
      password=int(input("Enter the pin : "))
      if pin==password:
       print("Welcome to the bank")
       break
      else:
        print("wrong pin")
        print("Try again")
    balance=40000
    while True:
      
      print("1 to check balance")
      print("2 to debit the amount")
      print("3 to credit the amount")
      print("4 to exit")
      opt=int(input("Enter the option : "))
      if opt==1:
        print(balance)
      elif opt==2:
        amount=int(input("Enter the amount : "))
        if amount<=balance:
            balance=balance-amount
            print("successfully withdraw")
        else:
            print("low balance")
      elif opt==3:
        amount1=int(input("Enter the amount : "))
        if amount1>=balance:
            balance=balance+amount1
            print("successfully credited")
      elif opt==4:
        print("Thank you visit again")
        break
    

    

    

    
   