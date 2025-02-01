from catalog import catalog  # Importing catalog from catalog.py

class Admin:
    def __init__(self, admin_id, admin_password):
        self.admin_id = admin_id
        self.admin_password = admin_password

    def add_item(self, product_id, name, price, stock):
        """
        Add a new product to the catalog or update existing product stock.
        """
        if product_id in catalog:
            catalog[product_id]["stock"] += stock  # Update stock quantity
            catalog[product_id]["price"] = price  # Update price
            print(f"Updated stock for {name} (ID: {product_id}). New stock: {catalog[product_id]['stock']}, New price: {catalog[product_id]['price']}")
        else:
            catalog[product_id] = {"name": name, "price": price, "stock": stock}
            print(f"Added product {name} with ID {product_id} to the catalog.")

    def remove_item(self, product_id):
        """
        Remove a product from the catalog.
        """
        if product_id in catalog:
            del catalog[product_id]
            print(f"Removed product with ID {product_id} from the catalog.")
        else:
            print(f"Product with ID {product_id} not found.")

    def update_product(self, product_id, name=None, price=None, stock=None):
        """
        Update product details in the catalog.
        """
        if product_id in catalog:
            if name:
                catalog[product_id]["name"] = name
            if price:
                catalog[product_id]["price"] = price
            if stock:
                catalog[product_id]["stock"] = stock
            print(f"Updated product {product_id} with new details: Name: {catalog[product_id]['name']}, Price: {catalog[product_id]['price']}, Stock: {catalog[product_id]['stock']}")
        else:
            print(f"Product with ID {product_id} not found.")

    def view_catalog(self):
        """
        Display the product catalog.
        """
        print("\n--- Product Catalog ---")
        for product_id, details in catalog.items():
            print(f"ID: {product_id}, Name: {details['name']}, Price: INR {details['price']}, Stock: {details['stock']}")

    def logout(self):
        """
        Log the admin out.
        """
        print("Admin logged out.")

def update_product(self, product_id, name=None, price=None, stock=None):
    """
    Update product details in the catalog.
    """
    for product in catalog:
        if product["id"] == product_id:
            if name:
                product["name"] = name
            if price:
                product["price"] = price
            if stock:
                product["stock"] = stock
            print(f"Updated product {product_id} with new details.")
            return
    print(f"Product with ID {product_id} not found.")        

def update_catalog():
    while True:
        print("\nAdmin Catalog Options:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Catalog")
        print("4. Log Out")
        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = input("Enter Product ID: ")
            product_name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock: "))
            
            # Check if the product already exists
            for product in catalog:
                if product["id"] == product_id:
                    product["stock"] += stock  # Update stock quantity
                    product["price"] = price
                    print(f"Updated stock for {product_name} (ID: {product_id}). New stock: {product['stock']} . New price: {product['price']}")
                    break
            else:
                # If product doesn't exist, add a new entry
                catalog.append({"id": product_id, "name": product_name, "price": price, "stock": stock})
                print("Product added successfully!")

        elif choice == "2":
            product_id = input("Enter Product ID to remove: ")
            for product in catalog:
                if product["id"] == product_id:
                    catalog.remove(product)
                    print("Product removed successfully!")
                    break
            else:
                print("Product not found!")
                
        elif choice == "3":
            print("\nCatalog:")
            for product in catalog:
                print(f"ID: {product['id']}, Name: {product['name']}, Price: INR {product['price']}, Stock: {product['stock']}")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice!")
