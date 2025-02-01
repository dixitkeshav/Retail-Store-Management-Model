import customer_bags
from customer_bags import get_customer_bag , add_to_bag , clear_customer_bag

class Salesman:
    def __init__(self, salesman_id, salesman_password):
        self.salesman_id = salesman_id
        self.salesman_password = salesman_password

    def process_customer_bag(self, customer_id):
        """
        Process a customer's bag by calculating the total and clearing the bag.
        """
        bag = get_customer_bag(customer_id)  # Use the function to get the bag
        if not bag:
            print(f"No items in the customer's bag (Customer ID: {customer_id}).")
            return

        print(f"\n--- Processing Bag for Customer ID: {customer_id} ---")
        print(f"{'Item':<20}{'Quantity':<10}{'Price':<10}{'Total'}")
        total_bill = 0
        for item in bag:
            print(f"{item['item_name']:<20}{item['quantity']:<10}{item['price']:<10}{item['total']}")
            total_bill += item["total"]

        print(f"\nTotal Bill: INR {total_bill}")
        clear_customer_bag(customer_id)  # Clear the bag
        print("Customer's bag processed and cleared successfully!")

    def logout(self):
        """
        Log the salesman out.
        """
        print("Salesman logged out.")

def salesman_options(salesman):
    """
    Provide options for the salesman to interact with the system.
    :param salesman: An instance of the Salesman class
    """
    while True:
        print("\n--- Salesman Options ---")
        print("1. Process Customer Bag")
        print("2. Log Out")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_id = input("Enter Customer ID to process: ")
            salesman.process_customer_bag(customer_id)
        elif choice == "2":
            salesman.logout()
            break
        else:
            print("Invalid choice!")
