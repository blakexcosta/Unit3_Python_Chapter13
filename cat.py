class Cat:
    def __init__(self, a_name, an_age, id_number="Missing"):
        self.name = a_name
        self.age = an_age
        self.id = id_number

    # this is like the tostring method in other languages
    def __str__(self):
        output = f"name:{self.name}\nage:{self.age}\nid:{self.id}"
        return output

    def meow(self):
        print(f"{self.name}: meow")
