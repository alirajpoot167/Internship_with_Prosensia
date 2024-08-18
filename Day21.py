# Initialize the inventory data structure
inventory = []

def add_product():
    """Add a new product to the inventory"""
    product_name = input("Enter product name: ")
    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    product = {"name": product_name, "id": product_id, "quantity": quantity, "price": price}
    inventory.append(product)
    print(f"Product '{product_name}' added to inventory!")

def view_inventory():
    """Display the current inventory"""
    if not inventory:
        print("No products in inventory.")
    else:
        print("Current Inventory:")
        for product in inventory:
            print(f"  {product['name']} (ID: {product['id']}, Quantity: {product['quantity']}, Price: ${product['price']:.2f})")

def update_product_quantity():
    """Update the quantity of an existing product"""
    product_id = input("Enter product ID: ")
    new_quantity = int(input("Enter new quantity: "))

    for product in inventory:
        if product["id"] == product_id:
            product["quantity"] = new_quantity
            print(f"Quantity of product '{product['name']}' updated to {new_quantity}.")
            return
    print(f"Product with ID '{product_id}' not found.")

def remove_product():
    """Remove a product from the inventory"""
    product_id = input("Enter product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            inventory.remove(product)
            print(f"Product '{product['name']}' removed from inventory.")
            return
    print(f"Product with ID '{product_id}' not found.")

def main():
    """Main function to drive the program"""
    while True:
        print("\nSimple Inventory Management System")
        print("1. Add a new product")
        print("2. View inventory")
        print("3. Update product quantity")
        print("4. Remove a product")
        print("5. Exit program")

        choice = input("Choose an option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_product_quantity()
        elif choice == "4":
            remove_product()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()