from typing import List
from abc import ABC, abstractmethod
from animal import Animal

class Cat(Animal):
    def __init__(self, name: str, age: int, color: str, is_indoor: bool = True):
        super().__init__(name, age, "Cat")
        self.color = color
        self.is_indoor = is_indoor
    
    def make_sound(self) -> None:
        self.meow()
    
    def meow(self) -> None:
        print(f"{self.name} says: Meow!")
    
    def purr(self) -> None:
        print(f"{self.name} is purring contentedly.")