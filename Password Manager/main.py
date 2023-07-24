import os
import sqlite3
from getpass import getpass
import hashlib
import time
from cryptography.fernet import Fernet

# Generate a key and initialize a cipher suite
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def connect_db(db_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Get the directory of the current script
    db_path = os.path.join(script_dir, db_name)  # Combine the directory with the db_name
    conn = sqlite3.connect(db_path)
    return conn

def create_table(conn):
    conn.execute('CREATE TABLE IF NOT EXISTS Manager (Website TEXT, Username TEXT, Password TEXT)')
    print("Table created successfully")


def insert_password(conn, website, username, password):
    if not website or not username or not password:
        print('\nInput values cannot be empty!\n')
        return
    encrypted_password = cipher_suite.encrypt(password.encode())  # Encrypt the password
    conn.execute(f"INSERT INTO Manager (Website, Username, Password) VALUES (?, ?, ?)", (website, username, encrypted_password))
    conn.commit()
    
def view_passwords(conn):
    cursor = conn.execute("SELECT Website, Username, Password FROM Manager")
    for row in cursor:
        decrypted_password = cipher_suite.decrypt(row[2]).decode()  # Decrypt the password
        print(f"Website: {row[0]}, Username: {row[1]}, Password: {decrypted_password}")

    
def delete_password(conn, website):
    cursor = conn.execute(f"SELECT * FROM Manager WHERE Website = ?", (website,))
    data = cursor.fetchone()
    if data is None:
        print('\nNo such information found!\n')
        return
    else:
        print('Information deleted successfully.\n')
    conn.execute(f"DELETE FROM Manager WHERE Website = ?", (website,))
    conn.commit()

def main():
    conn = connect_db('PasswordManager.db')
    create_table(conn)
    while True:
        print("\n1. Store new password")
        print("2. View stored passwords")
        print("3. Delete password")
        print("4. Quit\n")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            insert_password(conn, website, username, password)
            print('\nInformation stored successfully.\n')
            time.sleep(2)
            
        elif choice == 2:
            print('Your informations.')
            view_passwords(conn)
            time.sleep(2)
            
        elif choice == 3:
            website = input("\nEnter the website for which you want to delete the password: \n")
            delete_password(conn, website)
            time.sleep(2)
            
        elif choice == 4:
            break

if __name__ == "__main__":
    main()
