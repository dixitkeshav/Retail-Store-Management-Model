from credentials import credentials
from admin import Admin
from customer import Customer
from salesman import Salesman
from admin import update_catalog
from customer import customer_options
from salesman import salesman_options
def login(role):
    print(f"\nLogin as {role.capitalize()}")
    user_id = input("Enter ID: ")
    password = input("Enter Password: ")
    if credentials.get(role) and credentials[role].get(user_id) == password:
        print(f"Welcome, {user_id}!")
        return True
    else:
        print("Invalid ID or Password!")
        return False
def main():
    while True:
        print("\nSelect Role:")
        print("1. Admin")
        print("2. Customer")
        print("3. Salesman")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1" and login("admin"):
            update_catalog()
        elif choice == "2" and login("customer"):
            customer_name = input("Enter your name: ")
            customer_options(customer_name)
        elif choice == "3" and login("salesman"):
            salesman_options()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice or failed login!")
if __name__ == "__main__":
    main()
