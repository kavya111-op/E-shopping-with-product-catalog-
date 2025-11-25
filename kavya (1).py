# -------------------------------
# -------------------------------
#   Simple E-Shopping Program
# -------------------------------

# Product Catalog (ID : {name, price})
catalog = {
    1: {"name": "Laptop", "price": 55000},
    2: {"name": "Smartphone", "price": 20000},
    3: {"name": "Headphones", "price": 1500},
    4: {"name": "Keyboard", "price": 800},
    5: {"name": "Smart Watch", "price": 4500}
}

cart = {}

def show_catalog():
    print("\n===== PRODUCT CATALOG =====")
    print("ID   Name                Price")
    print("-------------------------------")
    for pid, item in catalog.items():
        print(f"{pid:<4} {item['name']:<18} ₹{item['price']}")
    print("-------------------------------")

def add_to_cart():
    show_catalog()
    try:
        pid = int(input("Enter product ID to add: "))
        if pid not in catalog:
            print("❌ Invalid product ID!")
            return
        

        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print("❌ Invalid quantity!")
            return

        if pid in cart:
            cart[pid] += qty
        else:
            cart[pid] = qty

        print("✔ Item added to cart!")
    except ValueError:
        print("❌ Please enter numeric values!")

def generate_bill():
    print("\n=========== INVOICE ===========")
    print("Name                 Qty   Price     Total")
    print("-------------------------------------------")

    subtotal = 0
    for pid, qty in cart.items():
        name = catalog[pid]["name"]
        price = catalog[pid]["price"]
        total = qty * price
        subtotal += total
        print(f"{name:<20} {qty:<5} ₹{price:<8} ₹{total}")

    tax = subtotal * 0.18  # 18% GST
    grand_total = subtotal + tax

    print("-------------------------------------------")
    print(f"Subtotal:                 ₹{subtotal}")
    print(f"GST (18%):                ₹{tax:.2f}")
    print(f"Grand Total:              ₹{grand_total:.2f}")
    print("===========================================\n")
    print("Thank you for shopping!")

# Main Menu
while True:
    print("\n===== E-SHOPPING MENU =====")
    print("1. Show Catalog")
    print("2. Add to Cart")
    print("3. Generate Bill")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_catalog()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        if cart:
            generate_bill()
            break
        else:
            print("❌ Your cart is empty!")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("❌ Invalid choice! Try again.")