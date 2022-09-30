import task_3_classes as t3

x = t3.Product()
y = t3.Product('fruit', 'Apple', 1.5)
z = t3.Product('electronic', 'blender', 99.99)
store = t3.ProductStore()

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