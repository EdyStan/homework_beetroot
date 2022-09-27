class Product:
    def __init__(self, type='vegetable', name='cucumber', price_for_one=1.):
        self.type = type
        self.name = name
        self.price_for_one = price_for_one
        self.discount = 30
        self.amount = 0
        self.sold_amount = 0


class ProductStore:
    def __init__(self):
        self.dict_of_products = {}

    def add(self, product, amount):
        product.amount = amount
        self.dict_of_products[product] = amount

# there, I tried to get the method name with something like key.exec(identifier_type)
# How can I implement that directly? Or is it a viable method, without filling the code with if statements?
    def set_discount(self, identifier, percent, identifier_type='name'):
        for key in self.dict_of_products:
            if identifier_type == 'name':
                if identifier == key.name:
                    key.discount = percent
            elif identifier_type == 'type':
                if identifier == key.type:
                    key.discount = percent

    def sell_product(self, product_name, amount):
        for key in self.dict_of_products:
            if product_name == key.name:
                key.amount -= amount
                key.sold_amount = amount

    def get_income(self):
        total_income = 0
        for key in self.dict_of_products:
            total_income += key.sold_amount * key.price_for_one * (100 - key.discount)/100
        print("{:.2f}".format(total_income) + '$')

    def get_all_products(self):
        for key in self.dict_of_products:
            print(f"Name: {key.name}\n"
                  f"Type: {key.type}")
            if key.type == 'vegetable' or key.type == 'fruit':
                print(f"Price for one kilogram: {key.price_for_one}$\n"
                      f"Amount for sell: {key.amount} kilograms")
            else:
                print(f"Price for one piece: {key.price_for_one}$\n"
                      f"Amount for sell: {key.amount} pieces")
            print(f"Discount: {key.discount}%\n")

    def get_product_info(self, product_name):
        for key in self.dict_of_products:
            if product_name == key.name:
                return key.name, key.amount


x = Product()
y = Product('fruit', 'Apple', 1.5)
z = Product('electronic', 'blender', 99.99)
store = ProductStore()

store.add(x, 100)
store.add(y, 605)
store.add(z, 4)

store.set_discount('cucumber', 40)
print(x.discount)

store.set_discount('blender', 15)

print(x.amount)
store.sell_product('cucumber', 50)
print(x.amount)

store.sell_product('blender', 2)

store.get_income()
store.get_all_products()

print(store.get_product_info('cucumber'))
