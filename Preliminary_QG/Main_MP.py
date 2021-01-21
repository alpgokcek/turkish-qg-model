from pprint import pprint
from fuzzywuzzy import fuzz
from PersonDataParser import Parser
from QuestionPatterns import QuestionPatterns
from bs4 import BeautifulSoup
import json
import os
from multiprocessing import Pool

THRESHOLD = 70
parser = Parser("everyone.txt")
parser.parse()

counter = 0
patterns = QuestionPatterns.patterns

out = open("out_data.txt", 'w')
full_wiki = open("wiki_new1.html").read()
soup = BeautifulSoup(full_wiki, "html.parser")


output_dict = {'data': list()}
print("Total persons: ", parser.get_person_count())
print("\nTop Occupations and their attributes: ")
persons = parser.get_persons()
occupations = parser.get_occupations()
occupations_with_attr = parser.get_top_occupations_and_attributes(top=10)

def process(enum):
    index, p = enum
    print(index)
    temp_dict = dict()
    description_tag = soup.find("div", {"id": int(p.doc_id)})
    if description_tag:
        description = description_tag.get_text().replace('\n', '')
        del description_tag
        temp_dict['description'] = description
        temp_dict['data'] = list()
        for pattern_type in patterns[p.occupation].keys():
            if pattern_type in p.attributes.keys():
                answer = p.attributes[pattern_type]
                temp_dict1 = {'answer': answer, 'questions': list()}
                for question in patterns[p.occupation][pattern_type]:                
                    if '~' not in question and '#' not in question: 
                        ratio = fuzz.partial_ratio(description, p.attributes[pattern_type])
                        if ratio > THRESHOLD:
                            temp_dict1['questions'].append(question.format(name=p.name))
                if len(temp_dict1['questions']) > 0:
                        temp_dict['data'].append(temp_dict1)
                else:
                    del temp_dict1
        if len(temp_dict['data']) > 0:
            out.write(json.dumps(temp_dict, ensure_ascii=False) + ", \n")
        del temp_dict




if __name__ == '__main__':
    pool = Pool(os.cpu_count()) # Create a multiprocessing Pool
    pool.map(process, enumerate(persons))
    pool.close()
    pool.join()
