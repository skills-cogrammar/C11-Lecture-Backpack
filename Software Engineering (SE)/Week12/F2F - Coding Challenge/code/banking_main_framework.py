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
        # Initialise username, balance, and transaction history
        pass


    def deposit(self, amount):
        # Add amount to balance and record transaction
        pass


    def withdraw(self, amount):
        # Subtract amount from balance (if valid) and record transaction
        pass


    def view_balance(self):
        # Display the current balance
        pass


    def save_transaction_history(self):
        # Save transaction history to a file
        pass


# Class for managing multiple accounts
class BankSystem:
    def __init__(self):
        # Initialise a dictionary to store user accounts
        pass


    def create_account(self, username, initial_balance = 0):
        # Create a new user account and add it to the dictionary
        pass


    def get_account(self, username):
        # Retrieve a user account from the dictionary
        pass


# Main function to simulate the banking system
def main():
    # Create a BankSystem instance
    bank = BankSystem()
    choice = None

    while choice != '6':
        # Display menu options
        print("\n--- Basic Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. Save Transaction History")
        print("6. Exit")

        # Get user choice
        choice = input("Choose an option (1 - 6): ")

        if choice == '1':
            # Handle account creation
            pass
        elif choice in ['2', '3', '4', '5']:
            # Handle deposit, withdraw, view balance, and save history
            pass
        elif choice == '6':
            # Exit the program
            continue
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
    