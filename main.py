import json
import string
from spellchecker import SpellChecker

f1 = open("attestation_hebergement.txt", encoding='utf-8')
f1_list = f1.readlines()
f1.close()

f2 = open("releve_de_compte.txt", encoding='utf-8')
f2_list = f2.readlines()
f2.close()

tmp = f1_list[0].replace("'", "\"") + f2_list[0].replace("'", "\"")

print(tmp)

res1 = json.loads(tmp)



for dict in res1:
    resultat = ' '.join([i for i in dict['content'].split(' ') if not i.isdigit()])
    dict['content'] = resultat

for dict in res1:
    out = ' '.join([i for i in dict['content'].split(' ') if i not in string.punctuation])
    dict['content'] = out

stop_word = open("stopwords.txt")
stop_word_list = stop_word.read()
stop_word.close()
#print(type(stop_word_list))

for dict in res1:
    out = ' '.join([i for i in dict['content'].split(' ') if i not in stop_word_list])
    dict['content'] = out

spell = SpellChecker()
for dict in res1:
    for mot in dict['content'].split(' '):
        mot_corrige = spell.correction(mot)
        mot = mot_corrige

with open("attestation_hebergement.json", "w", encoding ='utf-8') as outfile:
    outfile.write(str(res1))




