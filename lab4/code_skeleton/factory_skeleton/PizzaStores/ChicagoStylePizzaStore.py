from PizzaStores.PizzaStore import PizzaStore
from pizzas.Pizza import Pizza
from pizzas.CheesePizza import CheesePizza
from pizzas.ClamPizza import ClamPizza
from pizzas.PepperoniPizza import PepperoniPizza
from pizzas.VeggiePizza import VeggiePizza
from pizzas.PizzaType import PizzaType
from ingredient_factories.ChicagoPizzaIngredientFactory import ChicagoPizzaIngredientFactory

class ChicagoStylePizzaStore(PizzaStore):
    
    def create_pizza(self, pizza_type) -> Pizza: 
        if pizza_type == PizzaType.CHEESE:
            pizza = CheesePizza(ChicagoPizzaIngredientFactory())
            pizza.set_name('Chicago Style Cheese Pizza')
            return pizza
        elif pizza_type == PizzaType.CLAM:
            pizza = ClamPizza(ChicagoPizzaIngredientFactory())
            pizza.set_name('Chicago Style Clam Pizza')
            return pizza
        elif pizza_type == PizzaType.PEPPERONI:
            pizza = PepperoniPizza(ChicagoPizzaIngredientFactory())
            pizza.set_name('Chicago Style Pepperoni Pizza')
            return pizza
        else: #default to veggie
            pizza = VeggiePizza(ChicagoPizzaIngredientFactory())
            pizza.set_name('Chicago Style Veggie Pizza')
            return pizza