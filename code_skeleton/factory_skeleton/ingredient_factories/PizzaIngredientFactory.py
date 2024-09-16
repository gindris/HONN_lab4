from abc import ABC, abstractmethod
from factory_skeleton.ingredients.cheese import Cheese
from factory_skeleton.ingredients.clams import Clams
from factory_skeleton.ingredients.dough import Dough
from factory_skeleton.ingredients.pepperoni import Pepperoni
from factory_skeleton.ingredients.sauce import Sauce
from factory_skeleton.ingredients.veggies import Veggies
from typing import List

#abstrac/iteface fyrir NY og Chicago ingredient factories að erfa
class PizzaIngredientFactory(ABC):
    def __init__(self):
        pass
    #something something abstract factory pattern
    @abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abstractmethod
    def create_sauce(self) -> Sauce:
        pass

    @abstractmethod
    def create_cheese(self) -> Cheese:
        pass

    @abstractmethod
    def create_veggies(self) -> List[Veggies]:
        pass

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        pass

    @abstractmethod
    def create_clams(self) -> Clams:
        pass
