from pprint import pprint
from fuzzywuzzy import fuzz
from PersonDataParser import Parser
from QuestionPatterns import QuestionPatterns
from bs4 import BeautifulSoup
import time
THRESHOLD = 70
parser = Parser("everyone.txt")
parser.parse()


patterns = QuestionPatterns.patterns

out = open("out_data.txt", 'w')
full_wiki = open("wiki_new1.html").read()
soup = BeautifulSoup(full_wiki, "html.parser")
start=time.time()
long_info = soup.find("div", {"id": 16}).get_text()
end=time.time()
print(end-start)
start=time.time()
long_info = soup.find("div", {"id": 10}).get_text()
end=time.time()
print(end-start)
start=time.time()
long_info = soup.find("div", {"id": 1442}).get_text()
end=time.time()
print(end-start)
start=time.time()
long_info = soup.find("div", {"id": 3886}).get_text()
end=time.time()
print(end-start)
print(long_info, type(long_info))
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
def main():
    output_dict = {'data': list()}
    print("Total persons: ", parser.get_person_count())
    print("\nTop Occupations and their attributes: ")
    persons = parser.get_persons()
    occupations = parser.get_occupations()
    occupations_with_attr = parser.get_top_occupations_and_attributes(top=10)
    # pprint(occupations_with_attr)
    i = 0
    for p in persons:
        print(i)
        i+=1
        temp_dict = dict()
        description = soup.find("div", {"id": int(p.doc_id)})
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
        output_dict['data'].append(temp_dict)
print(output_dict)




if __name__ == '__main__':
    #main()
    pass
