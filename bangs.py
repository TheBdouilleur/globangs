#usr/bin/python3.8
import keyboard
import os
import json

bangs = {'!g':'google', '!w':'wikipedia'}

def formatWithBangs(text):
    for bang in bangs:
        text = text.replace(bang, bangs[bang])

    return text

keyboard.add_hotkey('ctrl+space+f', formatWithBangs, args=('!g'))
#while True:
#    selectedText = os.popen('xsel').read()
#
#    if '!' in selectedText and not '! ' in selectedText:
#        newText = formatWithBangs(selectedText)
#        pyautogui.typewrite(newText)
keyboard.wait()