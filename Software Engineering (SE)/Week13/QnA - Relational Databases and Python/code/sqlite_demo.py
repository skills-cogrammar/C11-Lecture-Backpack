import sqlite3


# ------------------------------ #
# Database Connection & Setup
# ------------------------------ #
def connect_db():
    """Establish connection to the SQLite database."""
    conn = sqlite3.connect("british_tea_shop.db")
    conn.execute("PRAGMA foreign_keys = ON;")  # Enforce foreign key constraints
    return conn


def create_tables(conn):
    """Create the database tables if they do not exist."""
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tea (
        tea_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        type TEXT NOT NULL,
        price DECIMAL(5,2) NOT NULL CHECK(price > 0)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT UNIQUE
    );
    """)
    """For the above, why not use customer_id INTEGER PRIMARY KEY AUTOINCREMENT?

    AUTOINCREMENT:
    - Ensures that customer_id values are never reused, even after deletion.
    - Gaps in IDs remain (e.g., if customer #3 is deleted, the next will be #4, not #3).
    - Slower inserts because SQLite maintains an internal counter to prevent ID reuse.
    
    NO AUTOINCREMENT:
    - Still generates unique IDs automatically, but…
    - Deleted IDs can be reused. If the highest ID was 10 and you delete customer #10, 
      the next customer might get ID 10 again.
    - Faster inserts since SQLite doesn't need to track past deletions.
    """

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        tea_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL CHECK(quantity > 0),
        order_date TEXT DEFAULT CURRENT_DATE,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE,
        FOREIGN KEY (tea_id) REFERENCES Tea(tea_id) ON DELETE CASCADE
    );
    """)

    conn.commit()


# ------------------------------ #
# Import Tea Data from File
# ------------------------------ #
def import_tea_data(conn, filename="tea_list.txt"):
    """Read tea varieties from a text file and insert them into the Tea table."""
    cursor = conn.cursor()
    
    try:
        with open(filename, "r") as file:
            for line in file:
                name, type_, price = line.strip().split(",")
                cursor.execute("""INSERT OR IGNORE INTO Tea (name, type, price)
                                    VALUES (?, ?, ?);""", 
                                    (name, type_, float(price)))

        conn.commit()
        print("[INFO] Tea data imported successfully.")

    except FileNotFoundError:
        print("[ERROR] File not found. Ensure 'tea_list.txt' exists in the directory.")


# ------------------------------ #
# CRUD Operations
# ------------------------------ #
def add_customer(conn, name, phone):
    """Insert a new customer if they don't already exist, and return their customer ID."""
    cursor = conn.cursor()

    # Check if the customer already exists (using phone as a unique identifier)
    cursor.execute("SELECT customer_id FROM Customers WHERE phone = ?;", (phone,))
    existing_customer = cursor.fetchone()

    if existing_customer:
        print(f"[INFO] Returning customer: {name} (ID: {existing_customer[0]})")
        return existing_customer[0]  # Return existing customer's ID
    else:
        # Insert new customer
        cursor.execute("INSERT INTO Customers (name, phone) VALUES (?, ?);", (name, phone))
        conn.commit()
        customer_id = cursor.lastrowid  # Get the auto-generated ID
        print(f"[INFO] New customer added: {name} (ID: {customer_id})")
        return customer_id


def place_order(conn, customer_id, tea_id, quantity):
    """Insert a new order into the Orders table."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Orders (customer_id, tea_id, quantity) VALUES (?, ?, ?);",
                   (customer_id, tea_id, quantity))
    conn.commit()


def get_orders(conn):
    """Retrieve all orders with customer and tea details."""
    cursor = conn.cursor()
    cursor.execute("""
    SELECT Orders.order_id, Customers.name, Tea.name, Orders.quantity, Tea.price, Orders.order_date 
    FROM Orders
    JOIN Customers ON Orders.customer_id = Customers.customer_id
    JOIN Tea ON Orders.tea_id = Tea.tea_id;
    """)
    
    return cursor.fetchall()


def update_order_quantity(conn, order_id, new_quantity):
    """Update the quantity of an order."""
    cursor = conn.cursor()
    cursor.execute("UPDATE Orders SET quantity = ? WHERE order_id = ?;", (new_quantity, order_id))
    conn.commit()


def delete_order(conn, order_id):
    """Delete an order from the Orders table after verifying its existence."""
    cursor = conn.cursor()

    # Check if the order exists
    cursor.execute("SELECT 1 FROM Orders WHERE order_id = ?;", (order_id,))
    order_exists = cursor.fetchone()

    if order_exists:
        cursor.execute("DELETE FROM Orders WHERE order_id = ?;", (order_id,))
        conn.commit()
        print(f"[INFO] Order #{order_id} has been deleted.")
    else:
        print(f"[WARNING] Order #{order_id} does not exist. No action taken.")


# ------------------------------ #
# Main Execution
# ------------------------------ #
if __name__ == "__main__":
    with connect_db() as conn:  # Auto-closes DB connection when block exits
        create_tables(conn)
        import_tea_data(conn)

        # Adding a customer (prevents duplicates)
        customer_id = add_customer(conn, "Mr. Arthur Pennyworth", "07123456789")

        # Placing an order
        place_order(conn, customer_id, 1, 2)  # 2 x Earl Grey (assuming ID 1)

        # Displaying orders
        orders = get_orders(conn)
        for order in orders:
            print(f"Order #{order[0]}: {order[1]} ordered {order[3]}x {order[2]} (£{order[4]} each) on {order[5]}")

        # Updating an order
        update_order_quantity(conn, 1, 3)

        # Deleting an order (with existence check)
        delete_order(conn, 1)

        # Deleting an order that does not exist
        delete_order(conn, 100)

