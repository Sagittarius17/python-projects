import sqlite3
import hashlib

# Connect to the database
conn = sqlite3.connect('passwords.db')

# Create a table to store the passwords
conn.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  website TEXT NOT NULL,
                  username TEXT NOT NULL,
                  password_hash TEXT NOT NULL);''')

# Function to hash the password using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Function to add a new password to the database
def add_password(website, username, password):
    password_hash = hash_password(password)
    conn.execute('INSERT INTO passwords (website, username, password_hash) VALUES (?, ?, ?)',
                 (website, username, password_hash))
    conn.commit()
    print('Password saved successfully!')

# Function to retrieve a password from the database
def get_password(website, username):
    cursor = conn.execute('SELECT password_hash FROM passwords WHERE website = ? AND username = ?',
                          (website, username))
    result = cursor.fetchone()
    if result is not None:
        password_hash = result[0]
        return password_hash
    else:
        return None

# Close the database connection
conn.close()
