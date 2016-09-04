class UnitWithItems:
    def __init__(self):
        self.items = set()

    def show_items(self):
        return '\n'.join(str(item) for item in sorted(self.items))

    def add_item(self, item):
        self.items.add(item.item)

    def remove_item(self, item):
        self.items.remove(item.item)
