from abc import ABC, abstractmethod
from typing import List, Optional

# Car Builder Pattern
class Car:
    """Product class representing a car"""
    
    def __init__(self):
        self.features: List[str] = []
        
    def add(self, feature: str):
        self.features.append(feature)
        
    def show(self):
        print(f"Car configuration: {', '.join(self.features)}")

class CarBuilder(ABC):
    """Abstract builder for cars"""
    
    def __init__(self):
        self.car = Car()
        
    @abstractmethod
    def _add_engine(self):
        pass
        
    @abstractmethod
    def _add_transmission(self):
        pass
        
    @abstractmethod
    def _add_interior(self):
        pass
        
    @abstractmethod
    def _add_options(self):
        pass

class BasicCarBuilder(CarBuilder):
    def _add_engine(self):
        self.car.add("Basic Engine")
            
    def _add_transmission(self):
        self.car.add("Manual Transmission")
            
    def _add_interior(self):
        self.car.add("Standard Interior")
            
    def _add_options(self):
        self.car.add("Basic Radio")

class FullOptionCarBuilder(CarBuilder):
    def _add_engine(self):
        self.car.add("Premium Engine")
            
    def _add_transmission(self):
        self.car.add("Automatic Transmission")
            
    def _add_interior(self):
        self.car.add("Luxury Interior")
            
    def _add_options(self):
        self.car.add("Premium Sound System, Navigation, Sunroof")

# Director
class CarDirector:
    def __init__(self):
        self.builder: Optional[CarBuilder] = None
            
    def construct(self, builder: CarBuilder):
        self.builder = builder
            
    def construct_basic_car(self):
        self.builder._add_engine()
        self.builder._add_transmission()
        self.builder._add_interior()
        self.builder._add_options()

# Test the implementations
print("Basic Car Configuration:")
basic_car_builder = BasicCarBuilder()
director = CarDirector()
director.construct(basic_car_builder)
director.construct_basic_car()
car = basic_car_builder.car
car.show()

print("\nFull Option Car Configuration:")
full_option_builder = FullOptionCarBuilder()
director = CarDirector()
director.construct(full_option_builder)
director.construct_basic_car()  # Same process works for different configurations
car = full_option_builder.car
car.show()