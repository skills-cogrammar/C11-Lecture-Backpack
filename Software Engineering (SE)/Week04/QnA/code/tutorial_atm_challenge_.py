"""
Objective: Simulate an ATM withdrawal process where a user can make a valid withdrawal. The system allows the user up to 3 attempts to enter a valid amount, ensuring the withdrawal is within their balance.
Major Steps:
- Initialise the balance: 
Set a starting balance for the user (e.g., £1000).
- Set a maximum number of attempts: 
Allow the user 3 attempts to enter a valid withdrawal amount.
- Check withdrawal validity: 
Ensure the withdrawal is positive and less than or equal to the available balance.
- Update balance: 
After a valid withdrawal, update the balance and show the new amount.
- Handle invalid inputs: 
If the withdrawal is invalid, decrease the remaining attempts and notify the user.
"""

# Simulate ATM withdrawal process

# Step 1: Initialise the balance
balance = 1000  # Starting balance £1000

# Step 2: Set a maximum number of attempts
max_attempts = 3

# Step 3: Start the withdrawal process
attempts = 0

while attempts < max_attempts:
    # Prompt the user for the withdrawal amount
    withdrawal_amount = float(input("Enter the amount to withdraw: £"))
    
    # Step 4: Check withdrawal validity
    if withdrawal_amount > 0 and withdrawal_amount <= balance:
        # Update balance after a valid withdrawal
        balance -= withdrawal_amount
        print(f"Withdrawal successful! Your new balance is: £{balance:.2f}")
        break  # Exit the loop after successful withdrawal
    else:
        # Handle invalid input
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if withdrawal_amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        elif withdrawal_amount > balance:
            print(f"Insufficient funds. Your current balance is £{balance:.2f}.")
        
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempt(s) left.")
        else:
            print("You have exceeded the maximum number of attempts. Please try again later.")


