from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from ingredients.dough.ThinCrustDough import ThinCrustDough
from ingredients.sauce.MarinaraSauce import MarinaraSauce
from ingredients.cheese.ReggianoCheese import ReggianoCheese
from ingredients.clams.FreshClams import FreshClams
from ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from ingredients.veggies.Garlic import Garlic
from ingredients.veggies.Onion import Onion
from ingredients.veggies.Mushroom import Mushroom
from ingredients.veggies.RedPepper import RedPepper

class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def __init__(self):
        pass
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clams(self):
        return FreshClams()