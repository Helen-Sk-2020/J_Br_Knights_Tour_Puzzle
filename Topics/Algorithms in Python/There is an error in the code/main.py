sentence = input()


def aver(sent):

    for sym in ['!', '?', ';', '.', '"', "'"]:
        sent = sent.replace(sym, '')

    words = sent.split()

    length = 0
    
    for word in words:
        length += len(word)     
    return length / len(words)


print(aver(sentence))
