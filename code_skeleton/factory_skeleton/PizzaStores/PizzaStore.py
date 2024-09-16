from abc import ABC, abstractmethod


class PizzaStore(ABC):
    #TODO: order pizza method

    #abstract eða ekki?
    def order_pizza(self, pizza_type: str):
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        #print(f'Ordered {pizza_type} pizza')

        return pizza
    
    @abstractmethod
    def create_pizza(self, pizza_type: str):
        #to be implemented by subclass
        pass
