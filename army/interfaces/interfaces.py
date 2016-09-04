class Observer:
    def __init__(self):
        self.observables = set()

    def add_observable(self, observable):
        self.observables.add(observable)
        observable.observers.add(self)

    def send_notification(self):
        pass

    def get_observables(self):
        return '\n'.join(str(observable.current_state.name) for observable in
                         self.observables)


class Observable:
    def __init__(self):
        self.observers = set()

    def inform(self):
        pass

    def get_observers(self):
        return '\n'.join(str(observer.current_state.name) for observer in
                         self.observers)
