import json
import string
from spellchecker import SpellChecker

f1 = open("attestation_hebergement.txt", encoding='utf-8')
f1_list = f1.readlines()
f1.close()

f2 = open("releve_de_compte.txt", encoding='utf-8')
f2_list = f2.readlines()
f2.close()

f3 = open("avis_taxe_fonciere.txt", encoding='utf-8')
f3_list = f3.readlines()
f3.close()

f4 = open("bulletin_de_paie.txt", encoding='utf-8')
f4_list = f4.readlines()
f4.close()

f5 = open("impot.txt", encoding='utf-8')
f5_list = f5.readlines()
f5.close()

L1 = f1_list[0].replace("'", "\"")
L2 = f2_list[0].replace("'", "\"")
L3 = f3_list[0].replace("'", "\"")
L4 = f4_list[0].replace("'", "\"")
L5 = f5_list[0].replace("'", "\"")

list1 = list(L1)
list1.pop(0)
list1.pop(-1)
L1 = "".join(list1)

list2 = list(L2)
list2.pop(0)
list2.pop(-1)
L2 = "".join(list2)

list3 = list(L3)
list3.pop(0)
list3.pop(-1)
L3 = "".join(list3)

list4 = list(L4)
list4.pop(0)
list4.pop(-1)
L4 = "".join(list4)

list5 = list(L5)
list5.pop(0)
list5.pop(-1)
L5 = "".join(list5)

tmp = "[" + L1 + "," + L2 + "," + L3 + "," + L4 + "," + L5 + "]"

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

for dict in res1:
    out = ' '.join([i for i in dict['content'].split(' ') if i not in stop_word_list])
    dict['content'] = out

spell = SpellChecker()
for dict in res1:
    for mot in dict['content'].split(' '):
        mot_corrige = spell.correction(mot)
        mot = mot_corrige

with open("final.json", "w", encoding='utf-8') as outfile:
    outfile.write(str(res1))



