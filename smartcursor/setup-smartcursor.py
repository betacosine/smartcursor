# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:07:35 2021

@author: BetaCosine
"""
import time
import pyautogui
import datetime
import numpy as np
from googlesearch import search

#screen shot

sc = pyautogui.screenshot()
sc.save('C:/PythonDev/autocursor/test_image.png')

x,y = pyautogui.locateCenterOnScreen('C:/PythonDev/autocursor/word_icon.png',
                                     confidence=.9)

pyautogui.moveTo(x,y)

sc2 = pyautogui.screenshot()
sc2.save('C:/PythonDev/autocursor/test_image_2.png')

x,y = pyautogui.locateCenterOnScreen('C:/PythonDev/autocursor/add_tab.png',
                                     confidence=.9)
pyautogui.moveTo(x,y)


#googlsearch function

def Gsearch(query):
    results = []
    for i in search(term=query,lang='en',num_results=10):
        results.append(i)
    return results

#type function

def type_emulator(s):
    lst = [i for i in s]
    for l in lst:
        pyautogui.write(l)
        time.sleep(.5)
    pyautogui.press('enter')

'''
testing task steps

1. click on the firefox search icon
2. find the search box and click
3. enter string into search box
4. in background run same search with googlesearch
5. click on the Word icon
6. click on document and enter first string in list from google search

'''

search_query = 'Are gerbils really animals or aliens sent here to probe us'
x,y = pyautogui.locateCenterOnScreen('C:/PythonDev/autocursor/firefox_icon.png',
                                     confidence=.9)
pyautogui.moveTo(x,y)
pyautogui.click()
time.sleep(2)
x,y = pyautogui.locateCenterOnScreen('C:/PythonDev/autocursor/search_box.png',
                                     confidence=.9)
time.sleep(2)
pyautogui.moveTo(x,y)
pyautogui.click()
time.sleep(2)
type_emulator(search_query)
time.sleep(2)
results = Gsearch(search_query)
#pyautogui.press('enter')
x,y = pyautogui.locateCenterOnScreen('C:/PythonDev/autocursor/word_icon.png',
                                     confidence=.9)
pyautogui.moveTo(x,y)
pyautogui.click()
time.sleep(2)
pyautogui.write('My Search Notes')
pyautogui.press('enter')
for r in results:
    domain = r.split('//')[1].split('/')[0]
    type_emulator(domain)
    time.sleep(2)


    
    


