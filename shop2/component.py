class Component:
    def __init__(self, comp_id, name):
        self.id = comp_id
        self.name = name

    @staticmethod
    def show_items(set_of_items):
        return '\n'.join(str(item) for item in sorted(set_of_items))

    def __str__(self):
        return '{0} {1}'.format(self.name, self.id)
