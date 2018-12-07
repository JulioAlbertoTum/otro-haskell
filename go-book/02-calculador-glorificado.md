### 2.1 Realizando calculos
Hay dias en los que pensamos vernos mas jovenes y con menos peso. En este tema, Marte tiene mucho que ofrecer. Marte toma 687 dias de la tierra para viajar alrededor del sol, y con su gravedad mas debil significa que tu peso es aproximadamente el 38% del que tienes en la tierra.

Para calcular cuan joven y liviano es Nathan en Marte, escribiremos un programa pequeno, que se ve en la lista 2.1. Go provee los mismos operadores aritmeticos asi como otros lenguajes de programacion: +, -, *, /, y % para adicion sustraccion, multiplicacion, division, y modulo respectivamente.

```go
// My programa de baja de peso  : un comentario para los lectores
package main

import "fmt"

func main() {
    fmt.Println("Mi peso en la superficie de marte es")
    fmt.Println(149.0 * 0.3783) // imprimir 56.3667
    fmt.Println("lbs, y mi edad es ")
    fmt.Println(41 * 365 / 687) // imprime 21
    fmt.Print(".")
}
```

El codigo en el listado precedente comienza con un comentario. Cuando Go ve un slash doble, ignora todo hasta el final de la linea. La programacion de computadoras es todo sobre comunicacion. El codigo comunica tus instrucciones a una computadora y cuando esta bien escrito este comunica tus intenciones a otras personas. Comentarios son solo para nosotros. Ellos no afectan como corre un programa.

La lista precedente llama a la funcion Print varias veces para mostrar una sentencia en una sola linea. Alternativamente, puedes pasar una lista de argumentos separados por comas. Un argumento para **Println** puede ser texto, un numero, o una expresion matematica:
```go
fmt.Println("Mi peso sobre la superficie de marte es", 149.0 * 0.3783, "lbs, y mi edad debe ser", 41 * 365.2425/687, " years old.")
```
### 2.2 Impresion con formateado
Las funciones Print y Println tienen un hermano que da mucho mas control sobre la salida. Pero usa **Printf**, muestra en la siguiente lista, puedes insertar valores cualquiera en el texto.
```go
    fmt.Printf("Mi peso en la superficie de marte es %v lbs, ", 149.0 * 0.3783)
    fmt.Printf(" y mi edad deberia ser %v.\n", 41 * 365 / 687)
```
A diferencia Print y Println, el primer argumento de Printf es siempre un texto. El texto contiene el **verbo de formato %v**, que es sustituido por el valor de la expresion provista por el segundo argumento.

La funcion Println automaticamente mueve a la siguiente linea, pero Printf y Print no. Sin embargo si quieres moverte a  una nueva linea, coloca \n en el texto.

Si se expresan multiples formatos verbo, la funcion Printf sustituye multiples valores en el orden:
```go
fmt.Printf("Mi peso en la superficie de la %v es %v lbs.\n", "Tierra", 149.0)
// imprime Mi peso en la superficie de la Tierra es 149.0 lbs.
```
En adicion a la sustitucion de valores cualquier en la sentencia, Printf puede ayudar a alinear texto. Especifica un ancho como parte del verbo de formato, tal como **%4v** para dar una valor con 4 caracteres de ancho. Un numero positivo de pads da espacios a la izquierda y un numero negativo da espacios a la derecha:

```go
fmt.Printf("%-15v $%4v\n", "SpaceX", 94)
fmt.Printf("%-15v $%4v\n", "Virgin Galactic", 100)
// imprime
// SpaceX          $  94
// Virgin Galactic $ 100
```

### 2.3 Constante y variables
Los calculos en el listado 2.1 son realizados sobre numeros literales. Esto no es claro lo que el numero significa, valores particulares como 0.3783. Los programadores algunas veces se refieren a numeros literales poco claros como **numeros magicos**. Constantes y variables pueden ayudar proveer nombres descriptivos.

Despues de ver los beneficios de vivir en Marte. la siguiente pregunta es cuan largo es el viaje a tomar. Viajando a la velocidad de la luz es ideal. la luz viaja a una velocidad constante en el espacio vacio, que hace la matematica mas  facil. En la otra mano, la distancia entre la tierra y marte varia significativamente, dependiendo sobre donde los planetas orbitan alrededor del sol. 

La siguiente lista introduce dos nuevas palabras clave, const y var, para declarar constantes y variables respectivamente. 

```go
const lightSpeed = 299792  // km/s
var distance = 56000000 // km
fmt.Println(distance/lightSpeed, "seconds")
distance = 401000000
fmt.Println(distance/lightSpeed, "seconds")

// 186 seconds
// 1337 seconds
```
Tipeando la lista 2.3 en el playground de Go y presionando Run. La velocidad de la luz es muy conveniente; probablemente nunca escuchaste preguntar, ya llegamos?

El primer calculo esta basado en la cercania de marte y la tierra, con la distancia declarada asignada inicialmente con 56,000,000 km. Entonces la distancia es variable es asignada un nuevo valor de 401,000,000 km, con los planetas en lados opuestos del sol, aunque dibujar un curso directo al sol podria ser problematico.

### 2.4 Tomando un atajo
Puede que no haya atajos para visitar marte, pero go provee unos pocos atajos de **keystroke-saving** (pulsacion de teclas salvado)

#### 2.4.1 Declarar multiples variables a la vez 
Cuando declaramos variables o constantes, puedes declarar cada una en su propia linea como esto:
```go
var distance = 56000000
var speed = 100800
```
O se puede declara en grupo
```go
var (
    distance = 56000000
    speed = 100800
)
```
Hay otra opcion es declarar multiples variables en una sola linea:
```go
var distance, speed = 56000000, 100800
```
Antes de declarar multiples variables como un grupo o en una sola linea, considera si las variables estan relacionadas o no. Siempre ten en mente la legibilidad de tu codigo.

### 2.4.2 Operadores de asignacion e incremento
Hay pocos atajos para realizar asignaciones con otros operadores. Las ultimas dos lineas de la siguiente son equivalentes.
```go
var weight = 149.0
weight = weight * 0.3783
weight *= 0.3783 
```
Incrementado por uno tiene un atajo adicional, como se muestra a continuacion.
```go
var age = 41
age = age + 1
age += 1
age++
```
puedes decrementar con **count--** o otras operaciones mas cortas como price /= 2 en la misma forma.

### 2.5 Pensar en un numero
Piensa en un numero entre 1 y 10

Hazlo? Okay.

Ahora tenemos que hacer que una computadora "piense" en un numero entre 1 y 10. Tu computadora puede generar numero pseudoaleatorio usando el paquete **rand**.Ellos se llaman pseudoaleatorios porque son mas o menos aleatorios, pero no verdaderamente aleatorios.

el codigo mostrado en 2.6 muestra dos numeros entre 1-10. Pasando  10 a **Intn** retorna un numero entre 0  y 9, para que adicion 1 asigne el resultado a num. La variable **num** np puede ser una constante de Go porque es el resultado de la llamada de una funcion.
```go
package main

import (
    "fmt"
    "math/rand"
)

func main() {
    var num = rand.Intn(10) + 1
    fmt.Println(num)
    
    num = rand.Intn(10) + 1
    fmt.Println(num)
}

// impresion
2
8
```
La direccion de importacion para el paquete rand es **math/rand**. La funcion Intn es prefijada con el nombre del paquete rand, pero la direccion de importacion es mas largo.

*Tip: * Para usar un paquete nuevo, este debe ser escuchado co un import. El playground de Go puede adicionar direccion de importacion para ti. Primeros aseguramos que el checkbox import es verificado.








