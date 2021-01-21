from Person import Person
from typing import Set, Dict, List
from collections import defaultdict
import json


class Parser:
    def __init__(self, path):
        self.path = path
        self.string = open(path, 'r').read().rstrip()
        self.paragraphs = []
        self.persons: List[Person] = []
        self.occupations: Dict[str, int] = {}
        self.occupations_and_attr: Dict[str, defaultdict] = {}

    def parse(self):
        paragraphs = self.string.split('\n\n')
        for par in paragraphs:
            attributes = par.split('#')
            doc_id = attributes[0]
            name = attributes[1]
            occup = attributes[2]
            self.occupations[occup] = self.occupations.get(occup, 0) + 1
            attr: Dict[str, str] = json.loads(attributes[4])
            self.drop_key(attr, "ad")
            self._add_attr_to_occupations(occup, attr)
            short_desc = attributes[7]
            self.persons.append(Person(doc_id, name, occup, attr, short_desc))
    def get_occupations(self):
        return self.occupations

    def get_person_count(self):
        return len(self.persons)

    def get_persons(self):
        return self.persons

    def _add_attr_to_occupations(self, occup, attr):
        if occup in self.occupations_and_attr:
            for key in attr.keys():
                _key = key.lower()
                self.occupations_and_attr[occup][_key] += 1
        else:
            self.occupations_and_attr[occup] = defaultdict(int)
            self._add_attr_to_occupations(occup, attr)

    def get_top_occupations_and_attributes(self, top: int = None):
        var = self.occupations_and_attr
        for key, val in var.items():
            tmp = var[key]
            var[key] = sorted(tmp.items(), key=lambda kv: kv[1], reverse=True)[:top]
        return var

    @staticmethod
    def drop_key(d: Dict, key):
        try:
            del d[key]
        except KeyError:
            pass