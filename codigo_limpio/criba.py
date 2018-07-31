from colorama import init, Fore, Back, Style

def generateList(n):
	arr = []
	for y in range(2,n+1):
		arr.append(y)
	return arr

def impares(arr):
	

init()
x = int(input("Escriba el limite superior: "))
arreglo = generateList(x)
arreglo = impares(x)
print(str(x))
print(Back.RED+Fore.WHITE+str(arreglo)+Back.RESET)

