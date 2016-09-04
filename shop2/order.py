from component import Component


class CustomerIsNotDefine(Exception):
    pass


class FirstItemIsNotDefine(Exception):
    pass


class Order(Component):
    all_orders = set()
    order_id = 1

    def __init__(self, customer=None, first_item=None, order_name='order'):
        Component.__init__(self, Order.order_id, order_name)
        Order.order_id += 1
        self.order_name = order_name
        self.items_of_order = set()

        if not customer:
            raise CustomerIsNotDefine()
        else:
            self.customer = customer
            self.customer.orders_of_customer.add(Component.__str__(self))

        if not first_item:
            raise FirstItemIsNotDefine()
        else:
            self.first_item = first_item
            self.items_of_order.add(Component.__str__(self.first_item))
            self.first_item.orders_of_item.add(Component.__str__(self))
            Order.all_orders.add(Component.__str__(self))

    def add_item(self, new_item):
        self.items_of_order.add(Component.__str__(new_item))
        new_item.orders_of_item.add(Component.__str__(self))

    def remove_item(self, removing_item):
        self.items_of_order.remove(Component.__str__(removing_item))
        if not self.items_of_order:
            raise FirstItemIsNotDefine()
        removing_item.orders_of_item.remove(Component.__str__(self))

    @staticmethod
    def get_all_orders():
        return '\nList of all orders:\n' + Component.show_items(
            Order.all_orders)

    def __str__(self):
        return '\n{0}\nowner: {1}\nordered items:\n{2}'.format(
            Component.__str__(self), Component.__str__(self.customer),
            Component.show_items(self.items_of_order))
