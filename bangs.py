#usr/bin/python3.8
import os
bangs = {'!g':'google', '!w':'wikipedia'}

def formatWithBangs(text):
#    wordList = list(text)[0].split()
#    text.replace(bangs[text])
#    curatedList = wordList[wordList.index('!')
    print('prepass:', text)
    for bang in bangs:
        print('passing', bang)
        text = text.replace(bang, bangs[bang])

    return text

while True:
    selectedText = os.popen('xsel').read()
    if '!' in selectedText and not '! ' in selectedText:
        print(selectedText)#formatWithBangs(selectedText)
        newText = formatWithBangs(selectedText)
        print(newText)
        break