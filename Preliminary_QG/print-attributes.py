from pprint import pprint
from PersonDataParser import Parser


def main():
    parser = Parser("everyone.txt")
    parser.parse()

    print("Total persons: ", parser.get_person_count())
    print("\nTop Occupations and their attributes: ")
    persons = parser.get_persons()
    occupations = parser.get_occupations()
    occupations_with_attr = parser.get_top_occupations_and_attributes(top=10)
    pprint(occupations_with_attr)


if __name__ == '__main__':
    main()