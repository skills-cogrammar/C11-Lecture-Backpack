"""
OBJECTIVE: Build a simple checkout system for an e-commerce store. 
When a customer checks out, they need to enter their age, 
total order price, and account balance. 

The system will categorise them into an age group and apply 
a discount if they qualify. 
Then it will check if the balance is sufficient to complete the purchase, 
taking into account any applicable discounts.

Steps to Implement: 
- Take User Inputs:
  Get the customer's age, total order price, and account balance.
- Categorise Age and Apply Discount:
  If the customer is aged 18-25, apply a 10% discount.
  If the customer is aged 26-60, apply a 5% discount.
  If the customer is under 18 or over 60, no discount is applied.
- Calculate Discounted Price:
  Adjust the total order price based on the applicable discount.
- Check Balance:
  Compare the customer’s account balance with the discounted price.
  If the balance is enough, proceed with the order. 
  If the balance is insufficient, calculate the shortfall and inform the user.
"""

# --> Step 1: Take User Inputs
# Prompt the user to input their age, total order price, and account balance
# This step ensures the program dynamically adjusts based on user input
age = int(input("Enter your age: "))
order_price = float(input("Enter the total order price: £")) # Alt+ 0163 for £
account_balance = float(input("Enter your account balance: £"))

# --> Step 2: Categorise Age and Apply Discount
# Age categorisation and discounts:
# Uses conditional statements to apply discounts based on the user's age
# Ensures appropriate logic for each age group
discount_percentage = 0  # Initialise the discount as 0

if 18 <= age <= 25:
    discount_percentage = 10  # 10% discount for ages 18-25
elif age <= 60:
    discount_percentage = 5   # 5% discount for ages 26-60
# else:                        # discount_persentage already 0 from initialise
#     discount_percentage = 0  # No discount for others

# --> Step 3: Calculate Discounted Price
# Dynamic calculations:
# Calculates the discount and adjusts the total order price accordingly
discount_amount = (discount_percentage / 100) * order_price
discounted_price = order_price - discount_amount

# Display the applied discount and the new total price to the user
print(f"\nDiscount applied: {discount_percentage}%")
print(f"Discounted total: £{discounted_price:.2f}")

# --> Step 4: Check Balance
# Balance check:
# Verifies if the user has enough funds and provides clear feedback on 
# their financial status for the transaction
if account_balance >= discounted_price:
    # If the balance is sufficient, confirm the purchase
    print("Purchase successful! Thank you for shopping with us!")
else:
    # If the balance is insufficient, calculate the shortfall and inform the user
    shortfall = discounted_price - account_balance
    print(f"Insufficient balance. You need an additional £{shortfall:.2f} to complete the purchase.")

# User interaction: Provide clear prompts for input and output messages 
# to make the system user-friendly
