from abc import ABC, abstractmethod

# Product Class
class Product:
    def __init__(self, name, price, sku):
        self.name = name
        self.price = price
        self.sku = sku

    def __str__(self):
        return f"{self.name} (SKU: {self.sku}) - ${self.price:.2f}"


# Cart Class
class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added {product.name} to the cart.")

    def remove_product(self, sku):
        for product in self.products:
            if product.sku == sku:
                self.products.remove(product)
                print(f"Removed {product.name} from the cart.")
                return
        print("Product not found in the cart.")

    def calculate_total(self):
        return sum(product.price for product in self.products)

    def show_cart(self):
        if not self.products:
            print("Your cart is empty.")
        else:
            print("Cart contents:")
            for product in self.products:
                print(f" - {product}")
            print(f"Total: ${self.calculate_total():.2f}")


# Order Class
class Order:
    def __init__(self, cart, customer_name, customer_email):
        self.cart = cart
        self.customer_name = customer_name
        self.customer_email = customer_email

    def __str__(self):
        return f"Order for {self.customer_name} ({self.customer_email}) - Total: ${self.cart.calculate_total():.2f}"


# Abstract PaymentProcessor Class
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Concrete PaymentProcessor Implementations
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount:.2f}...")


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f}...")


# CLI Interface
def main():
    cart = Cart()

    while True:
        print("\nE-Commerce System")
        print("1. Add Product to Cart")
        print("2. Remove Product from Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            sku = input("Enter product SKU: ")
            product = Product(name, price, sku)
            cart.add_product(product)

        elif choice == "2":
            sku = input("Enter product SKU to remove: ")
            cart.remove_product(sku)

        elif choice == "3":
            cart.show_cart()

        elif choice == "4":
            if not cart.products:
                print("Your cart is empty. Add products before checking out.")
                continue

            customer_name = input("Enter your name: ")
            customer_email = input("Enter your email: ")
            order = Order(cart, customer_name, customer_email)
            print(order)

            print("Select Payment Method:")
            print("1. Credit Card")
            print("2. PayPal")
            payment_choice = input("Enter your choice: ")

            if payment_choice == "1":
                processor = CreditCardProcessor()
            elif payment_choice == "2":
                processor = PayPalProcessor()
            else:
                print("Invalid payment method.")
                continue

            processor.process_payment(cart.calculate_total())
            print("Order placed successfully!")
            break

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()