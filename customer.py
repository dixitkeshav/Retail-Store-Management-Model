from catalog import catalog, update_catalog_stock
from customer_bags import add_to_bag, get_customer_bag, clear_customer_bag

class Customer:
    def __init__(self, customer_id, customer_password):
        self.customer_id = customer_id
        self.customer_password = customer_password
        self.wallet_balance = 0

    def view_catalog(self):
        """
        View the catalog of products.
        """
        print("\n--- Product Catalog ---")
        print(f"{'ID':<10}{'Name':<15}{'Price':<10}{'Stock':<10}")
        for product_id, details in catalog.items():
            print(f"{product_id:<10}{details['name']:<15}{details['price']:<10}{details['stock']:<10}")

    def deposit_amount(self, amount):
        """
        Deposit money into the customer's wallet.
        """
        self.wallet_balance += amount
        print(f"Deposited INR {amount}. Wallet Balance: INR {self.wallet_balance}")

    def add_to_bag(self, product_id, quantity):
        """
        Add a product to the customer's bag.
        """
        if product_id in catalog:
            product = catalog[product_id]
            if product["stock"] >= quantity:
                total_price = product["price"] * quantity

                # Add item to the global customer_bags dictionary
                add_to_bag(self.customer_id, product["name"], quantity, product["price"], total_price)

                # Reduce stock in the catalog
                update_catalog_stock(product_id, quantity)

                print(f"Added {quantity} of {product['name']} to the bag.")
            else:
                print(f"Not enough stock for {product['name']}. Available: {product['stock']}")
        else:
            print("Product not found in catalog.")

    def view_bag(self):
        """
        Display the items in the customer's shopping bag.
        """
        bag = get_customer_bag(self.customer_id)  # Retrieve the bag for this customer
        if not bag:
            print("Your bag is empty.")
            return

        print("\n--- Your Bag ---")
        print(f"{'Item':<15}{'Quantity':<10}{'Price':<10}{'Total':<10}")
        for item in bag:
            print(f"{item['item_name']:<15}{item['quantity']:<10}{item['price']:<10}{item['total']:<10}")

    def logout(self):
        """
        Log the customer out.
        """
        print("Customer logged out.")
def customer_options(customer):
    """
    Provide options for the customer to interact with the system.
    """
    while True:
        print("\nCustomer Options:")
        print("1. View Catalog")
        print("2. Add Item to Bag")
        print("3. View Bag")
        print("4. Deposit Money")
        print("5. Log Out")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer.view_catalog()
        elif choice == "2":
            product_id = input("Enter Product ID to add to bag: ")
            quantity = int(input("Enter quantity: "))
            customer.add_to_bag(product_id, quantity)
        elif choice == "3":
            customer.view_bag()
        elif choice == "4":
            amount = float(input("Enter amount to deposit: "))
            customer.deposit_amount(amount)
        elif choice == "5":
            customer.logout()
            break
        else:
            print("Invalid choice!")
