## Naming Conventions

### **1. Variable Names**
- **Use Descriptive Names**: Choose names that clearly describe the purpose of the variable.
  - **Good Example**: `total_price`, `user_age`
  - **Bad Example**: `tp`, `ua`

- **Use Lowercase with Underscores**: Variable names should be in lowercase letters, with words separated by underscores.
  - **Example**: `total_price`, `user_age`

### **2. Function Names**
- **Use Lowercase with Underscores**: Function names should be in lowercase with words separated by underscores.
  - **Example**: `calculate_total_price()`, `get_user_age()`

### **3. Class Names**
- **Use CamelCase**: Class names should follow the CamelCase convention, where each word starts with an uppercase letter and there are no underscores.
  - **Example**: `UserProfile`, `InvoiceManager`

### **4. Constants**
- **Use Uppercase with Underscores**: Constants should be written in uppercase letters with words separated by underscores.
  - **Example**: `MAX_RETRIES`, `DEFAULT_TIMEOUT`

### **5. Module and Package Names**
- **Use Short, Lowercase Names**: Module and package names should be short and written in lowercase. Use underscores if it improves readability.
  - **Example**: `data_processor`, `user_utils`

### **6. File Names**
- **Use Lowercase with Underscores**: File names should be in lowercase with words separated by underscores to enhance readability.
  - **Example**: `data_processing.py`, `user_management.py`

---

## Style Guide

### **1. Comments**
- **Write Clear and Helpful Comments**: Use comments to explain the purpose of your code. Comments should be complete sentences and be clear and helpful.
  - **Inline Comments**: Use these for short comments on the same line as the code.
    - **Example**: `total_price = subtotal + tax  # Add tax to subtotal`
  - **Block Comments**: Use these for longer explanations, placed above the code they refer to.
    - **Example**:
      ```python
      # This function calculates the total price including tax.
      # It takes the subtotal and tax rate as arguments.
      def calculate_total_price(subtotal, tax_rate):
          return subtotal + (subtotal * tax_rate)
      ```

### **2. Docstrings**
- **Use Triple Quotes**: Document your functions, classes, and modules using triple double quotes. This helps other users understand the purpose and usage of your code.
  - **Example**:
    ```python
    def calculate_total_price(subtotal, tax_rate):
        """
        Calculate the total price including tax.

        Args:
            subtotal (float): The initial price before tax.
            tax_rate (float): The tax rate to apply.

        Returns:
            float: The total price after tax.
        """
        return subtotal + (subtotal * tax_rate)
    ```

### **3. Indentation and Spacing**
- **Use Four Spaces per Indentation Level**: Follow the standard practice of using four spaces for each level of indentation.
- **Avoid Mixing Tabs and Spaces**: Consistently use spaces or tabs, but not both.

### **4. Line Length**
- **Limit Lines to 79 Characters**: Keep lines of code within 79 characters to ensure readability on various devices and editors.

### **5. Avoid Magic Numbers**
- **Use Named Constants**: Instead of hardcoding numbers directly into your code, use named constants to give them context.
  - **Example**: Instead of `if age > 18:`, use `if age > LEGAL_DRINKING_AGE:`

---

By following these **Naming Conventions**, you'll ensure that your code is easily understandable and maintainable. Adhering to the **Style Guide** will help keep your code clean, readable, and consistent. For more detailed guidelines, refer to the [PEP 8 Style Guide](https://pep8.org) and [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).