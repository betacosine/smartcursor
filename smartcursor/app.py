# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:57:30 2021

@author: BetaCosine
"""
import click
import time
import os
import sys
from functions import search_task, coding_task     

@click.command()
def main():
    print(workingDirectory)
    tasks = input('Would you like the bot to perform a search, coding, or both tasks?\n')
    search_query = input('Please provide the search query for the task:\n')
    if tasks in ['coding','both']:
        code = input('Please provide the path to your coding text file\n')
    print('Your bot will start in...')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    if tasks in ['search','both']:
        search_task(search_query,workingDirectory)
    if tasks in ['coding','both']:
        coding_task(code,workingDirectory)
    print('Your bot has completed its tasks')

if __name__ == "__main__":
    workingDirectory  = os.getcwd()
    main()
    