#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", breed="Unknown"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            if 1 <= len(name) <= 25:
                self._name = name
            elif len(name) == 0:
                print("Name must be string between 1 and 25 characters.\n")
            elif len(name) > 25:
                print("Name must be string between 1 and 25 characters.\n")
            else:
                print("Name must be string between 1 and 25 characters.\n")
        else:
            print("Name must be string between 1 and 25 characters.\n")

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)