from component import Component
from order import Order


class Customer(Component):
    all_customers = set()
    customer_id = 1

    def __init__(self, customer_name='Customer'):
        Component.__init__(self, Customer.customer_id, customer_name)
        Customer.customer_id += 1
        self.customer_name = customer_name
        self.orders_of_customer = set()
        Customer.all_customers.add(Component.__str__(self))

    def add_order(self, first_item):
        new_order = Order(self, first_item)
        self.orders_of_customer.add(Component.__str__(new_order))

    @staticmethod
    def get_all_customers():
        return '\nList of all customers:\n' + Component.show_items(
            Customer.all_customers)

    def __str__(self):
        return '\n{0}\n{1}\n'.format(Component.__str__(self),
                                     ('has made orders:\n' +
                                     Component.show_items(
                                        self.orders_of_customer) if
                                     self.orders_of_customer else
                                     "hasn't got orders"))
