def main():
    print(" ")
    print("================================================")
    print("ATM BANKING SIMULATOR")
    print("================================================")
    print(" ")
    print("WELCOME TO PYTHON BANK")
    print(" ")
    print("================================================")
    print(" ")
    print("1. Check Account Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Account Details")
    print("6. Exit")
    print(" ")
    choice = input("Enter your choice: ")


    account_holder = "Dev Dass"
    account_number = "123456789"
    balance = 50000


# ============================
#    Check Acoount Balance
# ============================

    if choice == "1":
        print("\n========== ACCOUNT BALANCE ==========")
        print(f"\nAccount Holder: {account_holder}")
        print(f"Account Number: {account_number}")
        print(f"\nAvailable Balance: Rs. {balance:,}")
        print("\n===============================================")

        
# ============================
#       Deposit Money
# ============================

    elif choice == "2":
        print(" ")
        print("========== DEPOSIT MONEY ==========")
        print(" ")

        deposit = int(input("Enter deposit amount: "))
        if deposit<0:
            print(" ")
            print("Error: Deposit amount must be greater than zero!")
            print(" ")
            print("Transaction cancelled.")
        
        else:
            balance = balance+deposit
            with open("transactions.txt", "a") as file:
                file.write("\nType: Deposit")
                file.write(f"\nAmount: Rs. {deposit:,}")
                file.write(f"\nBalance after Transaction Rs.{balance}")
                file.write("\n")

            print(" ")
            print("Deposit successful!")
            print(" ")
            print("Transaction Details:")
            print(" ")
            print("Transaction Type: Deposit")
            print(f"Deposited Amount: {deposit}")
            print(f"Previous Balance:{balance-deposit}")
            print(f"New Balance: {balance}")
            print(" ")
            print("===============================================")


# ============================
#       Withdraw Money
# ============================

    elif choice == "3":
        print(" ")
        print("========== WITHDRAW MONEY ==========")
        print(" ")

        withdrawal = input("Enter withdrawal amount: ")

        if not withdrawal.isdigit():
            print("Error: Invalid amount!")
            print(" ")
            print("Please enter numbers only.")
            print(" ")
            print("===============================================")

        else:
            withdrawal = int(withdrawal)

            if withdrawal <= 0:
                print("Error: Amount must be greater than zero!")

            elif withdrawal > balance:
                print("Transaction Failed!")
                print(" ")
                print("Error: Insufficient account balance!")
                print(" ")
                print(f"Available Balance: {balance:,}")

            else:
                previous_balance = balance
                balance = balance - withdrawal

                with open("transactions.txt", "a") as file:
                    file.write("\nType: Withdrawal")
                    file.write(f"\nAmount Rs. {withdrawal:,}")
                    file.write(f"\nBalance after Transaction: Rs. {balance:,}")
                    file.write("\n")

                print(" ")
                print("Withdrawal successful!")
                print(" ")
                print("Transaction Details:")
                print(" ")
                print("Transaction Type: Withdrawal")
                print(f"Withdrawn Amount: {withdrawal:,}")
                print(f"Previous Balance: {previous_balance:,}")
                print(f"New Balance: {balance:,}")
                print(" ")
                print("===============================================")
# ============================
#    Transaction History
# ============================

    elif choice == "4":
        print(" ")
        print("========== TRANSACTION HISTORY ==========")
        print(" ")
        transaction_no = 1 

        with open("transactions.txt", "r") as file:
            for line in file:
                line = line.strip() #Remove the primary space and end space

                if line == "":
                    continue

                if "Type:" in line:
                    print(f"Transaction {transaction_no}")
                    print(" ")
                    print(line)
                    transaction_no = transaction_no + 1

                elif "Balance" in line:
                    print(line)
                    print(" ")
                    print("-----------------------------------------------")
                    print(" ")

                else:
                    print(line)

            print(f"Total Transactions: {transaction_no - 1 }")
            print("===============================================")


# ============================
#    Check Acoount Details
# ============================

    elif choice == "5":
        print(" ")
        print("========== ACCOUNT DETAILS ==========")
        print("\n")

        with open("accounts.txt", "r") as file:
            for line in file:
                line = line.strip()
                print(line)

            print(" ")
            print(f"Current Balance: Rs.{balance}")
            print(" ")
            print("Account Status: Active")
            print(" ")
            print("===============================================")
            print(" ")

    elif choice =="6":
        print("===============================================")
        print(" ")
        print("Thank you for using")
        print("PYTHON BANK ATM!")
        print(" ")
        print("Your transaction history has been saved.")
        print(" ")
        print("Please collect your card.")
        print(" ")
        print("Goodbye!")
        print(" ")
        print("===============================================")

# ============================
#    Exit
# ============================

    else:
        print(" ")
        print("Error: Invalid choice!")
        print(" ")
        print("Please select between 1 and 6.")   
        print(" ")   
        print("===============================================")   
            
#Its calling the function
main()