class Component:
    def __init__(self, comp_id, name):
        self.comp_id = comp_id
        self.name = name

    def __str__(self):
        return '{0} {1}'.format(self.name, self.comp_id)
