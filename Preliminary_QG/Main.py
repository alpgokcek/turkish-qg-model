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


full_wiki = open("wiki_new1.html").read()
soup = BeautifulSoup(full_wiki, "html.parser")

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
output_dict = {'data': list()}
print("Total persons: ", parser.get_person_count())
print("\nTop Occupations and their attributes: ")
persons = parser.get_persons()
occupations = parser.get_occupations()
occupations_with_attr = parser.get_top_occupations_and_attributes(top=10)

def main(index, start, end):
    out = open("out_data_{}.txt".format(index), 'w')
    # pprint(occupations_with_attr)
    i = 0
    for p in persons[start:end]:
        print(i)
        i+=1
        temp_dict = dict()
        description_tag = soup.find("div", {"id": int(p.doc_id)})
        if description_tag:
            description = description_tag.get_text()
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
            if len(temp_dict['data']) > 0:
                out.write(json.dumps(temp_dict, ensure_ascii=False))




if __name__ == '__main__':
    CORE_COUNT = 8
    processes = []
    total_count = parser.get_person_count()
    divide, remainder = int(total_count/CORE_COUNT), total_count % CORE_COUNT
    start, end = 0, divide
    for i in range(0, CORE_COUNT):
        prpcess = multiprocessing.Process(target=main, args=(i, start, end))
        processes.append(prpcess)
        prpcess.start()
        start, end = end, end+divide
    for process in processes:
        process.join()