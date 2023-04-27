import nltk
import re

input_program = input("Enter your code: ")
input_program_tokens = nltk.wordpunct_tokenize(input_program)
print(input_program_tokens)

RE_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include"
RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
RE_Numerals = "^(\d+)$"
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_Headers = "([a-zA-Z]+\.[h])"

for token in input_program_tokens:
    if (re.findall(RE_Keywords, token)):
        print(token, "-------->keywords")
    elif (re.findall(RE_Operators, token)):
        print(token, "-------->operators")
    elif (re.findall(RE_Numerals, token)):
        print(token, "-------->numerals")
    elif (re.findall(RE_Identifiers, token)):
        print(token, "-------->identifiers")
    elif (re.findall(RE_Headers, token)):
        print(token, "-------->header")
    elif (re.findall(RE_Special_Characters, token)):
        print(token, "-------->Special_Characters")
    else:
        print("unknown value")
