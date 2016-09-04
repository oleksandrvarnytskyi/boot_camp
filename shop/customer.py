from component import Component
from order import Order
from unit_with_orders import UnitWithOrders


class Customer(UnitWithOrders):
    all_customers = set()
    customer_id = 1

    def __init__(self, customer_name='Customer'):
        UnitWithOrders.__init__(self)
        self.customer = Component(Customer.customer_id, customer_name)
        Customer.customer_id += 1
        Customer.all_customers.add(self.customer)

    def new_order(self, first_item):
        new_order = Order(self, first_item)
        self.add_order(new_order)
        first_item.add_order(new_order)

    @staticmethod
    def get_all_customers():
        return '\nList of all customers:\n' + \
               ('\n'.join(str(customer) for customer in sorted(
                   Customer.all_customers)))

    def __str__(self):
        return '\n{0}\n{1}\n'.format(self.customer, ('has made orders:\n' +
                                                     self.show_orders() if
                                                     self.orders else "hasn't "
                                                     "got orders"))
