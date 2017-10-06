import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def get_words(text):
    return re.findall('\w+', text.lower())

def get_counts(words):
    dct={}
    for i in words:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct 

def get_edits(word):
    lst=[]
    for i in range(len(word)):
        if i != 0:
            lst.append(word[:i-1]+word[i]+word[i-1]+word[i+1:]) #перестановки
        for j in alphabet:
            lst.append(word[:i]+j+word[i+1:]) #замена
        lst.append(word[:i]+word[i+1:]) #удаление 
    for i in range(len(word)+1):
        for j in alphabet:
            lst.append(word[:i]+j+word[i:]) #добавление одной буквы
    return sorted(list((set(lst))))

def get_most_likely(word, dct):
    if word in dct:
        return word, dct[word]
    else:
        word_edits = get_edits(word)
        fr = 0 #frequency
        w = word
        for word in word_edits:
            if word in dct and dct[word] > fr:
                w, fr = word, dct[word]  
        return w, fr


f = open('corpus.txt', 'r')
s = f.readlines()
f.close()
text = ' '.join(s)

words = get_words(text)
dct = get_counts(words)

w = 'conscius'
print(w, '->', get_most_likely(w, dct))

