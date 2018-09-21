def hey(phrase):
    preProcessedPhrase = phrase.strip()
    if preProcessedPhrase == "":
        return "Fine. Be that way!"
    if preProcessedPhrase.endswith('?'):
        if preProcessedPhrase.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    if phrase.isupper():
        return "Whoa, chill out!"
    return "Whatever."
