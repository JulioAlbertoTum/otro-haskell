### 7.1 Recursion
Algo es recursivo si se define en terminos de si mismo. Esto suele traer dolores de cabeza, como bucles infinitos. Las listas son una estructura de datos recursiva definida como una lista vacia o un elemento y otra lista. Funciones recursivas son solo funciones que se usan a si mismas en su propia definicion.

### 7.2 Reglas para la recursion
El problema con la recursion viene con la escritura de procesos recursivos. El secreto de escribir funciones recursivas es no pensar en la recursion!. Para resolver estos problemas son necesarias un conjunto de simples reglas
- Identifica la meta final
- Determina que pasa cuando una meta es alcanzada.
- Lista todas las alternativas posibles.
- Determina tu proceso de "enjaugue y repite"
- Asegurar que cada alternativa se mueva en la direccion de la meta.

### 7.2.1 Regla 1: Identifica la meta final
Generalmente los procesos recursivos tiene un final.Que hace que un meta sea una? Paraua lista el final de proceso es la lista vacia; para una lavadora es, un tanque vacio. Despues de reconocer que algo es un proceso recursivo.
### 7.2.2 Regla 2: Determinar que pasa cuando una meta es alcanzada
Para cada meta establecida en la regla 1, es necesario saber cual sera el resultado. En le caso de la lavaplatos, el resultado es que se ha terminado de lavar los platos.Con las funciones necesitas  retornar el valor, asi que tenemos que determinar que valor debe ser retornado al final de estado. 
### 7.2.3 Regla 3: Lista todas las posibilidades alternar
Si no tienes un estado meta, que tienes entonces? Esto suena a mucho trabajo, pero la mayoria de las veces tienes una o dos alternativas para ser el estado meta.
### 7.2.4 Regla 4: Determine tu "enjauga y repite"
Esta regla es similar a la regla 2, excepto que tienes que repetir tu proceso. No hay que sobrepensar tratando de relajar la recursion. Para una lista debes tomar una elemento y devolver la cola. 
### 7.2.5 Regla 5: Asegurar que cada alternativa se mueeve hacia la meta.
Esta es importante! Para todo proceso que se lista en la regla 4, es necesario preguntarte a ti mismo **Esto se aproxima hacia su meta?** Si tomas la cola de una lista, al final tendra la lista vacia. Recuerda que las llamadas eventualmente causan que el conteo para cada una alcance la meta. 

### 7.3 Tu primera funcion recursiva: Maximo comun Divisor
Comenzaremos con una viejo algoritmo numerico: el algoritmo de euclides. Este es un metodo simple para calcular el maximo comun divisor (MCD) de 2 numeros. Por ejemplo el MCD de 20 y 16 es 4 por que 4 es el numero mas grande que puede dividir a 20  y 16 
Los pasos basicos son:
- 1 Comenzamos con 2 numeros, a y b
- 2 Si divides a por b y el resto es 0 claramente b es el MCD.
- 3 En otro caso cambiamos el valor de **a** para asignarle este valor a **b**  (b sera el nuevo a) Puedes cambiar el valor de b para ser el resto que obtienes en el paso 2  (de nuevo b es el resto del a original dividido enter el b original)
- Entences repetimos hasta que a/b no tenga resto.
**Ejemplo**
- 1 a = 20, b = 16
- 2 a/b = 20/16 = 1 resto 4
- 3 a = 16, b = 4
- 4 a/b = 4 resto 0
- 5 MCD = b = 4
Para implementar este algoritmo, quieres comenzar con una condicion meta. La meta es no tener un resto para a/b. Usamos la funcion modulo para expresar esta idea : a `mod` b == 0
La siguiente cuestion es responder que retorna cuando se alcanza el estado meta. Si a/b no tiene resto b divide al anterior; entonces b es el MCD. Esto nos da un comportamiento global completo
**if a `mod` b == 0**
**then b ...**
A continuacion necesitamos figurar la forma en como moverse para acercarses a la meta. Para este problema, hay solo una alternativa: si el resto no es cero repetimos el algoritmo tomando b como nuevo a y el nuevo b sera el resto de: a `mod` b
**else mcd b (a `mod` b)**
De esta forma podemos implementar esta codigo
```hs
myMCD a b = if remainder == 0
			then b
			else myMCD b remainder
	where remainder = a `mod` b
```
Finalmente, nos aseguramos que nos estamo moviendo hacia la meta(regla 5). Usando el resto siempre seremos guiados hacia un nuevo b; en el peor caso (ambos numeros son primos) , eventualmente tendremos 1 en a y b. Esto confirma que tu algoritmo puede terminar. 

En la funcion myMCD, solo 2 cosas posibles pueden pasar: se consigue la meta, o el proceso se repite. En funciones mas complejas tendras sentencias mas largas de if then o si estas usando case. Haskell tiene una caracteristica maravillosa que es muestreo de patrones (pattern matching) que te permite "ojear" los valores pasados como argumentos y comportarse de acuerdo a este. 
```hs
sayAmount n  = case n of
1 -> "uno"
2 -> "dos"
n -> "un manojo"
```
Una version usando patronesde diseno luce asi:
```hs
sayAmount 1 = "uno"
sayAmount 2 = "dos"
sayAmount n = "un rollo"
```
Lo importante para realizar pattern matching es que puede manejar solo un argumento, pero este no puede ser computado de ninguna forma cuando se esta muestreando.
```hs
isEmpty [] = True
isEmpty _ = False
```
Usamos un wildcard para valores que no vayamos a usar. Podemos incluso usar patrones mas sofisticados en listas. Por convencion se usa x para representar un solo valor, y la variable xs para representar una lista de valores 
```hs
myHead (x:xs) = x
myHead [] = error "No head for empty list"
```
Aqui pensamos en la recursion como una mera lista de metas y casos alternativos, muestro de patrones llega a ser valioso para escribir codigo recursivo sin tener una migrana. El truco es pensar en patrones. 
