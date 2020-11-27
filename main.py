def factorial(n):
    res = 1
    for i in range(n):
        res *= i+1
    return res

fact = factorial(3)


def sumatorio(lista,longitud):
    if longitud > 1:
        return lista[longitud-1] + sumatorio(lista,longitud-1)
    else:
        return lista[longitud-1]

listNum = [1,1,1,1]
suma = sumatorio(listNum, len(listNum))

def multiplica(a,b):
    return a*b

def potenciaOper(potencia,exponente):
    if exponente > 1:
        return multiplica(potencia,potenciaOper(potencia, exponente-1))
    else:
        return potencia

res = potenciaOper(2,3)

print('FIN')