import numpy as np
import os
import logging


def main():
    
    diretorios = ['BTE', 'CANTE', 'CPTE', 'COS', 'CTE', 'ENTE']
    conteudo = np.array([x for x in open(path, 'rb')])

path = 'telas/'

id_alvo = 'LTICH_UAC1TIE2_KV_BI '
conteudo = np.array([x for x in open(path, 'rb')])

#with open(conteudo, 'rb') as lines:
#    source = np.array([line for line in lines])


teste = np.array([x for x in conteudo if (str(x).find(id_alvo)) != -1])

variavel = str(teste).replace(id_alvo, 'Testando ')

print(str(conteudo).replace(id_alvo, ))

#print(variavel)

#print(str(teste).find(id_alvo))

#print(len(id_alvo))

#print(str(conteudo).replace('UNIFILAR', 'Testando'))

#print(str(conteudo[110]).find(id_alvo))