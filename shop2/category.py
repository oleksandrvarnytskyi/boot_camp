from component import Component


class Category(Component):
    all_categories = set()
    category_id = 1

    def __init__(self, category_name='Category'):
        Component.__init__(self, Category.category_id, category_name)
        Category.category_id += 1
        self.category_name = category_name
        self.items_of_category = set()
        Category.all_categories.add(Component.__str__(self))

    def add_item(self, item):
        self.items_of_category.add(Component.__str__(item))

    def remove(self, item):
        self.items_of_category.remove(Component.__str__(item))

    @staticmethod
    def get_all_categories():
        return '\nList of categories:\n' + Component.show_items(
            Category.all_categories)

    def __str__(self):
        return '\n{0} \n{1}'.format(Component.__str__(self),
                                    ('includes items:\n' +
                                     Component.show_items(
                                         self.items_of_category)) if
                                    self.items_of_category else
                                    "hasn't got items")


if __name__ == '__main__':
    category1 = Category()
    category2 = Category()
    print category1
    print category2
    print Category.get_all_categories()
