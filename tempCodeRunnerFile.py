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
