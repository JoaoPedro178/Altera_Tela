import os 

"""remover = ['Sage3D_cos_rj', 'imagens', '~calc~', 'Testes', 'CEPEL', 'Controle']

diretorios = os.listdir('telas')

for x in remover:
    diretorios.remove(x)

for f in os.scandir('telas'):
    for a in os.scandir(f):
        print(a)"""

diretorios = ['BTE', 'CANTE', 'COS', 'CPTE', 'CTE', 'ENTE', 'IMTE']

for d in diretorios:
    for f in os.scandir(f'telas/{d}'):
        with open(f, 'rb') as file:
            print(file.name)
            print(file.read())