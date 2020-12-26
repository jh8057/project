'''
import urllib.request # url 가져오기 위한 모듈
import numpy # size 함수 쓰기 위한 모듈

DOC_URL = 'https://docs.google.com/spreadsheets/d/1-xcUUniY77oZQXubJUnvHAsAItZjYYHEutuGMbU1WSM/edit#gid=641509375&output=csv'    

f = urllib.request.urlopen(DOC_URL)
cont = f.read(SIZE)
f.close()
cont = str(cont, 'utf-8')
print(cont)
'''

import csv
 
file = open('readme.csv', 'r', encoding='utf-8') 
sth = csv.reader(file)
for line in sth:
    print(line)

