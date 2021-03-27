from pprint import pprint
from fuzzywuzzy import fuzz
from PersonDataParser import Parser
from QuestionPatterns import QuestionPatterns
from CommonPatterns import CommonPatterns
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
OUTPUT_PATH = "out/data.txt" if not args.output else args.output
CONFIG_FILE = json.load(open('config.json', 'r'))

OCCUPATION_SETTINGS = CONFIG_FILE["occupation_settings"]


THRESHOLD = 60
parser = Parser(ATTRIBUTES_PATH)
parser.parse()

counter = 0
occupational_patterns = QuestionPatterns.patterns
common_patterns = CommonPatterns.patterns


out = open("out/data.txt", 'w')
full_wiki = open(WIKI_PATH).read()
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

def format_question(p, question_pattern):
	try:
		if _suffix1 in question_pattern:
			question_pattern = question_pattern.format(
				name=p.name, _suffix1=get_suffix(p.name, _suffix1))
		elif _suffix2 in question_pattern:
			question_pattern = question_pattern.format(
				name=p.name, _suffix2=get_suffix(p.name, _suffix2))
		elif _suffix3 in question_pattern:
			question_pattern = question_pattern.format(
				name=p.name, _suffix3=get_suffix(p.name, _suffix3))
		else:
			question_pattern = question_pattern.format(name=p.name)
		return question_pattern
	except Exception as e:
		print("Error on: {} - {} \n{}\n".format(e, p.name, question_pattern))

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
				q = format_question(p, pattern)
				if q:
					qa_pair['questions'].append(q)
			pair_list.append(qa_pair)
	return pair_list
			

def process(enum):
	index, p = enum
	# print("Idx,", index, "P", p)
	person_dict = dict()
	description_tag = soup.find("div", {"id": int(p.doc_id)}) # large description text
	if description_tag:
		description = description_tag.get_text().replace('\n', '')
		del description_tag
		person_dict['description'] = "description"
		person_dict['data'] = list()
		common_questions = create_common_questions(p)
		person_dict['data'].append(common_questions)
		feature_patterns = occupational_patterns[p.occupation]
		# pattern type = rutbesi, pozisyon, etc.
		for pattern_type in feature_patterns.keys():
			if pattern_type in p.attributes.keys():
				answer = p.attributes[pattern_type]
				qa_pair = {'answer': answer, 'questions': list()}
				for question_pattern in feature_patterns[pattern_type]:
					ratio = int(fuzz.partial_token_set_ratio(description, answer)) # does the description paragraph contain answer?
					if ratio > THRESHOLD:
						qa_pair['ratio'] = ratio
						q = format_question(p, question_pattern)
						if q:
					   		qa_pair['questions'].append(q)
				if len(qa_pair['questions']) > 0: # if any relevant qa pair is present
					person_dict['data'].append(qa_pair)
				else:
					del qa_pair
		if len(person_dict['data']) > 0:
			out.write(json.dumps(person_dict, ensure_ascii=False)+ ", \n\n")
		del person_dict


if __name__ == '__main__':
	pool = Pool(os.cpu_count())  # Create a multiprocessing Pool
	#pool.map(create_common_questions, enumerate(persons))
	pool.map(process, enumerate(persons))
	pool.close()
	pool.join()
