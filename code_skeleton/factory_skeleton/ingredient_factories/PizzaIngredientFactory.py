from abc import ABC, abstractmethod
from ingredients.cheese.Cheese import Cheese
from ingredients.clams.Clams import Clams
from ingredients.dough.Dough import Dough
from ingredients.pepperoni.Pepperoni import Pepperoni
from ingredients.sauce.Sauce import Sauce
from ingredients.veggies.Veggies import Veggies
from typing import List

#abstrac/iteface fyrir NY og Chicago ingredient factories að erfa
class PizzaIngredientFactory(ABC):
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
