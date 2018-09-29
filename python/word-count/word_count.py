import string
import re

def word_count(phrase):
    dict = {}
    index = 0
    max_index = len(phrase)
    preprocess_phrase = ""
    while index < max_index:
        if phrase[index] in string.ascii_letters + string.digits + '\'- ':
            if phrase[index] in '\'\"':
                try:
                    if phrase[index+1] in string.ascii_letters + string.digits and phrase[index-1] in string.ascii_letters + string.digits:
                        preprocess_phrase += phrase[index]
                except:
                    index += 1
                    continue
            else:
                preprocess_phrase += phrase[index]
        else:
            preprocess_phrase += " "
        index += 1
    print(preprocess_phrase)

    for item in preprocess_phrase.strip().split():
        item = item.lower()
        if item in dict:
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1
    return dict