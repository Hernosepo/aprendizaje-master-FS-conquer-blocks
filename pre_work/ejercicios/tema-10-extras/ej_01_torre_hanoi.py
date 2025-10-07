def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f'Mover disco 1 de {origen} a {destino}')
        return 
    else:
        torres_de_hanoi(n-1, origen, auxiliar, destino)
        print(f'Mover disco {n} de {origen} a {destino}')
        torres_de_hanoi(n-1, auxiliar, destino, origen)


torres_de_hanoi(4,"A","B","C")