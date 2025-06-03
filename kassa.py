from nicegui import ui

class Product:
    def __init__(self, name : str, price : int):
        self.name = name
        self.price = price 

class Shopping_cart:
    def __init__(self, products : dict[Product, int]):
        self.products = products  

    def add_product(self, product : Product):
        #Om produkten redan finns
        for product_cart in self.products:
            if product_cart.name == product.name:
                self.products[product_cart] += 1
                return
        
        #Om produkten inte finns
        self.products[product] = 1

    def get_receipt(self):
        for product in self.products:
            ui.label(f"{product.name} {self.products[product] * product.price}")
            if self.products[product] > 1:
                ui.label(f"    {self.products[product]}st x {product.price}")

cart = Shopping_cart(
    {Product("Bröd", 32) : 1,
    Product("Glass", 20) : 1,
    Product("Mjölk", 16) : 1,
    })

cart.add_product(Product("Glass", 20))
cart.get_receipt()

with ui.column():
    ui.button("Mjölk", on_click= lambda: cart.add_product(Product("Mjölk", 16)))
    ui.button("Glass", on_click= lambda: cart.add_product(Product("Glass", 20)))
    ui.button("Bröd", on_click= lambda: cart.add_product(Product("Bröd", 32)))

ui.button("Visa Kvitto", on_click= lambda: cart.get_receipt())

receipt = ui.textarea(label="Kvitto")

ui.run(native=True)