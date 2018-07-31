
## 10.1 Un objeto con una propiedad: una copa de cafe

Modelamos una simple taza de cafe. guardamos el codigo en un archivo cup.hs, una copa tiene una sola propiedad: el # de onzas de liquido que tiene en un momento dado. tienes que poder guardar este valor y acceder a este despues. En la leccion 5 aprendimos a guardar valores dentro de una funcion: clausuras

Definimos una funcion cup que toma un numero de onzas de fluido en la copa y retornamos un closure almcenado este valor:
```hs
cup f10z = \_ -> f10z
```
asi puedes pasar este valor a una clausura y almacenarlo como un dato. Ahora es posible pasar la informacion almacenada como un objeto. Sin embargo lo que queremos es tener la capacidad de aplicar un mensaje para el valor interno de la copa. Usaremos una funcion de primera clase para pasar un mensaje a tu objeto. Este mensaje puede actuar sobre la propiedad interna del objeto. Usaremos un patron un poco diferente para enviar mensajes al objeto en lugar de un enfoque comun de llamada de metodos.

```hs
car.start() -- llamada a metodo enfocado en POO

start car -- paso de mensaje enfocado a POO (normalmente usado en programacion funcional)
```
## 10.1.1 Creando un constructor
La forma mas comun de crear una instancia de una objeto es usando un metodo especial llamado constructor. La unica cosa necesaria para crear un constructor para tu objeto es permitir una forma de enviar mensajes a tu objeto. Para adicionar un argumento nombrado a tu clausura, puedes adicionar una forma de mandar mensajes.
```hs
cup f10z = \message -> message f10z
```

Con este constructor ahora es posible hacer instancias de tus objetos.  Podemos hacer esto gracias a los lambdas, una clausura y funciones de primera clase
```hs
aCup = cup 6
coffeeCup = cup 12 -- copa de cafe
```
## 10.1.2 Adicionando accesores a tu objeto
ahora necesitamos algo util para este objeto. Crear mensajes simples par conseguir obtener y asignar valores dentro de tu objeto. Primero seremos capaces de conseguir el volumen de cafe en la taza. Crearemos un mensaje get0z que toma una objeto copa y retorna el numero de onzas de fluido que tiene.
```hs
getOz aCup = aCup (\f10z -> f10z)
getOz coffeeCup 
12
```
A continuacion haremos algo mas complicado. Lo mas util que hay que hacer con una copa es beberla. Beber una copa inherentemente cambia el estado del objeto. Haremos esto creando un nuevo objeto detras de camara. Tu mensaje configurara un valor para las onzas de fluido necesarias para retornar una nueva instancia de tu objeto con una propieda interna modificada apropiadamente.
```hs
drink aCup ozDrank = cup (f10z - ozDrank)
	where f10z = getOz aCup
```
Este codigo tiene un pequeno error puedes beber mas cafe del que realmente hay en la copa. Podemos reescribir la funcion:
```hs
drink aCup ozDrank = if ozDiff >= 0
					 then cup ozDiff
					 else cup 0
	where f10z = getOz aCup
	      ozDiff = f10z - ozDrank

isEmpty aCup = getOz aCup == 0
```
Con esta mejora no beberemos cafe de mas. ademas adicionamos una funcion para ver si la copa esta vacia
Necesitamos guardar un rastro constante del estado del objeto, ya que tomamos muchos tragos de la copa podria hacer el codigo mas verboso. Afortunadamente podemos usar la funcion foldl
```hs
afterManySips = foldl drink coffeeCup [1,1,1,1,1]
```
Eso funciona sin necesidad de muchos problemas

## 10.2 Un objeto mas complejo: construimos una pelea de robots
Al modelar un objeto. Seremos capaces de capturar informacion sobre un objeto mediante el uso de un constructor. Interactuamos con el objeto usando accesores. Ahora construiremos algo mas complicado.

Un robot tiene propiedades basicas:
- un nombre
- una fuerza de ataque
- un numero de puntos de golpe 

Se necesita algo mas sofisticado para manejar estos atributos. podemos pasar 3 valores a la clausura, pero esto hara el trabajo mas confuso. En su lugar usamos tuplas de de valores que representan los atributos de tu robot.Ej. ("bob", 10, 100) es un robot llamado bob con ataque 10 y 100 puntos de vida.

En lugar de enviar un mensaje para esta coleccion de atributos. Usamos un patron de muestreo para nuestra tupla de argumentos para hacer los valores mas faciles de leer.
```hs
robot (name, attack, hp) = \message -> message (name, attack, hp)
```
Todos los objetos pueden ser vistas como una coleccion de atributos que puede enviar mensajes a. En la siguiente unidad, veremos el sistema de tipos de haskell; que permite un metodo mas poderoso de abstraer nuestros datos. Incluso entonces, la idea de la tupla sirve como una estructura de datos minima viable para almacenar datos.

Una instancia se puede construir como:
```hs
killerRobot = robot ("kill3r", 25, 100)
```

Ahora es necesario adicionar unos pocos accesores para poder trabajar con estos datos mas facilmente. Comenzamos con funciones que hagan mas facil acceder a varias partes de tu tupla por nombre.
```hs
name (n,_,_) = n
attack (_,a,_) = a
hp (_, _,hp) = hp
```
Con estas funciones podemos implementar los getters
```hs
getName aRobot = aRobot name
getAttack aRobot = aRobot attack
getHP aRobot = aRobot hp
```
Tambien es necesario algunos setters para las propieades. Cada uno de estos casos retornara una nueva instancia de nuestro robot.
```hs
setName aRobot newName = aRobot (\(n,a,h) -> robot (newName,a, h))
setAttack aRobot newAttack = aRobot (\(n,a,h) -> robot (n,newAttack,h))
setHP aRobot newHP = aRobot (\(n,a,h) -> robot (n,a,newHP))
```
Podemos emular el comportamiento de la POO basada en prototipado, porque nunca cambia el estado.

**POO basado en prototipos**: Lenguajes orientados a objetos basados en prototipos, tal como javascript, creamos instancias de objetos para modificar un objeto prototipo, en lugar de usar clases.  Prototipado en javascript es fuente de confusion.

Otra funcion bastante bonita imprime el estado de todos los robots. Definimos el mensaje printRobot que trabaja como un toString de java.
```hs
printRobot aRobot = aRobot (\(n,a,h) -> n ++ " attack:" ++ (show a) ++ " hp:" ++ (show h))
``` 
## 10.2.1 Enviando mensajes entre objetos
La parte mas interesante de la pelea de robots es la pelea!. Necesitamos enviar un mensaje de dano a un robot. Esto trabaja como el mensaje de beber en el ejmplo de la copa. En este caso necesitamos obtener todos los atributos en lugar de solo uno.
```hs
damage aRobot attackDamage = aRobot (\(n,a,h) -> robot (n,a,h-attackDamage))

afterHit = damage killerRobot 90
> getHP afterHit
110
```
Con el mensaje damage, puedes decirle a un robot que reciba dano.
Necesitamos hacer algo de POO ahora. El mensaje de pelea debe ser algo equivalente a robotOne.fight(robotTwo)
El mensaje fight aplica dano del atacante a la defensa; adicionalmente, debes prevenir que un robot sin vida sea atacado
```hs
fight aRobot defender = damage defender attack
	where attack = if getHP aRobot > 10
				   then getAttack aRobot
				   else 0
```
## 10.3 Porque la programacion sin estado es importante.
Hasta ahora hemos sido capaces de crear una aproximacion rasonable de un sistema POO. Aunque esta solucion trabaja no hace mas facil tener objetos que sean mutables?  Ocultar el estado hace a este codigo limpio, pero mas grandes problemas pueden facilmente surgir con un estado oscuro. 

Dado que no tienes estados en la programacion funcional, tienes completo control sobre la forma de calcular que pasa. comparado con la POO con estado. 

En caso que el codigo fuera ejecutado secuencialmente, no hay problema. Pero suponga que usamos asincrono, concurrente o codigo paralelo. No tienes control sobre como estas operaciones son ejecutadas. Mas aun, controlar la prioridad de las peleas es mas dificil, si quieres asegurar que fastRobot siempre de el primer golpe.

	LEER CON MAS CALMA

## 10.4 Tipos - objetos y mucho mas
Haskell no es un lenguaje orientado a objetos. Toda la funcionalidad construida desde cero puede ser realizada de una forma mas poderosa. Usando el sistema de tipos de haskell. Muchas de estas ideas usadas en esta seccion seran vistas de nuevo, pero crearemos tipos. Tipos en haskell pueden replicar todos los comportamientos modelados aqui, pero con los beneficios adicionales que el compilador de haskell puede razonar mucho mas profundamente sobre los tipos que con estos objetos ad hoc. Las ventajas de la programacion funcional son tremendamente magnificadas cuando combinamos con sistema de tipos de haskell.

















