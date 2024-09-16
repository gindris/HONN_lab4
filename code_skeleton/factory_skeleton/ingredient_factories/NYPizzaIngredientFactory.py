from factory_skeleton.ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from factory_skeleton.ingredients.dough.ThinCrustDough import ThinCrustDough
from factory_skeleton.ingredients.sauce.MarinaraSauce import MarinaraSauce
from factory_skeleton.ingredients.cheese.ReggianoCheese import ReggianoCheese
from factory_skeleton.ingredients.clams.FreshClams import FreshClams
from factory_skeleton.ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from factory_skeleton.ingredients.veggies import Garlic, Onion, Mushroom, RedPepper

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