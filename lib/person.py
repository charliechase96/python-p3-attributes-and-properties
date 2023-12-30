#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="None"):
        self.name = name  # This will call the setter
        self.job = job  # This will call the setter

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            if 1 <= len(name) <= 25:
                self._name = name.title()  # Converts string to title case before saving
            elif len(name) == 0:
                print(f"Name must be string between 1 and 25 characters.")
            elif len(name) > 25:
                print(f"Name must be string between 1 and 25 characters.")
            else:
                print("Name must be string between 1 and 25 characters.")
        else:
            print(f"Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
