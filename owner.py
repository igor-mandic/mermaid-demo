from animal import Animal

class Owner:
    """Can own multiple pets"""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.pets: List[Animal] = []
    
    def add_pet(self, pet: Animal) -> None:
        self.pets.append(pet)
        print(f"{self.name} now owns {pet.name}!")
    
    def feed_pet(self, pet: Animal) -> None:
        if pet in self.pets:
            print(f"{self.name} is feeding {pet.name}")
            pet.eat()
        else:
            print(f"{pet.name} is not owned by {self.name}")
    
    def walk_pet(self, pet: Animal) -> None:
        if pet in self.pets and isinstance(pet, Dog):
            print(f"{self.name} is walking {pet.name}")
        elif pet in self.pets:
            print(f"{pet.name} doesn't need to be walked")
        else:
            print(f"{pet.name} is not owned by {self.name}")
    
    def list_pets(self) -> None:
        if self.pets:
            print(f"{self.name}'s pets:")
            for pet in self.pets:
                print(f"  - {pet}")
        else:
            print(f"{self.name} has no pets")