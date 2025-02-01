# customer_bags.py

# Dictionary to store bags for each customer
customer_bags = {}

def get_customer_bag(customer_id):
    """
    Retrieve the bag for a specific customer.
    """
    return customer_bags.get(customer_id, [])

def clear_customer_bag(customer_id):
    """
    Clear the bag for a specific customer.
    """
    if customer_id in customer_bags:
        customer_bags[customer_id] = []

def add_to_bag(customer_id, item_name, quantity, price, total):
    """
    Add an item to the customer's bag.
    """
    if customer_id not in customer_bags:
        customer_bags[customer_id] = []
    customer_bags[customer_id].append({
        "item_name": item_name,
        "quantity": quantity,
        "price": price,
        "total": total
    })
