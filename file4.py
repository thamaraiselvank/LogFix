class Pet:
    def __init__(self, name, species):
        if not name or not species:
            raise ValueError("Pet name and species are required.")
        self.name = name
        self.species = species
class Clinic:
    def __init__(self):
        self.pets = []
 
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise ValueError("Invalid pet object")
        if pet in self.pets:
            raise ValueError("Pet already exists in the clinic Please provide different name")
        self.pets.append(pet)
 
    def remove_pet(self, pet):
        if pet not in self.pets:
            raise ValueError("Pet not found in the clinic Please check the Pet name")
        self.pets.remove(pet)
 
    def update_pet_info(self, pet, new_name, new_species):
        if pet not in self.pets:
            raise ValueError("Pet not found in the clinic Please check the Pet name")
        pet.name = new_name
        pet.species = new_species
clinic = Clinic()
try:
    pet1 = Pet("Buddy", "Dog")
    clinic.add_pet(pet1)
    print("INFO: Pet added successfully.")
except ValueError as ve:
    print(f"Test Case 1: ValueError - {ve}")
except Exception as e:
    print(f"Test Case 1: Unexpected error - {e}")
try:
    clinic.add_pet(pet1)
    print("INFO: Pet added successfully.")
except ValueError as ve:
    print(f"Error: ValueError - {ve}")
except Exception as e:
    print(f"Test Case 2: Unexpected error - {e}")
try:
    pet2 = Pet("Whiskers", "Cat")
    clinic.add_pet(pet2)
    print("INFO: Pet added successfully.")
except ValueError as ve:
    print(f"Error: ValueError - {ve}")
except Exception as e:
    print(f"Test Case 3: Unexpected error - {e}")
try:
    clinic.remove_pet(Pet("NonExistent", "Unknown"))
    print("Pet removed successfully.")
except ValueError as ve:
    print(f"Error: ValueError - {ve}")
except Exception as e:
    print(f"Test Case 4: Unexpected error - {e}")
try:
    clinic.update_pet_info(Pet("NonExistent", "Unknown"), "NewName", "NewSpecies")
    print("Pet information updated successfully.")
except ValueError as ve:
    print(f"Error: ValueError - {ve}")
except Exception as e:
    print(f"Test Case 5: Unexpected error - {e}")
try:
    clinic.update_pet_info(pet1, "", "NewSpecies")
    print("INFO: Pet information updated successfully.")
except ValueError as ve:
    print(f"Test Case 6: ValueError - {ve}")
except Exception as e:
    print(f"Test Case 6: Unexpected error - {e}")