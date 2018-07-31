## 3.1 Funciones Lambda

Un lambda es una funcion sin nombre, para ser referidas se ua la letra griega lambda como minuscula. Otro nombre comun que se da es **funcion anonima** 
```hs
\x -> x
```
Una funcion lambda son la minima funcion posible: toman un valor y retornan otro. No se puede solo escribir esta funcion sino hay que pasarle un argumento para que haga algo.
```hs
> (\x -> x) 4
```
Los lambdas son utiles pero tiene un periodo corto de vida.

## Haciendo nuestra propia clausula where
```hs
sumSquareOrSquareSum x y = if sumSquare > squareSum
							then sumSquare
							else squareSum
	where sumSquare = x^2 + y^2
		  squareSum = (x+y)^2
```
En la computacion anterior usamos where para hacer el codigo mas legible y reducir las computaciones.

Otra forma de reducir esto es dividir la funcion en 2 pasos:
```hs
body sumSquare squareSum = if sumSquare > squareSum
							then sumSquare
							else squareSum
sumSquareOrSquareSum x y =body (x^2 + y^2) ((x+y)^2)
```
Esto resulve el problema pero necesita mas trabajo. En este caso una mejor solucion es usar una funcion lambda
```hs
body = (\sumSquare squareSum -> 
		if sumSquare > squareSum
		then sumSquare
		else squareSum)
```
Si sustituimos esta funcion por body obtenemos la expresion
```hs
sumSquareOrSquareSum x y = (\sumSquare squareSum -> 
							if sumSquare > squareSum
							then sumSquare
							else squareSum) (x^2 + y^2) ((x+y)^2)
``` 
Esto no se ve tan bien como where pero esta mucho mejor que lo que tenias antes. Lo mas importantes es que se implementa la idea de variables desde cero.

## 3.3 Desde lambda a let: haciendo nuestras propias variables
Aunque el lambda es mas desordenado que el where original es tambien mas poderoso.
where hace qle el codigo este sintacticamente encerrado en tu funcion. en cambio el lamda es una pieza de codigo autocontenida que se puede pegar y usar en cualquier lugar

Una alternativa a **where** son las expresiones **let**. Esta ultima permite combinar la legibilidad de un where con el poder de las funciones lambda.

```hs
sumSquareOrSquareSum x y = let sumSquare = (x^2 + y^2) # primer se definen
							   squareSum = (x+y)^2     # las varibles
						   in
						   	 if sumSquare > squareSum  # cuerpo de la 
						   	 then sumSquare            # expresion let
						   	 else squareSum
```
Escoger entre let o where es una cuestion de estilo la mayoria de las veces.
En programacion funcional, rara vez tiene sentido sobreescribir una variable, pero esto se puede hacer.
```hs
overwrite x = let x = 2
			  in
			  	let x = 3
			  	in
			  	  let x = 4
			  	  in
			  	    x
```
overwrite permite redifinir variables, de forma respetuosa con la programacion funcional.

## Funciones lambda en la practica y alcance lexicografico
Javascript tiene tambien un equivalente a los lambdas
```javascript
function (x) {
	return x;
}
```
Como javascript no hacia uso de namespace ni modulos era comun crear variables globales que generaban un codigo propenso a errores.
Una forma segura de resolver este problema es envolver esto en una funcion lambda y llamar inmediatamente a una funcion, asi tu codigo se mantiene seguro.
Este patron IIFE **inmediately invoked function expression** 
```js
(function(){
var a = 2;
var b = 3;
var c = a + b;
var d = libraryAdd(10,20);
console.log(c)
})
```
Esta solucion usa los mismos principios de reemplazo que la clausula where. La creacion de una nueva funcion da lugar a un nuevo ambito o alcance que es el contexto en el que la variable se define. Si una variable no esta ahi se seguira buscando en la superior. Este tipo de busqueda de variable se llama alcance lexicografico.

Usar funciones sin nombre para crear un alcance es una herramienta esencial para hacer cosas mas poderosas con lambdas.