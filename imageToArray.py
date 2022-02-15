import sys
import numpy as np 
import matplotlib.pyplot as plt 

data = plt.imread("C:/Users/arthu/Desktop/Amidar/amidar.jpg")
linhas = data.shape[0]
colunas = data.shape[1]
indx=0
x=0

for i in data:
    linha="lln"+str(x).format('999')+": .word "
    x+=1
    for j in i:
        indx+=1
        #print(j[0])
        r = hex(j[0]).replace('0x', '')
        g = hex(j[1]).replace('0x', '')
        b = hex(j[2]).replace('0x', '')
        if (j[0] > 100):
            linha = linha+'0x00'+'90'+'00'+'00'+' '
        else:
            linha = linha = linha+'0x00 '
    print(linha)
