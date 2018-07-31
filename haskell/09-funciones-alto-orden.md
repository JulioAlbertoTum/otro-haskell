# Funciones de Alto Orden

## 9.1 Usando map
Es dificil decir cuan importante es map en la programacion funcional. La funcion map toma otra funcion y ua lista como argumentos y aplica esta funcion a cada elemento en la lista.

Un programador podra darse cuenta que map es una version mas limpia para el bucle for. Las ventajas de map son claras. Sabes exactamente lo que pasa cuando y que estas pasando. La legibilidad del codigo es una mejora porque map es un tipo de iteracion.

## Abstrayendo recursion con map

La primera razon es que usamos funciones de primera clase, y mas aun tenemos funciones de alto orden, que puedes abstraer en patrones de programacion. De esta forma podemos pasar varias funciones a otra usando la funcion map.
```hs
-- adiciona "a " a cada miembro de la funcion
addAna [] = []
addAna (x:xs) = ("a " ++ x):addAna xs

--version con map
addAna xs = map ("a " ++) xs
```
Si vemos este o otros ejemplo el comportamiento del patron se puede abstraer como:
```hs
map f [] = []
map f (f:xs) = (f x):map f xs
```
En la practica, no encontraras funciones recursivas escritas explicitamente. Pero esto es porque los patrones comunes de recursion son funciones de alto orden.

## Filtrando listas
Otra funcion de alto orden muy importante para trabajar es filter. La funcion filter se comporta similar a map, toma una funcion y una lista como argumentos y retorna una lista. La diferencia es que la funcion pasada es un filtro que se pasa y retorna True o False. La funcion pasa  solo funciones que pasan el test.
```hs
filter even [1,2,3,4]
filter (\(x:xs) -> x == 'a') ["apple", "banana", "avocado"]
["apple", "avocado"]
```
Lo mas interesante de filter es el patron de recursion que abstrae. como map la meta de filter es una lista vacia. Pero tiene 2 posibles alternativas: una lista no vacia al que el primer elemento es pasado,y una lista no vacia en que el elemento no se pasa. si el test falla, el elemento no es recursivamente pasado a la lista
```hs
filter test [] = []
filter test (x:xs) = if test x
					 then x:filter test xs
					 else filter test xs
```
## Folding una lista
La funcion foldl (l viene de izquierda) toma una lista y reduce este a un solo valor. La funcion toma 2 argumentos: una funcion binaria, un valor inicial, y una lista.
```hs
foldl (+) 0 [1,2,3,4]
```
foldl es talvez la funcion menos obvia de todas de las funciones de alto orden que se han cubierto. Lo forma en que foldl trabaja es aplicando el argumento binario al valor inicial y a la cabeza de la lista.
El resultado de esta funcion es ahora un nuevo valor.

Foldl es muy util pero definitivamente toma algo de practica llegar a usarla bien. 

Es comun usar foldl y map juntos. Por ejemplo para crear sumOfSquares que suma los cuadrados de todos los valores en una lista y toma la suma de estos
```hs
sumOfSquares xs = foldl (+) 0 (map (^2) xs)
```
Un ejemplo clasico de foldl es el de invertir una lista para lo que usamos una funcion auxiliar llamada rcons.
```hs
rcons x y = y:x
reverse xs = foldl rcons [] xs
```
En este caso, el unico valor que fold retorna es otra lista.

Implementar foldl es un poco mas dificil que las otras funciones vistas hasta ahora. Una vez que el estado meta es la lista vacia []. pero que deberia retornar? porque el valor inicial se actualizara despues de cada llamada a la funcion binaria, esta contendra el valor final en el calculo. cuando alcanzas el final de la lista, retornaras el valor actual par init.
Solo tienes otra alternativa: una lista no vacia. Para esto, pasamos el valor inicial y el primer elemento de la lista a la funcion binaria. Esta crea un nuevo init.Entonces llamamos a foldl sobre el resto de la lista para usar este nuevo valor como init.



```hs
foldl f init [] = init
foldl f init (x:xs) = foldl f newInit xs
	where newInit = f init x
```

La cuestion es porque folder a la izquierda. De hecho hay otra forma de resolver este problemas general de foldear una lista de valores en un solo valor. la alternativa a foldl es foldr; la r viene right (derecha) la definicion difiere como:
```hs
foldr f init [] = init
foldr f init (x:xs) = f x rightResult
	where rightResult = foldr f init xs
```
La razon de llamar a rigth fold es que son dos argumentos en una funcion binaria: un argumento a la izquierda y uno la derecha. el fold left compacta la lista a los argumentos de la izquierda, y el right fold al argumento derecho.

Hay diferencias computacionales y de rendimiento entre foldl y foldr. Para el aprendizaje es importante conocer que estas funciones dan diferentes respuestas si el orden de la aplicacion. Para la adicion no importa. Pero para la sustraccion si es diferente.

foldl es preferible para foldear lista porque su comportamiento es mas intuitivo. Entender la diferencia entres foldl y foldr es buena senal que eres maestro en recursion.

Hal otra funcion foldl': es una version no perezosa de foldl que a menudo mucho mas eficiente.
foldr: es a menudo mas eficiente que foldl y es el unico fold que trabaja con listas infinitas.
foldl: es el mas intuitivo de los folds, pero por lo general tiene un rendimiento terrible y no se puede usar listas infinitas.