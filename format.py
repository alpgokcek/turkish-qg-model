import re

with open("qs-not.txt", 'r') as f:
	raw_content = f.read().strip()
	raw_content = re.split(',\s\[', raw_content)
	raw_content.pop(0) # first element is tensor specifier 
	raw_content[-1] = raw_content[-1][:-2] # last two chars are closing paranthesis

	for line in raw_content:
		formatted_line = ''
		line = line.split('), (')[0][:-1] # last char of every line is ]
		special_case = False
		for token in line.split(', '):
			token = re.sub("'$", '', token)
			token = re.sub("^'", '', token)
			if token == "[SEP]":
				continue
			elif token[0] == "#" or token == "?" or token == "." or special_case:
				formatted_line += token.replace('#', '').replace("'",'') 
				special_case = False
			elif token.find("'") != -1:
				special_case = True
				formatted_line += "\'"
			else:	
				formatted_line += " " + token.replace('#', '').replace("'",'')
		print(formatted_line.strip())	

