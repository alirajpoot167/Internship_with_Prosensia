# Inventory Management System

# Initialize an empty list to store the inventory
inventory = []

def add_product():
    # Get product details from the user
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    # Check if the product is already in the inventory
    for product in inventory:
        if product["name"] == name:
            print("Product already exists in the inventory.")
            return

    # Add the new product to the inventory
    new_product = {"name": name, "price": price, "quantity": quantity}
    inventory.append(new_product)
    print("Product added successfully.")

def update_product():
    # Get the product name from the user
    name = input("Enter product name: ")

    # Check if the product exists in the inventory
    for product in inventory:
        if product["name"] == name:
            # Update the product quantity
            quantity = int(input("Enter new product quantity: "))
            product["quantity"] = quantity
            print("Product quantity updated successfully.")
            return

    print("Product not found in the inventory.")

def display_inventory():
    # Display all products in the inventory
    for product in inventory:
        print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Display Inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()