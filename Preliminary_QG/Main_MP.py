from pprint import pprint
from fuzzywuzzy import fuzz
from PersonDataParser import Parser
from QuestionPatterns import QuestionPatterns
from CommonPatterns import  CommonPatterns
from bs4 import BeautifulSoup
import json
import os
from multiprocessing import Pool
from turkish_suffix_library.turkish import Turkish

THRESHOLD = 70
parser = Parser("sample_data/sample_wiki_persons.txt")
parser.parse()

counter = 0
occupational_patterns = QuestionPatterns.patterns
common_patterns = CommonPatterns.patterns


out = open("out/data.txt", 'w')
full_wiki = open("sample_data/sample_wiki_dump.html").read()
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
        suffix = Turkish(word).genitive(person=2)
    elif sffx_type == "_suffix2":
        suffix = Turkish(word).dative()
    elif sffx_type == "_suffix3":
        suffix = Turkish(word).ablative()
    suffix = str(suffix)
    return suffix[len(word):]


def create_common_questions(enum):
	index, p = enum
	for question in common_patterns:
		print("Person: ",p)
		print("Question: ",question)
		print("\n\n")

def process(enum):
    index, p = enum
    print("Idx,", index, "P", p)
    person_dict = dict()
    description_tag = soup.find("div", {"id": int(p.doc_id)}) # large description text
    if description_tag: 
        description = description_tag.get_text().replace('\n', '')
        del description_tag
        person_dict['description'] = "description"
        person_dict['data'] = list()
        feature_patterns = occupational_patterns[p.occupation]
        for pattern_type in feature_patterns.keys(): # pattern type = rutbesi, pozisyon, etc.
            if pattern_type in p.attributes.keys():
                answer = p.attributes[pattern_type]
                qa_pair = {'answer': answer, 'questions': list()}
                for question in feature_patterns[pattern_type]:
                    temp_question = question
                    #print(temp_question)
                    ratio = fuzz.partial_ratio(
                        description, p.attributes[pattern_type])
                    if ratio > THRESHOLD:
                        try:
                            if _suffix1 in temp_question:
                                temp_question = temp_question.format(
                                    name=p.name, _suffix1=get_suffix(p.name, _suffix1))
                            elif _suffix2 in temp_question:
                                temp_question = temp_question.format(
                                    name=p.name, _suffix2=get_suffix(p.name, _suffix2))
                            elif _suffix3 in temp_question:
                                temp_question = temp_question.format(
                                    name=p.name, _suffix3=get_suffix(p.name, _suffix3))
                            else:
                                temp_question = question.format(name=p.name)
                            qa_pair['questions'].append(temp_question)
                        except Exception as e:
                            print("Error on: {} - {} \n{}\n".format(e,
                                                                    p.name, temp_question))
                if len(qa_pair['questions']) > 0:
                    person_dict['data'].append(qa_pair)
                else:
                    del qa_pair
        if len(person_dict['data']) > 0:
            out.write(json.dumps(person_dict, ensure_ascii=False) + ", \n")
        del person_dict


if __name__ == '__main__':
    pool = Pool(os.cpu_count())  # Create a multiprocessing Pool
    pool.map(create_common_questions, enumerate(persons))
    #pool.map(process, enumerate(persons))
    pool.close()
    pool.join()
