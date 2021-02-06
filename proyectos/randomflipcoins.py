import random


def llenalistadeheadandtailcoins(tamano):

    lista = []
    for element in range(tamano):
        numeroaleatorio = random.randint(0, 1)

        if numeroaleatorio == 0:
            lista.append('h')
        else:
            lista.append('t')

    return lista

def averiguaposicionesdeseguidillas(lista):

    tamano = len(lista)
    string = ''
    string = string.join(lista)
    inicio = 0
    posicion = 0
    pos = ''

    while inicio < tamano:
        posicion = string.find('hhhhhh', inicio)

        if posicion != -1:
            pos += str(posicion) + ','
            inicio = posicion + 6
        else:
            break

    return pos


def formatoLista(lista):

    tamano = len(lista)
    lista2 = []
    for i in range(tamano):
        lista2.append(lista[i] + str(i))

    return lista2


def verificamossilistahayseguidillade_6H_6t_(lista,seis):

    string = ''
    string = string.join(lista)
    seis = seis * 6
    contadorh = 0
    encontrado = False
    posicion = ''
    hayaespaciopararecorrer = True
    tamano = len(lista)
    contadorh = string.count('hhhhhh')
    while hayaespaciopararecorrer:

        if seis in string:
            #contadorh += 1
            string = string[string.find(seis)+6:]
            tamanostring = len(string)
            encontrado = True

            if round(abs(tamanostring) / 6) > 0:
                hayaespaciopararecorrer = True
            else:
                hayaespaciopararecorrer = False
        else:
            break

    if encontrado:
        print('encontro {} seguidillas'.format(contadorh))

    return encontrado


#lista = ['t', 'h', 't', 't', 't', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 't', 'h', 'h', 't', 'h','h', \
#         'h', 'h', 'h', 'h','h', 'h', 'h', 'h', 'h','h','h', 'h', 'h', 'h', 'h','h','h', 'h', 'h', 'h', 'h','h','t', \
#         't','h', 'h', 'h', 'h', 'h','h','t','t','t','t','h', 'h', 'h', 'h', 'h','h','t','t']


encontrado = False
vueltas = 0
tamanolista = 40
while not encontrado:
    vueltas += 1
    lista = llenalistadeheadandtailcoins(tamanolista)
    letrah = 'h'

    encontrado = verificamossilistahayseguidillade_6H_6t_(lista, letrah)
    if encontrado:
        print(lista)
        print(formatoLista(lista))
        print(averiguaposicionesdeseguidillas(lista))
        print('se han dado {} vueltas para encontrar la seguidilla'.format(str(vueltas)))




