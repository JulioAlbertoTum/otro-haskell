### La anatomia de una lista

Es la estructura de datos mas importante en programacion fucnional. Ya que son inherentemente recursivas. Tomar valores y construir listas  son la herrameinta ma importante en FP.

Una lista vacia es diferente de otras ya que no tiene head o tail. 
En FP fragmentar  listas es tan importante  como construirlas. para crear solo es necesario el operador infijo **(:) que llamamos cons** Este termino es la abreviacion de **constructor** de origen en lisp.(tambien se hace referencia a consing)

Todas las listas en haskell son representadas como una rama de operacion de consignacion
```hs
>1:2:3:4:[]
[1,2,3,4]
>(1,2):(3,4):(5,6):[]
[(1,2),(3,4),(5,6)]
```
Una cosa importante en haskell es que todos los elementos de una lista deben ser del mismo tipo.

Si quisieras combinar 2 listas es mejor usar ++ que es operador para concatenar 2 listas.

### 6.2 Listas y evaluacion perezosa
Hay muchas formas de generar rangos de datos con distinto tamanio de paso
```hs
> [1..10]
[1,2,3,4,5,6,7,8,9,10]
> [1,3 .. 10]
[1,3,5,7,9]
>[1, 1.5 .. 5]
[1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
```

En haskell es posible hacer asignaciones como:
```hs
simple x = x
longList = [1 .. ]
stillLongList = simple longList
```
Este codigo compilara bien. crea una lista infinita y la usa en una funcion. Esto es posible gracias a la evaluacion perezosa. En la evaluacion perezosa el codigo no se evalua hasta que sea necesario.

La evaluacion perezosa tiene ventajas y desventajas. Las ventajas incluyen el benficio computacional es que el codigo no necesario nunca es computado. Otro beneficios es que es posible definir estructuras interesantes tales como listas infinitas. Las desventajas son que la evaluacion perezosa son menos obvias. ademas es mucho mas dificil razonar sobre el rendimiento del codigo. 

### Funciones comunes sobre listas
Hay un importante numero de funciones utiles 
```hs
[1,2,3] !! 0  -- nos permite acceder al valor de una lista por su indice 
1
length [1..20]  -- nos da la longitud de la lista
20
reverse [1,2,3] -- invierte el orden de la lista
[3,2,1]
elem 13 [0, 13 .. 100] -- toma un valor y una lista y devuelve true si esta en la lista.
take 5 [2,4 .. 100] -- toma un numero y una lista y retorna los primeros n elementos
[2,4,6,8,10]
drop 2 [1,2,3,4,5] -- remueve los primeros n elementos de la lista
zip [1,2,3] [2,4,6] -- combina dos listas miembro a miembro en una tupla
ones n = take n (cycle [1]) -- usa evaluacion perezosa para crear
ones 2                      -- una lista infinita, se usa en computacion numerica
[1,1]
ones 4
[1,1,1,1]
```
