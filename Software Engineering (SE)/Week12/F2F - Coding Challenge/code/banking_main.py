"""
***** Basic Banking System *****

Successfully build a Basic Banking System, 
by following a structured approach that ensures collaboration and 
leverages key programming concepts. 

*   Start by defining the core classes (e.g., User, Account, Transaction) 
    using Object-Oriented Programming principles. 

*   Assign team members to work on specific components: 
    as an example, one member or group of members can handle account creation 
    and balance management, another can implement deposit/withdrawal logic 
    with conditionals, and a third can focus on file handling to save 
    transaction history. 
    
*   Use loops for repetitive tasks like displaying account details or 
    processing transactions. 

*   Ensure functions are created for modularity 
    (e.g., deposit(), withdraw(), view_balance()). 
    
*   Regularly integrate individual contributions into a shared codebase, 
    and test each feature as it's developed. 
    
*   Finally, prepare a brief presentation highlighting the implementation, 
    challenges faced, and solutions applied. 
    
*   This approach ensures everyone contributes while reinforcing key skills.
"""


# Class for a user account
class UserAccount:
    def __init__(self, username, initial_balance = 0):
        self.username = username
        self.balance = initial_balance
        self.transaction_history = []


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: £{amount}")
            print(f"Deposited £{amount} successfully.")
        else:
            print("Deposit amount must be greater than 0.")


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: £{amount}")
            print(f"Withdrew £{amount} successfully.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


    def view_balance(self):
        print(f"Current balance: £{self.balance}")


    def save_transaction_history(self):
        filename = f"{self.username}_transactions.txt"
        with open(filename, "w") as file:
            for transaction in self.transaction_history:
                file.write(transaction + "\n")
        print(f"Transaction history saved to {filename}")


# Class for managing multiple accounts
class BankSystem:
    def __init__(self):
        self.accounts = {}


    def create_account(self, username, initial_balance = 0):
        if username in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[username] = UserAccount(username, initial_balance)
            print(f"Account created for {username}.")

            
    def get_account(self, username):
        return self.accounts.get(username, None)


# Main function to simulate the banking system
def main():
    bank = BankSystem()
    while choice != '6':
        print("\n--- Basic Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. Save Transaction History")
        print("6. Exit")

        choice = input("Choose an option (1 - 6): ")

        if choice == '1':
            username = input("Enter username: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(username, initial_balance)
        elif choice in ['2', '3', '4', '5']:
            username = input("Enter username: ")
            account = bank.get_account(username)
            if account:
                if choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                elif choice == '4':
                    account.view_balance()
                elif choice == '5':
                    account.save_transaction_history()
            else:
                print("Account not found.")
        elif choice == '6':
            print("Exiting the banking system. Goodbye!")
            continue
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()