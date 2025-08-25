from typing import List
from abc import ABC, abstractmethod

class Animal(ABC):
    """Base class for all animals"""
    
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
    
    def eat(self) -> None:
        print(f"{self.name} is eating.")
    
    def sleep(self) -> None:
        print(f"{self.name} is sleeping.")
    
    @abstractmethod
    def make_sound(self) -> None:
        """Each animal makes a different sound"""
        pass
    
    def __str__(self) -> str:
        return f"{self.name} ({self.species}, {self.age} years old)"