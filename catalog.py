catalog = {
    "P001": {"name": "Apple", "price": 50, "stock": 50},
    "P002": {"name": "Banana", "price": 25, "stock": 100},
    "P003": {"name": "Orange", "price": 60, "stock": 70},
    "P004": {"name": "Milk", "price": 60, "stock": 100},
    "P005": {"name": "Notebook", "price": 120, "stock": 50},
    "P006": {"name": "Pen", "price": 10, "stock": 30},
    "P007": {"name": "Chips", "price": 20, "stock": 20},
}

def view_catalog():
    print("\nCatalog:")
    print(f"{'ID':<10}{'Name':<15}{'Price':<10}{'Stock':<10}")
    for product_id, details in catalog.items():
        print(f"{product_id:<10}{details['name']:<15}{details['price']:<10}{details['stock']:<10}")

def update_catalog_stock(product_id, quantity):
    if product_id in catalog:
        catalog[product_id]["stock"] -= quantity
