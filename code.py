import random as rd 
import time 
import webbrowser
import string


#part of url generator

numbers = ['1','2','3','4','5','6','7','8','9','0', ' ', ' ']
possible_values = ["''", "!", "@", "*", ' ', ' ']

#opens up tabs

tabs_open = 0

while (tabs_open < 40):
    url_gen = f'https://www.bing.com/search?q= {rd.choice(string.ascii_uppercase)}{rd.choice(string.ascii_lowercase)}{(rd.choice(numbers))}{(rd.choice(string.ascii_letters))} {(rd.choice(possible_values))}'
    webbrowser.open(url_gen)
    tabs_open += 1
    time.sleep(1)
