from PizzaStores.PizzaStore import PizzaStore
from pizzas import Pizza, CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza
from ingredient_factories.NYPizzaIngredientFactory import NYPizzaIngredientFactory

#erfir Pizzastore, fær að implementa create_pizza sjálfur
class NYStylePizzaStore(PizzaStore):
    
    def create_pizza(self, pizza_type) -> Pizza: #TODO: add pizza_type parameter
        if pizza_type == 'CHEESE':
            return CheesePizza(NYPizzaIngredientFactory())
        elif pizza_type == 'CLAM':
            return ClamPizza(NYPizzaIngredientFactory())
        elif pizza_type == 'PEPPERONI':
            return PepperoniPizza(NYPizzaIngredientFactory())
        elif pizza_type == 'VEGGIE':
            return VeggiePizza(NYPizzaIngredientFactory())


