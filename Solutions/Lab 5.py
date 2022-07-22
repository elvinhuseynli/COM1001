x = input().split()
number_of_words = int(x[0])

en_words = []
tr_words = []
en_tr_dict = []
tr_en_dict = []
not_existing_words = []
not_existing_words_list = ''

#           creating dictionaries
while number_of_words != 0:
    z = input().split()
    en_word = ''
    tr_word = ''
    for item in z[::-1]:
        for a in item[0:item.index(':')]:
            en_word += a
        en_words.append(en_word)
    for item1 in z:
        for b in item1[item1.index(':')+1:]:
            tr_word += b
        tr_words.append(tr_word)
    number_of_words -= 1

en_words.reverse()
tr_words.reverse()

#           gathering wanted words together and creating language switch
wanted_words = []
m = input().split()
wanted_lang = m[0]
for c in m[1:]:
    wanted_words.append(c)

#           removing duplicates in wanted words
for d in wanted_words:
    while wanted_words.count(d) > 1:
        wanted_words.remove(d)

#           printing the wanted words in dictionary
for e in wanted_words:
    if e in en_words or e in tr_words:
        if wanted_lang == 'EN':
            tr_en_dict.append(e + '=' + en_words[tr_words.index(e)])
        elif wanted_lang == 'TR':
            en_tr_dict.append(e + '=' + tr_words[en_words.index(e)])
    else:
        not_existing_words.append(e)

#           sorting the dictionary in alphabetical order
tr_en_dict.sort()
en_tr_dict.sort()
not_existing_words.sort()

if bool(tr_en_dict) == True:
    for f in tr_en_dict:
        print(f)

if bool(en_tr_dict) == True:
    for g in en_tr_dict:
        print(g)

if bool(not_existing_words) == True:
    for h in not_existing_words:
        not_existing_words_list += ' ' + h
    print(str(len(not_existing_words)) + ' word not found:' + not_existing_words_list, end='')