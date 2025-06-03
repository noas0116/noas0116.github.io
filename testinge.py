from nicegui import ui

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_receipt(self):
        total = 0
        text = ""
        for p in self.products:
            text += f"{p.name}: {p.price:.2f} kr\n"
            total += p.price
        text += f"\nTotalt: {total:.2f} kr"
        return text

cart = ShoppingCart()

products = [
    Product("Äpple", 5.0),
    Product("Bröd", 20.0),
    Product("Mjölk", 15.0),
]

dropdown = ui.select([p.name for p in products], label='Välj en produkt')

receipt = ui.textarea(label="Kvitto")
receipt.disabled = True  # gör rutan skrivskyddad

def add_to_cart():
    name = dropdown.value
    for p in products:
        if p.name == name:
            cart.add_product(p)
            break
    receipt.value = cart.get_receipt()

ui.button("Lägg till i kundvagnen", on_click=add_to_cart)

ui.run(native=True)
