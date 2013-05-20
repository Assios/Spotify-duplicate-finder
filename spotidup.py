#! /usr/bin/env python
# -*- coding: utf-8 -*-

from re import sub
from urllib import urlopen
from collections import Counter

def makelist(f = open('songs.txt', 'r')):
	a = [line for line in f]
	return Counter(a) - Counter(set(a)),len(Counter(set(a)))

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

l=makelist()

titles = [urltitle(track) for track in l[0]]

if len(titles)==0:
	print('The playlist contains ' + str(l[1]) + ' songs and no duplicates.')
else:
	with open("duplicates.txt", "w") as dup:
		dup.write('Your playlist contains ' + str(l[1]) + ' distinct songs.\nFound ' + str(len(titles)) + ' duplicates: \n\n')
		[dup.write(charfix(titles[i])+'\n') for i in range(0, len(titles))]
	print('Found ' + str(l[1]) + ' distinct songs and ' + str(len(titles)) + ' duplicates. Check duplicates.txt for a list of the dupliates.')