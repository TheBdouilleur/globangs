#usr/bin/python3.8

'''1. Core program'''
import json
import os
from pynput import keyboard

with open('settings.json', "r") as file:
    config = json.load(file)

def formatWithBangs(text):
    """Returns expanded version of `text`
    """
    for bang in config['bangs']:
        text = text.replace(bang, config['bangs'][bang])


    return text

def autoComplete(characterList):
    """
    Wrapper around formatWithBangs that
    1. Simulates a series of backspace presses to delete user-typed bangword
    2. Generates a str from `characterList` (bangWord)
    3. Types expanded version of `bangWord`
    """
    kbd = keyboard.Controller()
    for char in range(0,len(characterList)+1): # Erase the bangword before typing the corresponding str
        kbd.press(keyboard.Key.backspace)
        kbd.release(keyboard.Key.backspace)

    bangWord = ''.join(characterList)
    kbd.type(formatWithBangs(bangWord)) #Type replacement

'''2. Keyboard shortcut handling'''
currentCharList = [] #

def on_press(key):
    global currentCharList
    print(f'{key}')
    print(key)

    #FIXME: Currently every keys pressed after ! are included in currentList 
    if (key == keyboard.KeyCode.from_char('!')) or (currentCharList and not key == keyboard.Key.space): # Check if: key is !, key follows !, key isn't a space
        currentCharList.append(str(key).strip("'")) # Without this, key looks like this '"key"'

    elif key == keyboard.Key.space and currentCharList:
        print('Bang shortcut detected, formatting')
        placeHolderList = currentCharList
        currentCharList = []
        autoComplete(placeHolderList)


    else:
        print(key, ' not equal to "!"')
if __name__ == '__main__':
    with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

