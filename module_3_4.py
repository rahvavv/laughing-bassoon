same_word = []

def single_root_words(root_word, *other_words,):
    global same_word
    for i in other_words:
        if root_word.lower() in i.lower():
            same_word.append(i)
        elif i.lower() in root_word.lower():
            same_word.append(i)
    print(same_word)


single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

