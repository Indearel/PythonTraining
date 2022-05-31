acronyms = {'LOL': 'laugh out loud',
            'IDK': 'I don`t know',
            'TBH': 'to be honest'}
#acronyms = {}

#acronyms['LOL'] = 'laugh out loud'
#acronyms['IDK'] = 'I don`t know',
#acronyms['TBH'] = 'to be honest'

#acronyms['TBH'] = 'honestly'

#definition = acronyms.get('BTW')

#if definition:
   # print(definition)
#else:
   # print("Key doesn`t exist")

sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') +' what happened '+ acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)
