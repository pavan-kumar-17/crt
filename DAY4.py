size=int(input("Enter the size of list : "))
age=[]
for i in range (size):
    ele=int(input("Enter the age : "))
    age.append(ele)
print(age)
for i in age:
    if(i>=1 and i<=100):
        if(i<12):
            print(f"{i}---------->$10")
        elif(i>=12 and i<=60):
            print(f"{i}----------->$15")
        else:
            print(f"{i}------------>$20")
bank atm
pin=int(input("Enter the pin: "))
acc_bal=0
if pin==1703:
    print("Welcome to the magadha bank")
#  Deposit,withdraw,balance inquire and exit.
    while True:
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Balance Enquiry")
        print("4.Exit")

        choice=int(input("Enter Your Choice :"))
        print("\n")
        if(choice==1):
            amount=int(input("Enter the amount to Deposit : "))
            acc_bal=acc_bal+amount
            print(f"Dear customer your account xxx4567 is credited with {amount}")
        elif(choice==2):
            amount=int(input("Enter the amount to Withdraw"))
            if(amount<acc_bal):
                print(f"Dear custmer your account xxxx4567 is debited with {amount}")
                acc_bal=acc_bal-amount
            else:
                print("Insufficient balance........!")
        elif(choice==3):
            print(f"Dear customer your account xxxxxxxxxxxxxxx4567 has {acc_bal}.")
        else:
            print("Thank You.......!")
            break
else:
    print("you Entered wromg pin.")






List=[i for i in range(2,10,2) ]
set={i for i in range(2,10,2)}
print(List)
print(sorted(set))



import copy
original=[1,2,3,4,5]
print(original)
new=original
print(new)
new[0]=100
print(original)
print(new)

a=[1,2,35,6,5,8,99,66]
print(a)
a.append(5)
print(a)
a.insert(2,85)
print(a)
a.remove(2)
print(a)
a.pop()
print(a)
a.pop(0)
print(a)

