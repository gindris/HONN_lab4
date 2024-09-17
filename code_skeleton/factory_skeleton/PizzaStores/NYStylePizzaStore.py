from PizzaStores.PizzaStore import PizzaStore
from pizzas.Pizza import Pizza
from pizzas.CheesePizza import CheesePizza
from pizzas.ClamPizza import ClamPizza
from pizzas.PepperoniPizza import PepperoniPizza
from pizzas.VeggiePizza import VeggiePizza
from pizzas.PizzaType import PizzaType
from ingredient_factories.NYPizzaIngredientFactory import NYPizzaIngredientFactory

class NYStylePizzaStore(PizzaStore):
    
    def create_pizza(self, pizza_type) -> Pizza: 
        if pizza_type == PizzaType.CHEESE:
            pizza = CheesePizza(NYPizzaIngredientFactory())
            pizza.set_name('New York Style Cheese Pizza')
            return pizza
        elif pizza_type == PizzaType.CLAM:
            pizza = ClamPizza(NYPizzaIngredientFactory())
            pizza.set_name('New York Style Clam Pizza')
            return pizza
        elif pizza_type == PizzaType.PEPPERONI:
            pizza = PepperoniPizza(NYPizzaIngredientFactory())
            pizza.set_name('New York Style Pepperoni Pizza')
            return pizza
        else: #default to veggie
            pizza = VeggiePizza(NYPizzaIngredientFactory())
            pizza.set_name('New York Style Veggie Pizza')
            return pizza


