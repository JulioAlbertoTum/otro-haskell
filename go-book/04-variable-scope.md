En el curso del programa, muchas variables son usados brevemente y despues descartados. Esto es facilitado por las reglas de alcance del lenguaje. 

### 4.1 Mirando dentro el alcance
Cuando una variable es declarada, esta viene en un alcance, o poniendolo de otra forma, donde las variables son visibles. Tu programa puede acceder a la variable a lo largo de su alcance, pero una vez que no esta en su alcance, intentar acceder reportara un error.

Un beneficio del alcance de variables es que puedes reusar el mismo nombre  para diferentes variables. Puedes imaginar si todas las  variables en tu programa tuvieran un unico nombre? Si es asi, trata de imaginar un programa un poco mas grande.

Alcance tambien ayuda mientras leemos a traves del codigo porque no necesitan guardar todas las variables en tu cabeza. Una vez una variable esta fuera del alcance, puedes dejar de pensar en esta variable.

En go, el alcance tiende a comenzar y terminar a lo largo de las lineas dentro {}. En la siguiente lista, la funcion main comienza un alcance, y el bucle for comienza un bucle con un alcance anidado.

```go
package main

import (
    "fmt"
    "math/rand"
    )

func main() {
    var count = 0   
    for count < 10 { // un nuevo alcance comienza
        var num = rand.Intn(10) + 1
        fmt.Println(num)
        count++ 
    } // fin del alcance
}
```
La variable *count* es declarada con el *alcance de la funcion* y es visible hasta el final de la funcion main. mientras  que la variable num es declarada dentro el alcance del bucle for despues que el bucle termina, la variable num queda fiera del alcance.

El compilador de Go reportara un error si se intenta acceder a num despues del bucle. Puedes acceder a la variable count despues del fin del bucle for porque esta declarado fuera del bucle, auque no hay realmente una razon para esto. Para confinar count al alcance del bucle for, sera necesario una forma diferente de declarar variables en Go.

### 4.2 Declaracion corta
Declaracion corta provee una sintaxis alternativa a la palabra clave var. Las siguientes dos lineas son equivalentes
```go
var count = 10
count := 10
```
Esto puede no paracer un gran cambio, pero salvar 3 caracteres hace una declaracion mas corta y mas popular que var. Mas importante, la declaracion corta puede ir en lugares donde var no puede.

La siguiente lista demuestra un variante del bucle for que combina inicializacion a una condicion, y una posterior sentencia que decrementa count. Cuando usamos esta forma del bucle for, el orden provisto es significativo: inicializacion, condicion, enviar.
```go
var count = 0
for count = 10; count > 0; count-- {
    fmt.Println(count)
}
fmt.Println(count) // count se retiene en el alcance
```
Sin declaraciones cortas, la variable count debe ser declarada fuera del bucle, que significa que permanece en el alcance despues que el bucle termina.

Para usar la declaracion corta, la variable count en la siguiente lista es declarada en la inicializacion como parte del bucle for y cae fuera del alcance una vez el bucle termina. Si count count es accedida fuera del bucle for, el compilador reportario un error *undefined: count* 
```go
for count := 10; count > 0; count-- {
    fmt.Println(count)
}
// count no esta fuera de este alcance.
```
La declaracion hace esto posible para declarar para declarar una nueva variable en una sentencia if, En la siguiente lista la variable num puede ser usada en cualquier rama de la sentencia if.

```go
if num := rand.Intn(3); num == 0 {
    fmt.Println("Aventuras espaciales")
} else  if num == 1 {
    fmt.Println("SpaceX")
} else {
    fmt.Println("Virgin Galactic")
} // num no es disponible fuera del alcance
```
La declaracion corta puede ser tambien usada como parte de una sentencia **switch**, como muestra la siguiente lista.
```go
switch num := rand.Intn(10); num {
case 0:
    fmt.Println("Space Adventures")
case 1:
    fmt.Println("SpaceX")
case 2:
    fmt.Println("Virgin Galactic")
default:
    fmt.Println("Random spaceline #", num)
}
```
### 4.3 Alcance Estrecho y Ancho
El codigo en la siguiente lista genera un vista de fechas aleatorias - quizas una fecha de salida a marte, Este demostrara diferentes alcances para Go y mostrara porque consideramos importante el alcance cuando declaramos variables
```go
package main

import (
    "fmt"
    "math/rand"
    )

var era = "AD" // disponible atraves del paquete

func main() {
    year := 2018 // era y year en el alcance
    switch month := rand.Intn(12) + 1; month { // era, year, y month en alcance
    case 2:
         day := rand.Intn(28) + 1    // era, year, month y dia en alcance
         fmt.Println(era, year, month, day)
    case 4, 6, 9, 11:
         day := rand.Intn(30) + 1   // es un nuevo dia
         fmt.Println(era, year, month, day)
    default:
         day := rand.Intn(31) + 1  // es un nuevo dia
         fmt.Println(era, year, month, day)
    }  // month y day estan fuera del alcance
}  // year no esta en el alcance
```

La variable *era* es declarado fuera de la funcion *main* en el alcance del paquete. si hubiera multiples funciones en el paquete main, *era* seria visible en todos ellos.

*Nota: *La declaracion corta no esta disponible para variables declaradas en el alcance del paquete , asi que era := "AD" 

La variable *year* es solo visible en la funcion main. Si hubiera otras funciones podrias ver *era* pero no *year*. El alcance de la funcion es mas estrecho que el alcance del paquete. Este comienza con la palabra clave *func* y termina con la llave de terminacion.

La variable *month* es visible en cualquier lugar en la sentencia *switch*, pero una vez  termina, month no esta en el alcance. El alcance comienza con la palabra clave switch y termina con la llave de terminacion para switch.

Cada *case* tiene su propio alcance, asi que estos tiene 3 variables *day* independientes. Como cada *case* termina, la variable *day* declarada con el *case* sale del alcance. Esta es la unica situacion donde los llaves no indican alcance.

El codigo en el listado esta lejos de ser perfecto. El alcance estrechode *month* y *day* resulta en duplicacion del codig (Println, Println, Println). Cuando este codigo es duplicado, algunas veces puedes revisas el codigo en un lugar, pero no en otro (tal como decidir o no imprimir era, pero olvidamos cambiar un caso). Algunas veces la duplicacion del codigo esta justificaco, pero este es considerado **codigo oloroso** y debe ser observado.

Para remover la duplicacion y simplificar el codigo, las variables en el listado deberian ser declarados en el alcance ancho de la funcion, haciendolos disponibles despues de la sentencia **switch** para trabajar despues. Es tiempo de refactorar! Refactorar significa modificar el codigo sin modificar el comportamiento del codigo. El codigo en la siguiente lista todavia muestra una fecha aleatoria
```go
package main

import (
    "fmt"
    "math/rand"
    )

var era = "AD"

func main() {
    year := 2018
    month := rand.Intn(12) + 1
    daysInMonth := 31
    switch month {
    case 2:
        daysInMonth = 28
    case 4, 6, 9, 11:
        daysInMonth = 30
    }
    day := rand.Intn(daysInMonth) + 1
    fmt.Println(era, year, month, day)
}
```
Aunque un alcance estrecho a menudo reduce la sobrecarga mental, el listado anterior demuestra la restriccion de variables muy apretado puede resulta en codigo menos legible. Toma esto como caso por caso, refactora hasta que no puedas mejorar la legibilidad mas.




