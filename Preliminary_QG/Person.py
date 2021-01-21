
class Person:
    def __init__(self, name, occupation, attributes, description):
        self.name = name
        self.occupation = occupation
        self.attributes = attributes
        self.description = description

    def __str__(self):
        return "{}: {} \n\t\t{}".format(self.name, self.occupation, self.description)
