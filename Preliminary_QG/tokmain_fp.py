import random
import string
random.seed(5)
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from pprint import pprint
from fuzzywuzzy import fuzz
from PersonDataParser import Parser
from QuestionPatterns import QuestionPatterns
from CommonPatterns import CommonPatterns

from MinifiedQuestionPatterns import MinifiedQuestionPatterns
from MinifiedCommonPatterns import MinifiedCommonPatterns

from bs4 import BeautifulSoup
from Person import Person
import json
import os
from multiprocessing import Pool
from turkish_suffix_library.turkish import Turkish
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--output", help="path of output file",
        type=str)
parser.add_argument(
        "--dev", help="development environment selection", action='store_true')
args = parser.parse_args()

ATTRIBUTES_PATH = "sample_data/sample_wiki_persons.txt" if args.dev else "data/wiki_persons.txt"
WIKI_PATH = "sample_data/sample_wiki_dump.html" if args.dev else "data/wiki_whole_data.html"
OUTPUT_PATH = "out/data.json" if not args.output else args.output
CONFIG_FILE = json.load(open('config.json', 'r'))

OCCUPATION_SETTINGS = CONFIG_FILE["occupation_settings"]


THRESHOLD = 60
parser = Parser(ATTRIBUTES_PATH)
parser.parse()

occupational_patterns = QuestionPatterns.patterns if not CONFIG_FILE[
        'use_minified'] else MinifiedQuestionPatterns.patterns
common_patterns = CommonPatterns.patterns if not CONFIG_FILE[
        'use_minified'] else MinifiedCommonPatterns.patterns

#print("occupational_patterns", occupational_patterns)


out = open("out/data_tokmain_fp.txt", 'w')
full_wiki = open(WIKI_PATH).read()
soup = BeautifulSoup(full_wiki, "html.parser")


output_dict = {'data': list()}
#print("Total persons: ", parser.get_person_count())
#print("\nTop Occupations and their attributes: ")
persons = parser.get_persons()
occupations = parser.get_occupations()
occupations_with_attr = parser.get_top_occupations_and_attributes(top=10)

def create_common_questions(p: Person):
    bitmap = OCCUPATION_SETTINGS[p.occupation]["common_questions"]
    pair_list = list()
    for i, (feature, question_patterns) in enumerate(common_patterns.items()):
        if bitmap[i] == "0":
            continue
        elif feature in p.attributes:
            ans = p.attributes[feature]
            qa_pair = {'answer': ans, 'questions': list()}
            for pattern in question_patterns:
                q = pattern 
                if q:
                    qa_pair['questions'].append(q)
            pair_list.append(qa_pair)
    return pair_list


def process(enum):
    index, p = enum
    print("Idx,", index, "P", p)
    person_dict = dict()
    description_tag = soup.find(
            "div", {"id": int(p.doc_id)})  # large description text
    if description_tag:
        description = description_tag.get_text().split("\n")[3]
        description = description.translate(str.maketrans('', '', string.punctuation))
        description = f"<{p.name}>{description}"
        del description_tag
        sentence_tokenizations = sent_tokenize(description)
        person_dict['data'] = list()
        desc_list = {1: sentence_tokenizations[0]}
        common_questions = create_common_questions(p)
        person_dict['data'] = person_dict['data'] + common_questions
        feature_patterns = occupational_patterns[p.occupation]
        # pattern type = rutbesi, pozisyon, etc.
        for pattern_type in feature_patterns.keys():
            if pattern_type in p.attributes.keys():
                answer = p.attributes[pattern_type]
                qa_pair = {'answer': answer, 'questions': list()}
                for question_pattern in feature_patterns[pattern_type]:
                    # does the description paragraph contain answer?
                    for i, sent in enumerate(sentence_tokenizations):
                        ratio = int(fuzz.partial_token_set_ratio(
                            sent, answer))
                        if ratio > THRESHOLD:
                            desc_list[i] = sent
                    #   else:
                    #      if random.randint(0, 31) == 2:
                    #         desc_list[i] = sentence_tokenizations[i]
                    q = question_pattern
                    if q:
                        qa_pair['questions'].append(q)
                if len(qa_pair['questions']) > 0:  # if any relevant qa pair is present
                    person_dict['data'].append(qa_pair)
                else:
                    del qa_pair
        if len(person_dict['data']) > 0:
            out = open("out/data_tokmain_fp.txt", 'a')
            person_dict['description'] = ' '.join(desc_list.values())
            person_dict['name'] = p.name
            out.write(json.dumps(person_dict, ensure_ascii=False) + ",\n")
            out.close()

        del person_dict


if __name__ == '__main__':
    pool = Pool(os.cpu_count())  # Create a multiprocessing Pool
    pool.map(process, enumerate(persons))
    pool.close()
    pool.join()
