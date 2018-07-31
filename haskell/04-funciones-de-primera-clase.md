# Funciones de primera clase

## 4.1 Funciones como argumentos
Las funciones no son diferentes a otros tipos de datos usados en un programa. Las funciones puede ser usadas como argumentos y retornadas como valores de otras funciones. Esto permite abstraer cualquier computacion repetitiva. y permitir escribir funciones que escriben otras funciones.
```hs
ifEvenInc n = if even n
			  then n + 1
			  else n
```
despues puedes necesitar otras 2 funciones que se doblan o elevan al cuadrado un numero su es par.
```hs
ifEvenDouble n = if even n
				 then n * 2
				 else n

ifEvenSquare n = if even n
				 then  n^2
				 else n
```
Estas funciones son parecidas, de forma que hay un patron de computacion que se puede abstraer
```hs
ifEven myFunction x = if even x
					  then myFunction x
					  else x

--tambien podemos abstraer las funciones
inc n = n + 1
double n = n * 2
square n = n^2

ifEvenInc n = ifEven inc n
ifEvenDouble n = ifEven double n
ifEvenSquare n = ifEven square n
```
De esta forma es posible implementar otras funciones parecidas como ifEvenCube.
Como recordatorio  tenemos que las funciones tienen nivel de precedencia mas alto que las operaciones comunes como + - * / % ^ 

### Funciones Lambda como argumentos
Nombrar funciones es generalmente una buena idea, pero tambien es posible usar funciones lambda para pasar codigo a una funcion.
```hs
ifEven (\x -> x*2) 6
```

### Ejemplo personalizado ordenacion
Si tenemos una lista de nombres y apellidos, cada nombre esta representado como una tupla.
Las tuplas son similares a las listas pero pueden ser de multiples tipos:
```hs
author = ("Juan", "Perez")
```
Para obtener los items de un tupla hay funciones fst y snd, que accecen al primer y segundo elemento respectivamente.
Si tienes una lista de nombres que deseas ordenar: names = [(firstname1,secondname1),(firstname2,secondname2),.....]
Haskell posee una funcion que nos permite ordenar **sort o sortBy** en este caso podemos hacer el ordenamiento basado en el apellido, para esto escribimos el siguiente codigo:
```hs
import Data.List

compareLastNames name1 name2 = if lastName1 > lastName2
							   then GT
							   else if lastName1 < lastName2
							   		then LT
							   		else EQ
	where lastName1 = snd name1
	      lastName2 = snd name2

-- podemos ejecutar el codigo como:
> sortBy compareLastNames names
```
### 4.2 Retornando funciones
Hemos hablado de pasar funciones como argumentos, pero  esto es solo la mitad de lo que significa pasar funciones de primera clase como valores. El retorno tambien puede ser una funcion. Pero porque yo quisiera retornar una funcion. Una buena razon es querer despachar ciertas funciones basadas en otros parametros.

Vea la siguiente funcion para enviar cartar a miembros de varias oficinas regionales. Es necesaria una funcion que tome un nombre tupla y una localizacion de oficina y poner junto la direccion de correo.
```hs
addressLetter name location = name ++ " - " ++ location
	where nameText = (fst name) ++ " " ++ (snd name)
```
Necesitamos una funcion diferente para cada oficina
```hs
sfOffice name = if lastName < "L"
				then nameText ++ " - PO Box 1234 - San Francisco, CA, 94111"
				else nameText ++ " - PO Box 1010 - San Francisco, CA, 94109"
	where lastName = snd name
	      nameText = (fst name) ++ " " ++ lastName

nyOffice name = nameText ++ ": PO Box 789 - New York, NY, 10013"
	where nameText = (fst name) ++ " " ++ (snd name)

renoOffice name = nameText ++ " - PO Box 456 - Reno, NV 89523"
	where nameText = snd name
```

Como podriamos usar estas funciones con addressLetter, Podriamos reescribir addressLetter para que tome una funcion en lugar de una localizacion como argumento. el problema es que addressLetter va a ser parte de una gran aplicacion web. y nos gustaria pasar un string para la localizacion. podemos construir otra funcion llamada getLocationFunction que tome un solo string y envie la funcion correcta.
```hs
getLocationFunction location = case location of
	"ny" -> nyOffice
	"sf" -> sfOffice
	"reno" -> renoOffice
	_ -> (\name -> (fst name) ++ " " ++ (snd name))
```
esta funcion es facil de entender excepto por _ al final. _ captura cualquier situacion que no encaje con las 3 primeras se le denomina wildcard. Ahora podemos reescribir addressLetter
```hs
addressLetter name location = locationFunction name
	where locationFunction = getLocationFunction location
```
En este ejemplo hemos visto como retornar funciones como valroes ayuda a hacer mas facil de entender y extender el codigo. 










