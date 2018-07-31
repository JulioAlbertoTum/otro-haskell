# Programacion Funcional

Toda funcion en Haskell sigue tres reglas:
- Todas las funciones deben tomar un argumento.
- Todas las funciones deben retornar un valor.
- Cualquier funcion es llamada con el mismo argumento, debe retornar el mismo valor.

La tercera regla es una definicion matematica de una funcion y se le suele llamar **Transparencia Referencial**

El calculo lambda de alonso church resulto ser un modelo universal de computacion al igual que la maquinade Turing.

La principal ventaja de la programacion funcional es que nos brinda el poder de las matematicas en la programacion en una forma usable.

### El valor de la programacion funcional en la practica

Un lenguaje de programacion seguro es uno que forza a tus programas a comportarse de la forma esperada.

Cuando tu no  pasas un argumento a una funcion entonces estas accediendo a algun valor en tu ambiente, y si  ademas no retornas un valor entonces estas cambiando alguna variable en tu entorno. Este **cambio de estado** ocasiona **efectos secundarios**

### Variables

```hs
x = 2
```
El unico detalle en haskell es que las **variables** no son variables realmente. Es mejor pensar en estas como **Definiciones** 

Podemos usar una clausula **where** para realizar un calculo a la vez y asignarlo a una variable, where invierte el uso normal para escribir variables. A diferencia de otros lenguajes este orden nos da a entender que la asignacion se hace una sola vez, ademas que hay una ganancia de legibilidad.
```hs
calcCambio propio dado = if change > 0
						 then change
						 else 0
    where change = dado - propio
```
### Variables que son variables
Dado que el cambio es una parte inevitable de la vida, tiene sentido que las variables puedan ser reasignadas. A partir de GHC version 8 las variables se prefijan con la clausula **let**  para diferenciarlas de otras variables en haskell. Las funciones tambien pueden ser prefijadas de esta forma

```hs
> let x  = 5
> let f x = x^2
> f 8
64
```
