#! /usr/bin/env python
# -*- coding: utf-8 -*-

from re import sub
from urllib import urlopen
from collections import Counter

def makelist(f = open('songs.txt', 'r')):
	a = [line for line in f]
	return Counter(a) - Counter(set(a))

def urltitle(url):
   f = urlopen(url).read()
   s = f.find('<title>')
   e = f.find('</title>')
   return f[s:e][7:-11]

def charfix(string):
	chars = {'&#039;':'\'', '&amp;':'&'}
	for k in chars:
		string = sub(k,chars[k],string)
	return string

titles = [urltitle(track) for track in makelist()]

if len(titles)==0:
	print('No duplicates')
else:
	with open("duplicates.txt", "w") as dup:
		dup.write('Found ' + str(len(titles)) + ' duplicates: \n\n')
		[dup.write(charfix(titles[i])+'\n') for i in range(0, len(titles))]
	print('Done. Check duplicates.txt for duplicates.')