from component import Component
from unit_with_items import UnitWithItems


class CustomerIsNotDefine(Exception):
    pass


class FirstItemIsNotDefine(Exception):
    pass


class Order(UnitWithItems):
    all_orders = set()
    order_id = 1

    def __init__(self, customer=None, first_item=None, order_name='order'):
        UnitWithItems.__init__(self)
        self.order = Component(Order.order_id, order_name)
        Order.order_id += 1

        if not customer:
            raise CustomerIsNotDefine()
        else:
            self.customer = customer
            self.customer.orders.add(self.order)

        if not first_item:
            raise FirstItemIsNotDefine()
        else:
            self.first_item = first_item
            self.add_item(self.first_item)
            self.first_item.add_order(self)
            Order.all_orders.add(self.order)

    def add_item(self, new_item):
        UnitWithItems.add_item(self, new_item)
        new_item.orders.add(self.order)

    def remove_item(self, removing_item):
        UnitWithItems.remove_item(self, removing_item)
        if not self.items:
            raise FirstItemIsNotDefine()
        removing_item.remove_order(self)

    @staticmethod
    def get_all_orders():
        return '\nList of all orders:\n' + ('\n'.join(str(order) for order
                                                      in sorted(
                                                      Order.all_orders)))

    def __str__(self):
        return '\n{0}\nowner: {1}\nordered items:\n{2}'.format(
            self.order, self.customer.customer, self.show_items())
