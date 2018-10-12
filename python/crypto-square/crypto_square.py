import math
def encode(plain_text):
    if plain_text == '':
        return ''
    i_text = ''.join(alpha.lower() for alpha in plain_text if alpha.isalnum())
    sq_rt = math.sqrt(len(i_text))
    r = c = int(round(sq_rt))
    if r*r > len(i_text):
        c += 1      
    else:
        r += 1

    en_text = ''
    for index_1 in range(0, r):
        for index_2 in range(index_1,len(i_text), c):
            en_text += i_text[index_2]
        if index_1 != r-1:
            en_text += ' ' 
    return en_text

