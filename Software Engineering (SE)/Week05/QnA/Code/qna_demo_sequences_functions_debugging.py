"""
--- Coding a challenge solution
o	Employee Onboarding System with String, List, and Dictionary Operations
o	Objective: Build a system to manage employee onboarding details, 
    applying string manipulation, list operations, and dictionary usage 
    to handle employee data efficiently.

**  String Manipulation:
-   Concatenation: Combine employee first name and last name into a full name.
-	Slicing: Extract initials from employee names for identification.
-	Formatting: Display employee data (name, age, department, hobbies) in a clear format.
**  Lists:
-	Store a list of employee hobbies.
-	Manipulate the hobbies list through basic operations: indexing, slicing, appending, and removing.
-	Manage sales data for multiple weeks in a 2D list and perform operations on the weekly sales.
**  Dictionaries:
-	Store employee details like name, age, department, address, and hobbies as key-value pairs.
"""

# import modules
from tabulate import tabulate # Used in display_employee_data

# Step 1: String Manipulation

def create_full_name(first_name, last_name):
    """Concatenate first name and last name to form the full name."""
    return first_name + " " + last_name


def get_initials(first_name, last_name):
    """Extract initials from the first and last name."""
    return first_name[0] + last_name[0]


def display_employee_data(full_name, age, department, hobbies, sales):
    """Display employee data in a clean tabular format using tabulate."""
    # Create headers and data rows for tabulate
    employee_data = [
        ["Full Name:", full_name],
        ["Age:", age],
        ["Department:", department],
        ["Hobbies:", ", ".join(hobbies)],
    ]
    
    # Print the employee data in table format
    print("Employee Data:")
    print(tabulate(employee_data, tablefmt="plain"))
    
    # Display sales data for the employee
    print("\nSales Data (Weekly Sales):")
    sales_headers = ["Week", "Sales"]
    weekly_sales = [
        [f"Week {i+1}", sum(week)]  # Summing up sales for each week
        for i, week in enumerate(sales)
    ]
    print(tabulate(weekly_sales, headers=sales_headers, tablefmt="grid"))
    
# Step 2: Lists (Employee Hobbies and Sales Data)

def add_hobby(hobbies, new_hobby):
    """Add a new hobby to the hobbies list."""
    hobbies.append(new_hobby)
    return hobbies


def remove_hobby(hobbies, hobby):
    """Remove a hobby from the hobbies list."""
    if hobby in hobbies:
        hobbies.remove(hobby)
    return hobbies


def display_hobbies(hobbies):
    """Display the list of hobbies."""
    print("Employee Hobbies:", hobbies)


def calculate_total_sales(weekly_sales):
    """Calculate total sales for all weeks."""
    return sum(sum(week) for week in weekly_sales)


def calculate_average_sales(weekly_sales):
    """Calculate the average sales for each week."""
    return [sum(week) / len(week) for week in weekly_sales]
    # Generates a list of the answers for each week.

# Step 3: Dictionaries (Employee Information)

def create_employee(first_name, last_name, age, department, address, hobbies, sales):
    """Create a dictionary for storing employee details including sales data."""
    full_name = create_full_name(first_name, last_name)
    employee = {
        'name': full_name,
        'age': age,
        'department': department,
        'address': address,
        'hobbies': hobbies,
        'sales': sales  # Added sales data
    }
    return employee


def update_employee_info(employee, key, value):
    """Update a specific key-value pair in the employee dictionary."""
    employee[key] = value
    return employee


def display_employee_info(employee):
    """Display the employee's dictionary information."""
    print()
    print(f"** Employee Details:\n{employee}")


def get_employee_info(employee, key):
    """Fetch a specific value from the employee dictionary."""
    return employee.get(key)


def display_employee_items(employee):
    """Display all key-value pairs in the employee dictionary."""
    print("Employee Items:", employee.items())


def display_employee_keys(employee):
    """Display all keys of the employee dictionary."""
    print("Employee Keys:", employee.keys())


def display_employee_values(employee):
    """Display all values of the employee dictionary."""
    print("Employee Values:", employee.values())

# Step 4: Main Function to Control the Workflow

def main():
    # Print output header
    print("========= Employee Onboarding ========\n")
    # Initialise hobbies list and weekly sales data for the employee
    hobbies = ['reading', 'travelling', 'cycling', 'cooking']
    weekly_sales = [
        [100, 200, 150],  # Week 1
        [250, 300, 200],  # Week 2
        [300, 400, 350]   # Week 3
    ]
    
    # Adding and removing hobbies
    hobbies = add_hobby(hobbies, 'painting')
    display_hobbies(hobbies)
    hobbies = remove_hobby(hobbies, 'cooking')
    display_hobbies(hobbies)
    print()
    
    # Create full name, initials, and employee data display
    first_name = "John"
    last_name = "Doe"
    full_name = create_full_name(first_name, last_name)
    initials = get_initials(first_name, last_name)
    print(f"Full Name: {full_name}")
    print(f"Initials: {initials}\n")
    
    # Create employee with sales data
    employee = create_employee(first_name, last_name, 30, 'HR', 
                                '123 Elm Street', hobbies, weekly_sales)
    display_employee_data(full_name, 30, 'HR', hobbies, weekly_sales)
    
    # Perform sales-related calculations
    total_sales = calculate_total_sales(employee['sales'])
    print()
    print(f"Total Sales for All Weeks: {total_sales}")
    
    average_sales = calculate_average_sales(employee['sales'])
    # Print the average sales for each week
    for i, avg_sales in enumerate(average_sales, 1):
        print(f"Average Sales for Week {i}: {avg_sales}")
    
    # Update employee department and address
    employee = update_employee_info(employee, 'department', 'Sales')
    employee = update_employee_info(employee, 'address', '456 Oak Street')
    display_employee_info(employee)
    
    # Get specific employee data
    employee_age = get_employee_info(employee, 'age')
    print()
    print(f"Employee Age: {employee_age}")
    
    # Display employee keys, values, and items
    print()
    display_employee_items(employee)
    print()
    display_employee_keys(employee)
    display_employee_values(employee)
    

# Run the main function to execute the onboarding system
if __name__ == "__main__":
    main()
