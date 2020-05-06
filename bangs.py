#usr/bin/python3.8

'''1. Core program'''
import os
from pynput import keyboard

bangs = {'!g':'google', '!w':'wikipedia'}

def formatWithBangs(text):
    for bang in bangs:
        text = text.replace(bang, bangs[bang])

    return text

def getSelection():
    selectedText = os.popen('xsel').read()  

    if selectedText and '!' in selectedText and not '! ' in selectedText:
        return selectedText

def autoComplete(): #Wrapper function necessary to be properly called back by add_hotkey()
    formattedText = formatWithBangs(getSelection()) 
    kbd = keyboard.Controller()
    kbd.type(formattedText) 


'''2. Keyboard shortcut handling'''
COMBINATION = {keyboard.Key.alt, keyboard.Key.space, keyboard.KeyCode.from_char('f')}
current = set()

def on_press(key):
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            print('All modifiers active!')
            autoComplete()
    if key == keyboard.Key.esc:
        listener.stop()

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()