import sqlite3


# Function to establish a connection to the database
def connect_db():
    return sqlite3.connect("shop.db")


# Function to create necessary tables in the database
def create_tables():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.executescript("""
            -- Enable foreign key constraints to maintain referential integrity
            PRAGMA foreign_keys = ON;

            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY,
                customer_name VARCHAR(50) NOT NULL,
                customer_address VARCHAR(50) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                product_name VARCHAR(255) NOT NULL,
                product_category VARCHAR(255) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                customer_id INT,
                product_id INT,
                quantity INT NOT NULL,
                order_date DATE NOT NULL,
                -- Ensure customer_id exists in customer table
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                -- Ensure product_id exists in products table
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            );
        """)
        conn.commit()
        print("Tables created successfully.")


# Function to insert a new customer into the customers table
def insert_customer(customer_id, name, address):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO customers VALUES (?, ?, ?)", 
                       (customer_id, name, address))
        conn.commit()
        print(f"Customer {name} added successfully.")


# Function to insert a new product into the products table
def insert_product(product_id, name, category):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO products VALUES (?, ?, ?)", 
                       (product_id, name, category))
        conn.commit()
        print(f"Product {name} added successfully.")


# Function to insert a new product into the products table
def insert_order(customer_id, product_id, quantity, order_date):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT OR REPLACE INTO orders
                       (customer_id, product_id, quantity, order_date)
                       VALUES (?, ?, ?, ?)""",
                       (customer_id, product_id, quantity, order_date))
        conn.commit()
        print(f"Order for customer {customer_id} placed successfully.")


# Function to fetch orders for a specific customer
def fetch_customer_orders(customer_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT orders.order_id, orders.product_id, orders.quantity,
                       customers.customer_name, customers.customer_address,
                       products.product_name, orders.order_date
            FROM orders
            -- Join orders with customers table to get customer details
            INNER JOIN customers ON orders.customer_id = customers.customer_id
            -- Join orders with products table to get product details
            INNER JOIN products ON orders.product_id = products.product_id
            WHERE customers.customer_id = ?;
        """, (customer_id,))

        results = cursor.fetchall()
        print(f"\nOrders for Customer {customer_id}:\n")
        for row in results:
            print(row)
        print()
        return results


# Function to update a customer's address
def update_customer_address(customer_id, new_address):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""UPDATE customers SET customer_address = ?
                       WHERE customer_id = ?""", (new_address, customer_id))
        conn.commit()
        print(f"Customer {customer_id}'s address updated to {new_address}.")


# Function to delete an order from the orders table
def delete_order(order_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM orders WHERE order_id = ?", (order_id,))
        conn.commit()
        print(f"Order {order_id} deleted successfully.")


# Example usage to demonstrate CRUD operations
if __name__ == "__main__":
    create_tables()  # Create tables if they do not exist
    insert_customer(100, "John Poe", "123 Elm Str, NY")  # Insert a sample customer
    insert_product(2002, "Thingamajig", "Gadgets")  # Insert a sample product
    insert_order(100, 2002, 10, "2024-05-25")  # Insert a sample order
    fetch_customer_orders(100)  # Fetch and print orders for customer 100
    update_customer_address(100, "321 Birch St, NY")  # Update customer address
    delete_order(1)  # Delete an order by order_id
