from pprint import pprint
from fuzzywuzzy import fuzz
from PersonDataParser import Parser
from QuestionPatterns import QuestionPatterns
from bs4 import BeautifulSoup
import json
import multiprocessing

THRESHOLD = 70
parser = Parser("everyone.txt")
parser.parse()
patterns = QuestionPatterns.patterns
_suffix1, _suffix2, _suffix3 = "_suffix1", "_suffix2", "_suffix3"


full_wiki = open("wiki_new1.html").read()
soup = BeautifulSoup(full_wiki, "html.parser")


output_dict = {'data': list()}
print("Total persons: ", parser.get_person_count())
print("\nTop Occupations and their attributes: ")
persons = parser.get_persons()
occupations = parser.get_occupations()
occupations_with_attr = parser.get_top_occupations_and_attributes(top=10)

def get_suffix(suffix_type):
    if suffix_type == _suffix1:
        pass
    elif suffix_type == _suffix2:
        pass
    elif suffix_type == _suffix3:
        pass

def main():
    out = open("output_files/out_data_{}.txt".format(index), 'w')
    i, file_index = 0, 0
    FILE_COUNT = 50
    total_count = parser.get_person_count()
    divide, remainder = int(total_count/FILE_COUNT), total_count % FILE_COUNT
    NEXT_END = divide + remainder

    for p in persons:
        print(i)
        i+=1
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
                        temp_question = question
                        if _suffix1 in question:
                            temp_question = temp_question.format(_suffix1=get_suffix(_suffix1))
                        if _suffix2 in question:
                            temp_question = temp_question.format(_suffix2=get_suffix(_suffix2))
                        if _suffix3 in question:
                            temp_question = temp_question.format(_suffix3=get_suffix(_suffix3))
                        
                        ratio = fuzz.partial_ratio(description, p.attributes[pattern_type])
                        if ratio > THRESHOLD:
                            temp_dict1['questions'].append(temp_question.format(name=p.name))
                        
                    if len(temp_dict1['questions']) > 0:
                        temp_dict['data'].append(temp_dict1)
                    else:
                        del temp_dict1
            if len(temp_dict['data']) > 0:
                out.write(json.dumps(temp_dict, ensure_ascii=False) + ", \n")
            del temp_dict
        if i == NEXT_END:
            out.close()
            index += 1
            out = open("output_files/out_data_{}.txt".format(index), 'w')
            NEXT_END += divide


if __name__ == '__main__':
    main()

'''
{
    data: [
        {
        description: str,
        data: [
            {
                questions: [str],
                answer: str
            }
        }
    ]
}
'''