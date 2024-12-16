# ===== Basic List Operations

# Initial list of hobbies
hobbies = ["reading", "hiking", "painting"]

# Indexing: Access the first hobby
first_hobby = hobbies[0]
print(f"First hobby: {first_hobby}")  # Output: reading

# Slicing: Get the first two hobbies
first_two_hobbies = hobbies[:2]
print(f"First two hobbies: {first_two_hobbies}")  # Output: ['reading', 'hiking']

# Appending: Add a new hobby
hobbies.append("cycling")
print(f"Updated hobbies: {hobbies}")  # Output: ['reading', 'hiking', 'painting', 'cycling']

# Removing: Remove a hobby
hobbies.remove("hiking")
print(f"Updated hobbies: {hobbies}")  # Output: ['reading', 'painting', 'cycling']

# Removing: Remove the last hobby using pop
hobbies.pop()
print(f"Updated hobbies: {hobbies}")  # Output: ['reading', 'painting']

# Removing: Remove the first hobby
hobbies.pop(0)
print(f"Updated hobbies: {hobbies}")  # Output: ['painting']


# ===== String Operations with Employee Data

# Employee data
first_name = "John Tim"
last_name = "Mark Harris"
age = 30
dept = "commercial"
address = "123 Main St, Anytown, USA 12345"
company = "xyz"
hobbies = ["reading", "hiking", "photography", "cooking"]

# Concatenation: Create the full name
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Slicing and uppercase: Get employee initials
initials = (first_name[0] + last_name[0]).upper()
print(f"Employee initials: {initials}")

# Email creation using string concatenation and formatting
email = f"{first_name.split()[0].lower()}.{last_name.split()[0].lower()}@{company.lower()}.com"
print(f"Email: {email}")

# Address formatting
street = address.split(',')[0]
city = address.split(', ')[1].strip()
print(f"Street: {street}")
print(f"City: {city}")

# Slicing: Extract zip code from the address
zip_code = address[-5:]
print(f"Zip code: {zip_code}")

# Formatting the employee info string
employee_info = "Employee: {}, Age: {:02d}, Department: {} enjoys {}".format(full_name, age, dept, ', '.join(hobbies))
print(employee_info)

# ===== List operations on sales
print("\nOperations on sales list:")

# 2D List Operations with Sales Data

# Sales data: Week 1, Week 2, Week 3 (monday, tuesday, wednesday, thursday, friday)
sales_data = [
    [30, 0, 120, 0, 130],  # Week 1
    [40, 0, 110, 0, 90],   # Week 2
    [50, 0, 160, 0, 200],  # Week 3
]

# Indexing: Access sales data for specific days
print(f"Number of sales on Monday in Week 2: {sales_data[1][0]}")
print(f"Number of sales on Friday in Week 3: {sales_data[2][4]}")

# Slicing: Get sales for Monday and Tuesday in Week 2
print(f"Sales on Monday and Tuesday in Week 2: {sales_data[1][:2]}")

# Adding Week 4 data to the sales_data list
sales_data.append([])  # Week 4
for i in range(5):  # Populate with sales data for Week 4
    sales_data[3].append(i)

print(f"sales == {sales_data[3]}") # Output: [0, 1, 2, 3, 4]

# Updating specific days in Week 4
sales_data[3][0] = 39  # Monday
sales_data[3][2] = 15  # Wednesday
sales_data[3][4] = 151  # Friday
print(f"Updated Week 4 sales: {sales_data[3]}")

# Calculate the sales per week using nested loops
sales_per_week = []
for week in sales_data:
    total = 0
    for sale in week:
        total += sale
    sales_per_week.append(total)
print(f"Sales per week: {sales_per_week}")


# ====== Dictionary Operations with Employee Data

# Employee data stored in a dictionary
john = {
    "first_name": "John Tim",
    "last_name": "Mark Harris",
    "age": 30,
    "dept": "commercial",
    "address": "123 Main St, Anytown, USA 12345",
    "hobbies": ["reading", "hiking", "photography", "cooking"]
}

# Accessing values from the dictionary
print(f"Full Name: {john['first_name']} {john['last_name']}")
print(f"Age: {john['age']}")
print(f"Department: {john['dept']}")

# Modifying dictionary values
john["dept"] = "marketing"
print(f"Updated Department: {john['dept']}")

# Adding a new key-value pair
john["email"] = "john.tim@xyz.com"
print(f"Email: {john['email']}")

# How to update the hobbies values in the dictionary
# Long way
change_hobbies = john["hobbies"]
change_hobbies[1] = "fishing"
john["hobbies"] = change_hobbies
# Short cut
john["hobbies"][1] = "toe counting"

print(john["hobbies"])
