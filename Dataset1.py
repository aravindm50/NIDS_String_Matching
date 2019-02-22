import rstr
from rstr import Rstr,xeger
from random import SystemRandom
import csv
import numpy as np
from xeger import Xeger
import string
import random
import pandas as pd 

firstloop =0
num_pat = 50
while (firstloop != 1):
    rs = [rstr.rstr(string.ascii_uppercase, 5,5) for j in range(num_pat)]
    with open('fixed_random_file.csv', mode='w') as random1:
        rwrite = csv.writer(random1, delimiter=',')
        rwrite.writerow(rs)
    firstloop = 1   

## Generating string of datas with patterns inserted at random length

first_500 = rstr.rstr(string.ascii_uppercase, 500,500)
a =[]
with open('fixed_random_file.csv', newline='\n') as csvfile:
    data = list(csv.reader(csvfile))
n = 50000
with open ('dataset1.csv', mode = 'w') as dataset:
    for z in range(100):
        str_50 = [random.choice(string.ascii_uppercase)]
        while (len(str_50[0]) < n):
            str_50[0] = str_50[0] + first_500[0:random.randrange(500)] + data[0][random.randrange(num_pat)]
        if (len(str_50[0]) > n):
            str_50[0] = str_50[0][:(n-len(str_50[0]))]
        wrt = csv.writer(dataset,delimiter = ',')
        wrt.writerow(str_50)
        
        
firstloop =0
num_pat = 50
while (firstloop != 1):
    rs = [rstr.rstr(string.ascii_uppercase, 5,5) for j in range(num_pat)]
    with open('fixed_random_file.csv', mode='w') as random1:
        rwrite = csv.writer(random1, delimiter=',')
        rwrite.writerow(rs)
    firstloop = 1 