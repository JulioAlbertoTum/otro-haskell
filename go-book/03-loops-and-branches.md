Programas de computadora raramente se leen desde el principio a fin como una novela. Programas son mas como escoger un libro de aventura o ficcion interactiva. Ellos toman diferentes caminos bajo ciertas condiciones o repiten los mismos pasos hasta conseguir un condicion.

Si estas familliarizado con if, else, y for encontrados en muchos lenguajes de programacion, esta leccion servira como una rapida introduccion a la sintaxis de Go.

### 3.1 True o False
Cuando lees tus libros de aventura pasas a traves de elecciones como esta:
- *Si quieres caminar fuera de la cueva ve a la pagina 21* 
Si quieres caminar fuera de la cueva? En Go, tu respuesta puede ser true o false, dos constantes que estan actualmente dcclaradas. Puedes usarlas como: 
```go
var walkOutside = true
var takeTheBluePill = false
```
En Go, el unico valor true es true y el unico false es false (en python 0 o "" pueden representar false)

True y false son valores  booleanos, fueron nombrados despues del siglo 19 por el matematico George Boole. Varias funciones en la libreria estandar retornan un valor Booleano. Por ejemplo, la siguiente lista usa la funcion Contains del paquete **strings** para preguntar si la variabla command contiene el texto "outside". Asi si contiene el texto devuelve true.

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    fmt.Println("Te encuntras a  ti mismo en la caverna.")
    var command = "camina fuera"
    var exit = strings.Contains(command, "fuera")
    fmt.Println("Estas fuera de la caverna:", exit)
}
``` 
### 3.2 Comparaciones 
Otra forma de llegar a true o false es mediante la comparacio de valores. Go provee los operadores de comparacion.
-- ==  Igual               |    != No igual
-- <   menor que           |    >  Mayor que
-- <=  menor que o igual   |    >= Mayor que o igual que

Puedes usar estos operadores en la tabla 3.1 para comparar texto o numeros, como se muestra en la siguiente lista.

```go
fmt.Println("Hay in letrero en la entrada que dice 'No menores'.")
    var age = 41
    var minor = age < 18
    fmt.Printf("Mi edad es %v, soy menor? %v\n", age, minor")

Hay in letrero en la entrada que dice 'No menores'.
Mi edad es 41, soy menor? false
```
*Nota:*  En Go solo existe una igualdad para elementos del mismo tipo (js y php permiten cosas como 1 == "1")

### 3.3 Ramificando con if
Una computadora puede usar valores Booleanos o comparaciones para escoger entre diferentes caminos con una sentencia if, como se muestra en la siguiente lista.
```go
package main

import (
    "fmt"
)

func main() {
    var command = "ve al este"
    if command == "ve al este" {
        fmt.Println("Te diriges a la montana.")
    } else if command == "ve dentro" {
        fmt.Println("Ingresas a la caverna donde viviras el resto de tu vida.")
    } else {
        fmt.Println("No entiendo eso")
    }
}

// Salida
// Te dirijes a la montana
```
*else if* y *else* son opcionales. Cuando hay varios caminos a considerar, puedes repetir *else if* tantas veces como necesites.

*Nota: * Go reporta error si accidentalmente usas (=) cuando quieres la igualdad (==).

### 3.4 Operadores logicos
En Go los operadores logicos || que significa or, y el operador logico && significa and. Use operadores logicos para verificar multiples condiciones una vez.

El codigo en la lista 3.4 determina si 2100 es un anio bisiesto. Las reglas para determinar un anio bisiesto es como sigue
- Cualquier anio que es igualmente divisible por 4 pero no es divisible por 100
- O cualquier anio que es igualmente divisible por 400

```go
fmt.Println("El anio es 2100, es biciesto?")
    var year = 2100
    var biciesto = year%400 == 0 || (year%4 == 0 && year%100 != 0)
    if leap {
        fmt.Println("Mira antes de saltar!")
    } else {
        fmt.Println("Manten tus pies en el suelo")
    }
```
Esta lista previa produce la salida siguiente:
```go
El anio es 2100, es bisiesto?
Manten tus pies en la tierra.
```
Asi como en la mayoria de lenguajes de programacion, Go usa logica de corto circuito. si la primera condicion es true (el anio es divisible por 400), no necesitamos evaluar que sigue al operador ||, asi esto es ignorado.

El operador && es el opuesto. El resultado es falso a menos que ambas condiciones sean true. Si el no es divisible por 4, aqui no necesitamos evaluar la siguiente condicion.

El operador logico not (!) cambia un valor booleano de false a true y viceversa. La siguiente lista muestra un mensaje si el jugador no tiene una antorcha o si la antorcha no esta encendida.

```go
var haveTorch = true
    var litTorch = false
    if !haveTorch || !litTorch {
        fmt.Println("Nada que ver aqui.")
    }
```
### 3.5 Ramificando switch
Cuando comparamos un valor con otros varios, Go provee la sentencia switch, que puedes ver en la siguiente lista.
```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println("Hay una entrada a una caverna y un camino al este.")
    var command = "ve dentro"
    switch command {
    case "ve al este":
        fmt.Println("Debes ir hacia la montana.")
    case "ingresa a la caverna", "ve dentro":
        fmt.Println("Te encuentras a ti mismo en una caverna.")
    case "lee el letrero":
        fmt.Println("El letrero dice 'No menores'.")
    default:
        fmt.Println("No entiendo eso")
    }
}

// Salida:
// Hay una entrada a una caverna y un camino al este.
// Te encuentras a ti mismo en una caverna.
```
O puedes usar *switch* con condiciones para cada caso, que es como usar muchos if..else. Una unica caracteristica de *switch*  es la palabra clave **fallthrough**, que es usado para ejecutar  el cuerpo de el siguiente case, como se muestra en la siguiente lista.

```go
var room = "lago"
    switch{
    case room == "cueva":   
        fmt.Println("Te encuentras a ti mismo en una caverna")
    case room == "lago":
        fmt.Println("El hielo parece solido aunque")
        fallthrough
    case room == "bajo el agua":
        fmt.Println("El agua esta muy fria")
    }
// salida

// El hielo parece solido aunque
// El agua esta muy fria
```

*Nota:* Caer a traves para por defecto en C, Java y JS, mientras que en Go toma un enfoque seguro requiriendo de una palabra clave explicita fallthrough

### 3.6 Repeticion con bucles
En lugar de typear el mismo codigo en multiples lineas, la palabra clave **for** repite el codigo por ti. El bucle listado cuenta hasta que count sea igual a 0.
Antes de cada iteracion, la expresion count > 0 es evaluada para producir una valor Booleano. Si el valor es false (count = 0), el loop termina - en otro caso, este ejecuta el cuerpo del bucle (el codigo entre { and }).

```go
    var count = 10 // Declara e inicializa
    for count > 0 { // una condicion
        fmt.Println(count)
        time.Sleep(time.Second)
        count-- // Decrementa cuenta
    }
    fmt.Println("Liftoff!")
```
Un bucle infinito no especifica una condicion **for**, pero puedes todavia **break** romper el bucle en cualquier momento. el siguiente codigo orbita 360 grados y para aleatoriamente.
```go
func main() {
    var degrees = 0
    for {
        fmt.Println(degrees)
        degrees++
        if degress >= 360 {
            degrees = 0
            if rand.Intn(2) == 0 {
                break
            }
        }
    }
}
```
