from pizzas import Pizza


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory
    
    def prepare(self):
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        cheese = self.ingredient_factory.create_cheese()
        clams = self.ingredient_factory.create_clams()

