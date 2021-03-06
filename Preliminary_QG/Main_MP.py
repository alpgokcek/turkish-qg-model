from pprint import pprint
from fuzzywuzzy import fuzz
from PersonDataParser import Parser
from QuestionPatterns import QuestionPatterns
from bs4 import BeautifulSoup
import json
import os
from multiprocessing import Pool
from turkish_suffix_library.turkish import Turkish

THRESHOLD = 70
parser = Parser("data/wiki_persons.txt")
parser.parse()

counter = 0
patterns = QuestionPatterns.patterns

out = open("out_data.txt", 'w')
full_wiki = open("data/wiki_whole_data.html").read()
soup = BeautifulSoup(full_wiki, "html.parser")


output_dict = {'data': list()}
print("Total persons: ", parser.get_person_count())
print("\nTop Occupations and their attributes: ")
persons = parser.get_persons()
occupations = parser.get_occupations()
occupations_with_attr = parser.get_top_occupations_and_attributes(top=10)

_suffix1, _suffix2, _suffix3 = "_suffix1", "_suffix2", "_suffix3"

def get_suffix(word: str, sffx_type: str):
    suffix = ''
    if sffx_type == "_suffix1":
        suffix = Turkish(word).possessive(person=2)
    elif sffx_type == "_suffix2":
        suffix = Turkish(word).dative()
    elif sffx_type == "_suffix3":
       suffix = Turkish(word).ablative()
    suffix = str(suffix)
    return suffix[len(word):]
    
def process(enum):
    index, p = enum
    print("Idx,", index, "P", p)
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
                    temp_question = question.format(name=p.name)
                    print(temp_question)
                    ratio = fuzz.partial_ratio(description, p.attributes[pattern_type])
                    if ratio > THRESHOLD:
                        try:
                            if _suffix1 in temp_question:
                                temp_question = temp_question.format(_suffix1=get_suffix(p.name, "_suffix1"))
                            if _suffix2 in temp_question:
                                temp_question = temp_question.format(_suffix2=get_suffix(p.name, "_suffix2"))
                            if _suffix3 in temp_question:
                                temp_question = temp_question.format(_suffix3=get_suffix(p.name, "_suffix3"))
                            temp_dict1['questions'].append(temp_question)
                        except Exception as a:
                            print("ANAM SIKILDI", a,"BU SIKTI", p.name, temp_question)
                
                if len(temp_dict1['questions']) > 0:
                    temp_dict['data'].append(temp_dict1)
                else:
                    del temp_dict1
        if len(temp_dict['data']) > 0:
            out.write(json.dumps(temp_dict, ensure_ascii=False) + ", \n")
        del temp_dict


if __name__ == '__main__':
    pool = Pool(os.cpu_count()) # Create a multiprocessing Pool
   # pool.map(get_suffix, enumerate(persons))
    pool.map(process, enumerate(persons))
    pool.close()
    pool.join()
