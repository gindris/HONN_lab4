from factory_skeleton.PizzaStores.PizzaStore import PizzaStore
from factory_skeleton.pizzas import Pizza, CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza, PizzaType
from factory_skeleton.ingredient_factories.NYPizzaIngredientFactory import NYPizzaIngredientFactory

class NYStylePizzaStore(PizzaStore):
    
    def create_pizza(self, pizza_type) -> Pizza: 
        print('pizza type: ', pizza_type)
        if pizza_type == PizzaType.CHEESE:
            return CheesePizza(NYPizzaIngredientFactory())
        elif pizza_type == PizzaType.CLAM:
            return ClamPizza(NYPizzaIngredientFactory())
        elif pizza_type == PizzaType.PEPPERONI:
            return PepperoniPizza(NYPizzaIngredientFactory())
        elif pizza_type == PizzaType.VEGGIE:
            return VeggiePizza(NYPizzaIngredientFactory())
        else:
            return CheesePizza(NYPizzaIngredientFactory()) # default to cheese pizza


