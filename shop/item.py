from component import Component
from unit_with_orders import UnitWithOrders


class CategoryIsNotDefine(Exception):
    pass


class Item(UnitWithOrders):
    all_items = set()
    item_id = 1

    def __init__(self, category=None, item_name='item'):
        UnitWithOrders.__init__(self)
        self.item = Component(Item.item_id, item_name)
        Item.item_id += 1
        self.category = category

        if not self.category:
            raise CategoryIsNotDefine()
        else:
            self.category.items.add(self.item)
            Item.all_items.add(self.item)

    def change_category(self, new_category):
        new_category.items.add(self.item)
        self.category.items.remove(self.item)
        self.category = new_category

    @staticmethod
    def get_all_items():
        return '\nList of all items:\n' + \
               ('\n'.join(str(item) for item in sorted(Item.all_items)))

    def __str__(self):
        return '\n{0} \n{1}\n'.format(self.item,
                                      ('is included in orders:\n' +
                                       self.show_orders() if self.orders else
                                       "hasn't been included in any orders"))


if __name__ == '__main__':
    from category import Category
    from order import Order
    from customer import Customer

    try:
        customer1 = Customer()
        goods = Category()
        item1 = Item(goods)
        item2 = Item(goods)
        item3 = Item(goods)
        order1 = Order(customer1, item1)
        print item1
        print item2
    except CategoryIsNotDefine:
        print 'CategoryIsNotDefine was caught'
    print Item.get_all_items()
