from ast import Or
from os import O_RDWR


acronyms = ['TBH', 'AFK', 'SMH']

acronyms.append('LOL')
acronyms.append('IDK')

acronyms.remove('SMH')

if 'AFK' in acronyms:
    print('True') 

word = 'IMO'
new_acronym = input(word + ' is not in the list, but you can add it here:\n')
updated_list = acronyms.append(str(new_acronym))
if word in acronyms:
    print(word + 'is in the list')
else:
    print(new_acronym)

for acronym in acronyms:
    print(acronym)