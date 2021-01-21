from pprint import pprint
from fuzzywuzzy import fuzz
from PersonDataParser import Parser
from QuestionPatterns import QuestionPatterns

THRESHOLD = 60


def main():

    parser = Parser("everyone.txt")
    parser.parse()


    patterns = QuestionPatterns.patterns

    out = open("out_data.txt", 'w')

    print("Total persons: ", parser.get_person_count())
    print("\nTop Occupations and their attributes: ")
    persons = parser.get_persons()
    occupations = parser.get_occupations()
    occupations_with_attr = parser.get_top_occupations_and_attributes(top=10)
    # pprint(occupations_with_attr)
    for p in persons:
        description = p.description
        out.write(p.name + '->' + p.occupation + "\nDescription:" + description + '\n')
        for pattern_type in patterns[p.occupation].keys():
            for question in patterns[p.occupation][pattern_type]:
                if pattern_type in p.attributes.keys():
                    answer = p.attributes[pattern_type]
                    if '~' not in question and '#' not in question:
                        ratio = fuzz.partial_ratio(p.description, p.attributes[pattern_type])
                        if ratio > THRESHOLD:
                            out.write(question.format(name=p.name) + '\n')
                            out.write("Answer: "+ answer +"\n")






if __name__ == '__main__':
    main()
