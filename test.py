import os
from time import sleep
import sys
print(sys.version_info[0])

sleep(10)

x=['1',"232",'4444']
print(x,"","dssad")
print("new matches:"+str(x)[1:-1])

with open('/Users/mercy/Dockerfile') as f:
    lines = [line.rstrip() for line in f]
    print(lines)

lines = tuple(open('/Users/mercy/Dockerfile', 'r'))
print(lines)

with open('/Users/mercy/Dockerfile') as f:
    lines = f.read().splitlines()
    print(lines)


import requests

params = (
    ('async', 'false'),
)

files = {
    'audio': ('audio.mp3', open('audio.mp3', 'rb')),
    'transcript': ('words.txt', open('words.txt', 'rb')),
}

response = requests.post('http://localhost:8765/transcriptions', params=params, file={
    'audio': ('audio.mp3', open('audio.mp3', 'rb')),
    'transcript': ('words.txt', open('words.txt', 'rb')),})

print(response.text)
