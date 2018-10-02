def find_anagrams(word, candidates):
    anagram = []
    for item in candidates:
        if len(item) == len(word) and item.lower() != word.lower():
            str1 = list(item.lower())
            str1.sort()
            str2 = list(word.lower())
            str2.sort()
            if(str1 == str2):
                anagram.append(item)
    return anagram
            
