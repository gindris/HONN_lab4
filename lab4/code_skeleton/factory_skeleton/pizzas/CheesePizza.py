from pizzas.Pizza import Pizza

class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory
    
    def prepare(self):
        print(f'Preparing {self._name}')
        self._dough = self.ingredient_factory.create_dough()
        self._sauce = self.ingredient_factory.create_sauce()
        self._cheese = self.ingredient_factory.create_cheese()

