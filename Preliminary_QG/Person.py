
class Person:
    def __init__(self, doc_id, name, occupation, attributes, description):
        self.name = name
        self.doc_id = doc_id
        self.occupation = occupation
        self.attributes = attributes
        self.description = description

    def __str__(self):
        return "{}: {} \n\t{}".format(self.doc_id, self.name, self.occupation, self.description)
