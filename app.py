import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("users.db", isolation_level=None)

# Create the users table if it doesn’t exist
with conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)
print("Table created successfully!")

# Insert sample data into the table
with conn:
    conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
    conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
print("Data inserted successfully!")


# Fetch all users from the table
print("Users in the database:")
for row in conn.execute("SELECT * FROM users"):
    print(row)


# Update a user’s age
with conn:
    conn.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
print("Data updated successfully!")

# Verify the update
for row in conn.execute("SELECT * FROM users WHERE name = 'Alice'"):
    print("Updated record:", row)


# Delete a user
with conn:
    conn.execute("DELETE FROM users WHERE name = ?", ("Bob",))
print("Data deleted successfully!")

# Verify the deletion
print("Remaining users:")
for row in conn.execute("SELECT * FROM users"):
    print(row)


conn.close()
print("Connection closed.")


import sqlite3
# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("users.db", isolation_level=None)

"""Creates the users table if it doesn't exist."""
conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    age INTEGER NOT NULL
    )
""")

def create_user(name, age):
    """Create a new user."""
    cursor = conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    return cursor.lastrowid  # Return the ID of the inserted row

def list_users():
    """Return a list of all users in the database."""
    return conn.execute("SELECT * FROM users").fetchall()

def update_user(uid, name, age):
    """Update a user's age."""
    cursor = conn.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, uid))
    return cursor.rowcount > 0  # True if at least one row was updated

def delete_user(uid):
    """Delete a user."""
    cursor = conn.execute("DELETE FROM users WHERE id = ?", (uid,)) # we need to provide a comma if we only have 1 value
    return cursor.rowcount > 0  # True if at least one row was deleted

def main():
    while True:
        print("\nChoose an option:")
        print("1. Create user")
        print("2. List users")
        print("3. Update user")
        print("4. Delete user")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            if create_user(name, age):
                print("User created successfully!")
        elif choice == "2":
            users = list_users()
            print("\nUsers in the database:")
            for user in users:
                print(user)
        elif choice == "3":
            id = int(input("Enter id of user to update: "))
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            if update_user(id, new_name, new_age):
                print("User updated successfully!")
            else:
                print("User not found.")
        elif choice == "4":
            id = int(input("Enter id of user to delete: "))
            if delete_user(id):
                print("User deleted successfully!")
            else:
                print("User not found.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
    
    #conn.close()
    #print("Database connection closed.")

if __name__ == "__main__":
    main()



# Similar to list_users(), but return only users that matches the name provided
def search_user(name):
    """Return users matching the provided name."""
    return conn.execute(
        "SELECT * FROM users WHERE name LIKE ?",
        (f"%{name}%",)
    ).fetchall()


# Main function
def main():
    while True:
        print("\nChoose an option:")
        print("1. Create user")
        print("2. List users")
        print("3. Update user")
        print("4. Delete user")
        print("5. Search user")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            if create_user(name, age):
                print("User created successfully!")

        elif choice == "2":
            users = list_users()
            print("\nUsers in the database:")
            for user in users:
                print(user)

        elif choice == "3":
            id = int(input("Enter id of user to update: "))
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            if update_user(id, new_name, new_age):
                print("User updated successfully!")
            else:
                print("User not found.")

        elif choice == "4":
            id = int(input("Enter id of user to delete: "))
            if delete_user(id):
                print("User deleted successfully!")
            else:
                print("User not found.")

        elif choice == "5":
            name = input("Enter name to search: ")
            users = search_user(name)
            print("\nMatching users:")
            for user in users:
                print(user)
            if not users:
                print("No matching users found.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

    conn.close()
    print("Database connection closed.")


if __name__ == "__main__":
    main()