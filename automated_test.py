from admin import Admin
from customer import Customer
from salesman import Salesman
from customer_bags import get_customer_bag, clear_customer_bag

def automated_test():
    # Step 1: Admin Actions
    print("\n--- Admin Login ---")
    admin_id = "admin1"
    admin_password = "adminpass"
    admin = Admin(admin_id, admin_password)

    print("\n[Admin] Adding Multiple Items to Catalog")
    admin.add_item("P001", "Apple", 70, 50)
    admin.add_item("P002", "Banana", 40, 100)
    admin.add_item("P003", "Orange", 100, 70)

    print("\n[Admin] Updating Product Details")
    admin.update_product("P001", stock=100, price=70
                         )  # Update stock and price for Apple

    print("\n[Admin] Viewing Updated Catalog")
    admin.view_catalog()

    print("\n[Admin] Removing an Item from Catalog")
    admin.remove_item("P003")  # Remove Orange from catalog

    print("\n[Admin] Logging Out")
    admin.logout()

    # Step 2: Customer Actions
    print("\n--- Customer Login ---")
    customer_id = "cust1"
    customer_password = "custpass"
    customer = Customer(customer_id, customer_password)

    print("\n[Customer] Viewing Catalog")
    customer.view_catalog()

    print("\n[Customer] Depositing Money to Wallet")
    customer.deposit_amount(500)  # Low balance scenario

    print("\n[Customer] Adding Items to Bag")
    customer.add_to_bag("P001", 2)  # Add 2 Apples
    customer.add_to_bag("P002", 5)  # Add 5 Bananas

    print("\n[Customer] Viewing Bag")
    customer.view_bag()

    print("\n[Customer] Attempting Checkout with Insufficient Funds")
    # Ensure the customer can only check out items within their wallet balance
    try:
        customer.checkout()  # Add this method to validate wallet balance
    except Exception as e:
        print(f"Checkout failed: {e}")

    print("\n[Customer] Logging Out")
    customer.logout()

    # Step 3: Salesman Actions
    print("\n--- Salesman Login ---")
    salesman_id = "sales1"
    salesman_password = "salespass"
    salesman = Salesman(salesman_id, salesman_password)

    print("\n[Salesman] Processing Customer Bag")
    customer_bag = get_customer_bag(customer_id)
    if customer_bag:
        salesman.process_customer_bag(customer_id)  # Process the customer's cart
    else:
        print(f"Customer {customer_id} has no items in their bag.")

    print("\n[Salesman] Logging Out")
    salesman.logout()

    print("\n--- Test Case Execution Completed ---")


# Run the automated test case
if __name__ == "__main__":
    automated_test()
