from component import Component


class CategoryIsNotDefine(Exception):
    pass


class Item(Component):
    all_items = set()
    item_id = 1

    def __init__(self, category, item_name='item'):
        Component.__init__(self, Item.item_id, item_name)
        Item.item_id += 1
        self.item_name = item_name
        self.category = category
        self.orders_of_item = set()

        if not self.category:
            raise CategoryIsNotDefine()
        else:
            self.category.items_of_category.add(Component.__str__(self))
            Item.all_items.add(Component.__str__(self))

    def change_category(self, new_category):
        new_category.items_of_category.add(Component.__str__(self))
        self.category.items_of_category.remove(Component.__str__(self))
        self.category = new_category

    @staticmethod
    def get_all_items():
        return '\nList of all items:\n' + Component.show_items(Item.all_items)

    def __str__(self):
        return '\n{0} \n{1}\n'.format(Component.__str__(self),
                                      ('is included in orders:\n' +
                                       Component.show_items(
                                           self.orders_of_item) if
                                       self.orders_of_item else
                                       "hasn't been included in any orders"))


if __name__ == '__main__':
    from category import Category

    try:
        goods = Category()
        item1 = Item(goods)
        item2 = Item(goods)
        item3 = Item(goods)
        print item1
        print item2
    except CategoryIsNotDefine:
        print 'CategoryIsNotDefine was caught'
    print Item.get_all_items()
