import sys
import numpy as np 
import matplotlib.pyplot as plt 

data = plt.imread("C:/Users/arthu/Desktop/Amidar/amidar.jpg")
linhas = data.shape[0]
colunas = data.shape[1]
indx=0
x=0
reds = 0

for i in data:
    linha="ln"+str(x).format('999')+": .word "
    x+=1
    indx=0
    for j in i:
        indx+=1
        r = hex(j[0]).replace('0x', '')
        g = hex(j[1]).replace('0x', '')
        b = hex(j[2]).replace('0x', '')
        #linha = linha = linha+'0x00'+r+g+b+' '
        if (j[0] > 100):
            if j[1] > 100:
                linha = linha+'0x00'+'ff'+'ff'+'ff'+' '
            else:
                if indx < 107:
                    linha = linha+'0x00900000 '
                    reds += 1
                else:
                    linha = linha+'0x00950000 '
        else:
            linha = linha = linha+'0x00 '
        #print(indx)
    #print(linha)

print(reds)
