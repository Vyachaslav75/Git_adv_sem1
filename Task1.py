from random import randint as ri
import csv
import json
from typing import Callable

def decor1(func: Callable):
    
    def wrapper1():
        with open('data.csv', 'r', newline='', encoding='utf-8') as f:
            data=f.readlines()
            
            #print(data)
        res={}
        for i in data:
            i=i.strip().split(',')
            #print(i[0], i[1], i[2])
            res[str((i[0], i[1], i[2]))]=func(int(i[0]), int(i[1]), int(i[2]))
        return res
    return wrapper1

def decor2(func: Callable):
    
    def wrapper2():
        res=func()
        print(res)
        with open('result.json', 'w', encoding='utf-8') as f:
            json.dump(res, f, indent=4, ensure_ascii=False)
    return wrapper2

@decor2
@decor1
def reshenie_uravnenia(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0:
        return ('Нет решения')
    elif d == 0:
        return -b / (2 * a)
    else:
        return ((-b + d ** (1 / 2)) / (2 * a), (-b - d ** (1 / 2)) / (2 * a))

def generate_numbers():
    res=[]
    for _ in range(ri(100, 1000)):
        a=ri(-1000, 1000)
        if a!=0:
            res.append([a, ri(-1000, 1000), ri(-1000, 1000)])
    with open('data.csv', 'w', newline='', encoding='utf-8') as f:
        csv_writer=csv.writer(f, dialect='excel')
        csv_writer.writerows(res)

# print(reshenie_uravnenia(3, -4, 2))
# print(reshenie_uravnenia(1, -6, 9))
# print(reshenie_uravnenia(1, -4, -5))
generate_numbers()
#reshenie_uravnenia(1, -4, -5)
print(reshenie_uravnenia())
print('Info for first commit')