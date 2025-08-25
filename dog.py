from typing import List
from abc import ABC, abstractmethod
from animal import Animal

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str, is_trained: bool = False):
        super().__init__(name, age, "Dog")
        self.breed = breed
        self.is_trained = is_trained
    
    def make_sound(self) -> None:
        self.bark()
    
    def bark(self) -> None:
        print(f"{self.name} says: Woof! Woof!")
    
    def fetch(self) -> None:
        if self.is_trained:
            print(f"{self.name} fetches the ball!")
        else:
            print(f"{self.name} doesn't know how to fetch yet.")