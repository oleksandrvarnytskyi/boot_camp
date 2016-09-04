from category import Category
from item import Item
from customer import Customer
from order import Order

cust1 = Customer()
cust2 = Customer()

categ1 = Category()
categ2 = Category()
categ3 = Category()

item1 = Item(categ1)
item2 = Item(categ1)
item3 = Item(categ2)
item4 = Item(categ1)
item5 = Item(categ2)
item6 = Item(categ3)

order1 = Order(cust1, item1)
order2 = Order(cust1, item2)
order3 = Order(cust2, item4)

print cust1
print cust2

order2.add_item(item5)
order3.add_item(item2)
order3.add_item(item3)

print order3
order3.remove_item(item3)
print order3

print Category.get_all_categories()
print Item.get_all_items()
print categ1
print categ2
item3.change_category(categ1)
print categ1
print categ2
print categ3
categ3.remove(item6)
print categ3
cust2.add_order(item1)
print cust2
print item1
print Order.get_all_orders()
