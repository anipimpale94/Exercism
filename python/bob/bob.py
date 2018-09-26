def hey(phrase):
    preproccesed_phrase = phrase.strip()
    if preproccesed_phrase == "":
        return "Fine. Be that way!"
    if preproccesed_phrase.endswith('?'):
        if preproccesed_phrase.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    if phrase.isupper():
        return "Whoa, chill out!"
    return "Whatever."
