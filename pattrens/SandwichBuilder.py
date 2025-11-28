from abc import ABC, abstractmethod
from typing import List, Optional

# Sandwich Builder Pattern
class Sandwich:
    """Product class representing a sandwich"""
    
    def __init__(self):
        self.ingredients: List[str] = []
        
    def add(self, ingredient: str):
        self.ingredients.append(ingredient)
        
    def show(self):
        print(f"Sandwich configuration: {', '.join(self.ingredients)}")

class SandwichBuilder(ABC):
    """Abstract builder for sandwiches"""
    
    def __init__(self):
        self.sandwich = Sandwich()
        
    @abstractmethod
    def _add_bread(self):
        pass
        
    @abstractmethod
    def _add_protein(self):
        pass
        
    @abstractmethod
    def _add_vegetables(self):
        pass
        
    @abstractmethod
    def _add_sauce(self):
        pass

class ShawarmaBuilder(SandwichBuilder):
    def _add_bread(self):
        self.sandwich.add("Bread")
            
    def _add_protein(self):
        self.sandwich.add("Shawarma Chicken")
            
    def _add_vegetables(self):
        self.sandwich.add("Salad")
        self.sandwich.add("frites")
            
    def _add_sauce(self):
        self.sandwich.add("Mayonnaise")
        self.sandwich.add("Harissa")

class GroundMeatBuilder(SandwichBuilder):
    def _add_bread(self):
        self.sandwich.add("bread")
            
    def _add_protein(self):
        self.sandwich.add("viande achée")
            
    def _add_vegetables(self):
        self.sandwich.add("salade")
        self.sandwich.add("frites")
            
    def _add_sauce(self):
        self.sandwich.add("Mayonnaise")

class FriesOmeletteBuilder(SandwichBuilder):
    def _add_bread(self):
        self.sandwich.add("Bread")
            
    def _add_protein(self):
        self.sandwich.add("Eggs")
            
    def _add_vegetables(self):
        self.sandwich.add("frites")
            
    def _add_sauce(self):
        self.sandwich.add("mayonnaise")
        self.sandwich.add("hrissa")

# Director
class SandwichDirector:
    def __init__(self):
        self.builder: Optional[SandwichBuilder] = None
            
    def construct(self, builder: SandwichBuilder):
        self.builder = builder
            
    def construct_shawarma(self):
        self.builder._add_bread()
        self.builder._add_protein()
        self.builder._add_vegetables()
        self.builder._add_sauce()

# Test the implementations
print("Shawarma Configuration:")
shawarma_builder = ShawarmaBuilder()
director = SandwichDirector()
director.construct(shawarma_builder)
director.construct_shawarma()
sandwich = shawarma_builder.sandwich
sandwich.show()

print("\nGround Meat Configuration:")
ground_meat_builder = GroundMeatBuilder()
director = SandwichDirector()
director.construct(ground_meat_builder)
director.construct_shawarma()  # Same process works for different configurations
sandwich = ground_meat_builder.sandwich
sandwich.show()

print("\nFries with Omelette Configuration:")
fries_builder = FriesOmeletteBuilder()
director = SandwichDirector()
director.construct(fries_builder)
director.construct_shawarma()  # Same process works for different configurations
sandwich = fries_builder.sandwich
sandwich.show()