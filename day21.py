# random password generator
import random
import string 
characters = string.ascii_letters + string.digits + string.punctuation
n = int(input("Enter number of digits :  "))
password = " " 
for i in range(n):
    password += random.choice(characters)
print(password)

# ATM
Balance = 0

p1 = int(input("Enter the pin: "))

if len(str(p1)) != 4:
    print("PIN must contain 4 digits")
else:
    p2 = int(input("Re-enter the pin: "))

    if p1 == p2:
        print("PINs created successfully")

        while True:
            print("1. Balance Enquiry")
            print("2. Amount Deposit")
            print("3. Amount Withdraw")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Your balance is:", Balance)

            elif choice == 2:
                amount = int(input("Enter amount to deposit: "))
                Balance = Balance + amount
                print("Amount deposited successfully")
                print("Current balance:", Balance)

            elif choice == 3:
                amount = int(input("Enter amount to withdraw: "))

                if amount <= Balance:
                    Balance = Balance - amount
                    print("Please collect your cash")
                    print("Remaining balance:", Balance)
                else:
                    print("Insufficient balance")

            elif choice == 4:
                print("Thank you for using our ATM!")
                break

            else:
                print("Invalid choice")

    else:
        print("PINs do not match")