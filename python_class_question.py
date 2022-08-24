import psycopg2, os
from statistics import mean
from bs4 import BeautifulSoup
import collections

def extractTextFromFileTable(file):

    htmlFile = open(file)

    contents = htmlFile.read()

    beautifulSoupText = BeautifulSoup(contents, features="html.parser")

    table_text = beautifulSoupText.find('table').text

    text = {}

    tr = table_text.split()[1:]

    tuesday_index = tr.index('TUESDAY')
    wednesday_index = tr.index('WEDNESDAY')
    thursday_index = tr.index('THURSDAY')
    friday_index = tr.index('FRIDAY')

    for r in tr:
        if r == "MONDAY":
            text['MONDAY'] = dict(collections.Counter([x.strip(',') for x in tr[1:tuesday_index]]))
        elif r == "TUESDAY":
            text['TUESDAY'] = dict(collections.Counter([x.strip(',') for x in tr[tuesday_index+1:wednesday_index]]))
        elif r == "WEDNESDAY":
            text['WEDNESDAY'] = dict(collections.Counter([x.strip(',') for x in tr[wednesday_index+1:thursday_index]]))
        elif r == "THURSDAY":
            text['THURSDAY'] = dict(collections.Counter([x.strip(',') for x in tr[thursday_index+1:friday_index]]))
        elif r == "FRIDAY":
            text['FRIDAY'] = dict(collections.Counter([x.strip(',') for x in tr[friday_index+1:]]))
        else:
            pass

    return text


def getFrequency():

    text = extractTextFromFileTable("python_class_question.html")
    frequency = {}

    for v in text.values():
        for x, y in v.items():
            if x in frequency:
                frequency[x] += y
            else:
                frequency[x] = y

    return frequency


def getMean():

    freq = getFrequency()
    mean_color = f'Mean color value is {round(mean(list(freq.values())), 2)}'

    return mean_color
            

def getMode():

    freq = getFrequency()
    mode_color = f'Mode color of shirt for the week is {max(freq, key=freq.get)}'

    return mode_color


def getMedian():

    freq = getFrequency()
    sorted_k_v = sorted(freq.items(), key=lambda x: x[1])
    middle = float(len(sorted_k_v))/2

    if middle % 2 != 0:
        return f'The median color is {sorted_k_v[int(middle - .5)][0]}' 
    else:
        return f'The median colors are {sorted_k_v[int(middle)][0]} and {sorted_k_v[int(middle-1)][0]}'

def getVariance():

    freq = getFrequency()
    n = len(list(freq.values()))
    x = round(mean(freq.values()), 2)
    deviation = [round(((y - x) ** 2), 2) for y in list(freq.values())]
    
    return f'Variance is {round((sum(deviation)/n), 2)}'


def saveColorFrequencyInPostgresql():

    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='Qaam@100',
        host='localhost',
        port='5432'
    )

    conn.autocommit = True
    cursor = conn.cursor()

    sql = '''CREATE TABLE COLORS(color char(20),\
          frequency int NOT NULL
          );'''

    cursor.execute(sql)

    freq = getFrequency()
    freqList = [(k, v) for k, v in freq.items()]

    for i in freqList:
        sql2='''insert into COLORS(color , frequency) VALUES{};'''.format(i)

        cursor.execute(sql2)

    sql3='''select * from COLORS;'''
    cursor.execute(sql3)

    for i in cursor.fetchall():
        print(i)
 
    conn.commit()
    conn.close()
    
    
print()
print(getFrequency())
print()
print(getMean())
print()
print(getMode())
print()
print(getMedian())
print()
print(getVariance())
print()
saveColorFrequencyInPostgresql()
print()