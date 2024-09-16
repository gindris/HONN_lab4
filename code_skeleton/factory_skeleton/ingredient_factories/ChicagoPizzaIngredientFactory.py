import PizzaIngredientFactory
from ingredients.dough.ThickCrustDough import ThickCrustDough
from ingredients.sauce.PlumTomatoSauce import PlumTomatoSauce
from ingredients.cheese.Mozzarella import Mozzarella
from ingredients.clams.FrozenClams import FrozenClams
from ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from ingredients.veggies import EggPlant, Spinach, BlackOlives

class ChicagoIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return Mozzarella()

    def create_veggies(self):
        return [EggPlant(), Spinach(), BlackOlives()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clams(self):
        return FrozenClams()