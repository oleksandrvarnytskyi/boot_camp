class UnitWithOrders:
    def __init__(self):
        self.orders = set()

    def show_orders(self):
        return '\n'.join(str(order) for order in sorted(self.orders))

    def add_order(self, order):
        self.orders.add(order.order)

    def remove_order(self, order):
        self.orders.remove(order.order)
