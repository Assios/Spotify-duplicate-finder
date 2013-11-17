#! /usr/bin/env python
# -*- coding: utf-8 -*-

from re import sub
from urllib import urlopen
from collections import Counter
import urllib
import json

def fetch(url):
    json_data = urllib.urlopen(url)
    data = json.load(json_data)
    json_data.close()
    return data

def makelist(f = open('songs.txt', 'r')):
	s = raw_input("Type 1 to match on URL and 0 to match on title: ")
	if s=="1":
		a = [line for line in f]
	elif s=="0":
		a = [fetch("http://ws.spotify.com/lookup/1/.json?uri=" + line)["track"]["name"] for line in f]
	return Counter(a) - Counter(set(a)),len(Counter(set(a))),s

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

if l[2]=="1":
	titles = [urltitle(track) for track in l[0]]
elif l[2]=="0":
	titles = [track for track in l[0]]

if len(titles)==0:
	print('The playlist contains ' + str(l[1]) + ' songs and no duplicates.')
else:
	with open("duplicates.txt", "w") as dup:
		dup.write('Your playlist contains ' + str(l[1]) + ' distinct songs.\nFound ' + str(len(titles)) + ' duplicates: \n\n')
		[dup.write(charfix(titles[i])+'\n') for i in range(0, len(titles))]
	print('Found ' + str(l[1]) + ' distinct songs and ' + str(len(titles)) + ' duplicates. Check duplicates.txt for a list of the dupliates.')