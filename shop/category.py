from component import Component
from unit_with_items import UnitWithItems


class Category(UnitWithItems):
    all_categories = set()
    category_id = 1

    def __init__(self, category_name='Category'):
        UnitWithItems.__init__(self)
        self.category = Component(Category.category_id, category_name)
        Category.category_id += 1
        Category.all_categories.add(self.category)

    def add_item(self, item):
        item.change_category(self)

    @staticmethod
    def remove_item_to_category(item, category):
        item.change_category(category)

    @staticmethod
    def get_all_categories():
        return '\nList of categories:\n' + \
               ('\n'.join(str(order) for order in sorted(
                Category.all_categories)))

    def __str__(self):
        return '\n{0} \n{1}'.format(
            self.category, ('includes items:\n' + self.show_items() if
                            self.items else "hasn't got items"))


if __name__ == '__main__':
    category1 = Category()
    category2 = Category()
    print category1
    print category2
    print Category.get_all_categories()
