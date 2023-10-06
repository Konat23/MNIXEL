import random

def numeros_aleatorios():
    numeros = []
    while len(numeros) < 10:
        num = random.randint(0, 9)
        if num not in numeros:
            numeros.append(num)
    return numeros


if __name__ == '__main__':
    print(numeros_aleatorios())