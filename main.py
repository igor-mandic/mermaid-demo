
from dog import Dog
from cat import Cat
from owner import Owner


# Example usage
if __name__ == "__main__":
    # Create pets
    buddy = Dog("Buddy", 3, "Golden Retriever", is_trained=True)
    whiskers = Cat("Whiskers", 2, "Orange", is_indoor=True)
    
    # Create owner
    john = Owner("John Smith", "john@example.com")
    
    # Add pets to owner
    john.add_pet(buddy)
    john.add_pet(whiskers)
    
    # Interact with pets
    john.list_pets()
    print()
    
    john.feed_pet(buddy)
    john.walk_pet(buddy)
    print()
    
    john.feed_pet(whiskers)
    whiskers.purr()
    print()
    
    # Make sounds
    buddy.make_sound()
    whiskers.make_sound()
    
    # Dog-specific behavior
    buddy.fetch()