# Revision: Reglas de recursion
- Identificar la meta final
- Determinar que pasa cuando la meta es alcanzada
- Listar todas las posibilidades alternas.
- Determinar tu "enjuaga y repita".
- Asegurar que cada movimiento alternativo se mueva hacia alcanzar la meta

## Recursion sobre listas 
**Implementacion de length**
**Implementacion de Take**
**Implementacion de ciclo**
Esta es la funcion mas interesante para implementar, en ciclo tomas una lista y la repites para siempre.
Esto es gracias a la evaluacion perezosa, Desde el punto de vista de las reglas la funcion ciclo no tiene un estado meta. Incluso en haskell la recursion sin metas es algo bastante raro.

Primero sabemos que construiremos una lista. Construimos una version no infinita de la lista.
```hs
finiteCycle (first:rest) = first:rest ++ [first] -- finitecycle [1,2,3] ==> [1,2,3,1]
```
Esta version no es una lista infinita, para ciclar este proceso necesitas repertir el comportamiento del ciclo para el resto rest:[first]
```hs
myCycle (first:rest) = first: myCycle (rest ++ [first])
```
Incluso con la guia a menudo la recursion puede causar un dolor de cabeza. La clave es resolver problemas lo cual toma su tiempo, dirigido hacia una meta, y rasonando a traves del proceso. Los beneficios de los problemas recursivos es que su solucion son solo unas pocas linesas de codigo.

## 8.3 Recursion Patologica: funcion de Ackerman y la conjetura Collatz(Ulam)

Veremos algunas funciones que demuestran algunos de los limites de nuestras 5 reglas de recursion

### 8.3.1 La funcion de Ackerman
La funcion toma dos argumentos m y n. Cuando nos referimos a la definicion matematica usamos A(m,n) tiene 3 reglas:
- Si m = 0 returna n + 1
- Si n = 0 entonces A(m-1, 1)
- Si ambos m != 0 y n !=0, entonces A(m-1, A(m, n-1))
Si usamos haskell la implementacion seria:
```
ackermann 0 n = n + 1
ackermann m 0 = ackermann (m-1) 1
ackermann m n = ackermann (m-1) (ackermann m (n-1))
```
Si analizamos las metas si n=0 entonces decrementamos m y eventualmente llegaras a m=0. Lo mismo se aplica al caso final. el primer m decrementa hasta 0 y el segundo eventualmente decrementa a 0 tambien.
Incluso con parametro relativamente bajos la recursion es bastante cara.

## La conjetura de collatz (ulam)
Es un facinante problema aditivo en matematicas.La definicion involucra  un proceso recursivo dado un numero inicial n:
- Si n es 1, se termina
- Si n es par, repetimos con n/2
- Si n es impar, repetimos con n*3 + 1 
```
collatz 1 = 1
collatz n = if even n
			then collatz (n `div` 2)
			else collatz (n*3 + 1)
```
Sin embargo olvidamos confirmar que la recursion en cada estado alternativo conduce a cerrar a tu meta. El primer caso alternativo si en es par no es un problema. Cuando n es par estas dividiento a la mitad y eventualmente llegaras a 1. Pero en el caso impar no es decir de desvias de la meta. es posible incluso que si combinamos esta forma con el decremento de los pares lleguemos a 1. Sin embargo no lo sabemos nadie lo sabe. La conjetura de collatz es la suposicion que tu funcion de collatz siempre termina, pero no hay prueba de que sea verdad.
La funcion de collatz viola nuestras reglas en forma interesante. Esto no significa que debas desechar esta funcion. Sin embargo date cuenta que la regla 5 es violada. y es peligroso tratar con funciones que no terminan nunca.