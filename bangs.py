#usr/bin/python3.8

'''1. Core program'''
import os
from pynput import keyboard
import json


with open('settings.json', "r") as file:
    config = json.load(file)

def formatWithBangs(text):
    bangs = config['bangs']
    for bang in bangs:
        text = text.replace(bang, bangs[bang])

    return text


def autoComplete(): #Wrapper function necessary to be properly called back
    #TODO: move the if else to root (ie. os.popen(...)) to increase speed and reduce memory impact
    formattedText = formatWithBangs(os.popen('xsel').read()) 

    if formattedText and '!' in formattedText and not '! ' in formattedText:
        kbd = keyboard.Controller()
        kbd.type(formattedText) 

    else: print("autoComplete() didn't detect bangs in current selection")

'''2. Keyboard shortcut handling'''
COMBINATION = {keyboard.Key.alt, keyboard.Key.space, keyboard.KeyCode.from_char('f')}
current = set()

def on_press(key):
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            print('Keyboard shortcut pressed, running autoComplete()')
            autoComplete()
    

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()