def is_pangram(sentence):
    dict = {}
    for letter in list(sentence.lower()):
        if(ord(letter) > 96 and ord(letter) < 123):
            dict[letter] = True

    i = 97
    while i < 123:
        if(chr(i) in dict ):
            i += 1
        else:
            print(chr(i))
            return False    

    return True