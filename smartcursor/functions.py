# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 15:51:05 2021

@author: BetaCosine
"""
import time
import pyautogui
from googlesearch import search
import os
import click

#googlsearch function

def Gsearch(query):
    results = []
    for i in search(term=query,lang='en',num_results=10):
        results.append(i)
    return results

def type_emulator(s):
    lst = [i for i in s]
    for l in lst:
        pyautogui.write(l)
        time.sleep(.25)
    pyautogui.press('enter')

def cursor_location(image_path):
    x,y = pyautogui.locateCenterOnScreen(image_path, confidence=.9)
    time.sleep(.5)
    pyautogui.moveTo(x,y)

def search_task(search_query,workingDirectory):
    #search_query = 'Are gerbils really animals or aliens sent here to probe us'
    cursor_location(os.path.join(workingDirectory+'/thumbnails/firefox_icon.png'))
    pyautogui.click()
    time.sleep(2)
    cursor_location(os.path.join(workingDirectory+'/thumbnails/add_tab.png'))
    pyautogui.click()
    time.sleep(2)
    cursor_location(os.path.join(workingDirectory+'/thumbnails/search_box.png'))
    pyautogui.click()
    time.sleep(2)
    type_emulator(search_query)
    time.sleep(2)
    results = Gsearch(search_query)
    cursor_location(os.path.join(workingDirectory+'/thumbnails/word_icon.png'))
    pyautogui.click()
    time.sleep(8)
    cursor_location(os.path.join(workingDirectory+'/thumbnails/word_newdoc.png'))
    pyautogui.click()
    time.sleep(2)
    pyautogui.write('My Search Notes')
    pyautogui.press('enter')
    for i,r in enumerate(results):
        domain = r.split('//')[1].split('/')[0]
        type_emulator(str(i)+'. '+domain)
        time.sleep(2)  

def coding_task(code_txt_path,workingDirectory):
    with open(code_txt_path, 'r') as f:
        s = f.read()
    lines = s.splitlines()
    newS = [l.strip() for l in lines]
    newS = '\n'.join(newS)
    newS = newS.split('def ')
    newS = ['def '+string for string in newS if len(string) > 0]
    cursor_location(os.path.join(workingDirectory+'/thumbnails/spyder.png'))
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    cursor_location(os.path.join(workingDirectory+'/thumbnails/spyder_new_icon.png'))
    pyautogui.click()
    time.sleep(2)

    for string in newS:
        type_emulator(string)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('home')
        time.sleep(1)   