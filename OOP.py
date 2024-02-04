class Person:
    def __init__(self, name, age, hometown, occupation, skills=[], favourite_food=""):
        self.name = name
        self.age = age
        self.hometown = hometown
        self.skills = skills
        self.favourite_food = favourite_food
        self.occupation = occupation

    def greet_someone(self, name):
        print(f"Hello {name}! I'm {self.name}. Nice to meet you!\n")

    def update_age(self, new_age):
        if new_age > self.age:
            self.age = new_age
            print(f"Happy birthday {self.name}! You are now {self.age} years old!")
        else:
            print(
                "Invalid input! New age should be greater than current age. Try again."
            )

    def __str__(self):
        return f"""
Name: {self.name}
Age: {self.age}
Hometown: {self.hometown}
Occupation: {self.occupation}
Skills: {self.skills if self.skills != [] else None}
Favourite food: {self.favourite_food if self.favourite_food != "" else None}.
"""

    def update_occupation(self, new_occupation):
        if new_occupation != "":
            self.occupation = new_occupation
            print(f"Congratulation! Now your occupation is: {self.occupation}")
        else:
            print("Invalid input. Try again.")

    def add_skills(self, new_skills):
        pass


person1 = Person("Abd", 12, "Feni", "Painter")
print(person1)
person1.greet_someone("Jo")
person1.update_age(15)
