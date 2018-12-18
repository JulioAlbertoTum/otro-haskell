Go ofrece 10 tipos diferentes para los numeros enteros, llamados colectivamente *integers*, Enteros no sufren del problema de exactitud de los tipos de punto flotante, pero ellos no pueden almacenar numeros fraccionarios ademas de tener un rango limitado. El tipo entero que se escoja dependera del rango de valores  que se necesiten en una determinada situacion.

### 7.1 Declaracion de variables de enteros
5 Tipos de enteros usan signo, que significa que ellos pueden representar numeros enteros positivos y negativos. El tipo de entero mas comun es un entero con signo con la abreviatura *int*:
```go
var year int = 2018
```
Los otros 5 tipos de enteros no tienen signo, significa que ellos solo puede ser usado con numeros positivos. La abreviacion usada es *uint*
```go
var month uint = 2
```
Cuando usamos inferencia de tipos, Go siempre escogera el tipo *int* para un numero entero literal. las siguientes 3 lineas son equivalentes.
```go
year := 2018
var year = 2018
var year int = 2018
```
*Tips: * Como en el siguiente tipo de punto flotantees preferible no especificar el tipo int cuando este puede ser inferido.

### 7.1.1 Tipos de Enteros para cada ocasion
Enteros, con o sin signo, vienen en una variedad de tamanio. El tamanio afecta a los valores minimos y maximos y como la memoria es consumida. Hay ocho tipos de sufijos independientes de la arquitectura con el numero de bits que ellos necesitan, se sumariza en la tabla 7.1 

Hay un monton de tipos para escoger! Despues en esta leccion, mostraremos algunos ejemplos donde especificaremos tipos de enteros que tengan sentido, y que pasa cuando tu programa excede el rango disponible.

Hay 2 tipos de enteros no listados en 7.1 El *int* y el tipo *uint* son optimos para el dispositivo. El Go playground, Raspberry Pi 2, y viejos moviles proveeran un ambiente de 32-bit donde ambos int y uint son valores de 32 bits. Cualquier computadora reciente proveera un ambiente de 64 bits donde int y uint tendran valores de 64 bits. 

*Tips:* Si estas operando sobre numeros mas grandes que 2 billones, y si el codigo podria ejecutarse sobre hardware viejo de 32 bits, asegurate  de usar int64 o uint64 en lugar de int y uint 

*Nota: * Aunque es tentador pensar en *int* como un *int32* sobre algunos dispositivos y un *int64* sobre otros dispositivo, hay 3 distintos tipos. El tipo *int* no es un alias para otros tipos.

### 7.1.2  Conociendo tu tipo
Si eres curioso por saber que tipo infiere el compilador de Go, la funcion Printf provee el  verbo de formato %T para mostrar el tipo de una variable, como se muestra en la lista.
```go
year := 2018
fmt.Printf("Tipo %T para %v\n", year, year) // Imprime el tipo Int para 2018
``` 
En lugar de repetir la variables 2 veces, puedes llamar a Prinf usando el primer argumento[1] para la segunda forma verbal.
```go
days := 365.2425
fmt.Printf("Type %T para %[1]v\n", days) // Imprime tipo float64 para 365.2425
```
### 7.2 El tipo uint8 para colores de 8 bits
En CSS (hojas de stilo en cascada), los colores sobre la pantalla son especificados como una tripleta red, green, blue, cada una con rango 0-255. Esta es una situacion perfecta para usar el tipo uint8, y enteros sin signo capaces de representar valores de 0 a 255
```go 
var red, green, blue uint8 = 0, 141, 213
```
Aqui todos los beneficios de uint8 en lugar de un int regular  en este caso:
- Con un uint8, las variables son restringidas a un rango de valores validos, eliminando 4 millones de  posibilidades incorrectas comparadas con un entero de 32 bits.
- Si hay un  monton de colores almacenados secuencialmente, tal como un imagen sin comprimir, podrias lograr ahorra una considerable cantidad de memoria usando enteros de 8 bits.

### 7.3 Enteros y redondeos
Los enteros son libres de redondear errores que hacen los puntos flotantes  inexactos, Pero todos los tipos enteros tienen un problema diferent: un rango limite. Cuando el rango es excedido, los entero en Go "wrap around"

En enteros sin signo de 8 bit se tiene un rango de 0-255. Incrementado mas alla de 255 el volvera a posicionarse en 0. La siguiente lista muestra los enteros sin y con signo,  y com se causa el "wrap around".
```go
var red uint8 = 255
red++
fmt.Println(red)  // Imprime 0
var number int8 = 127
number++
fmt.Println(number) \ Imprime -128
```
### 7.3.1 Viendo los bits
Para entender porque los enteros vuelven, hechemos un  vistazo a los bits. el formato de verbo %b nos muestra un valor entero como bits. Como otros verbos formato, %b puede ser colocado a cero para un minimo valor, como veras en la lista.
```go
var green uint8 = 3
fmt.Printf("%08b\n", green) // Imprime 00000011
green++
fmt.Printf("%08b\n", green) // Imprime 00000100
```
*Tip: * El paquete math define math.MaxUint16 como 65535 y similares constantes maximas y minimas para cada tipo de entero independiente de la arquitectura. Recuerda que int y uint puede ser 32-bit o 64-bit, dependiendo del hardware bajo el que se trabaja.

En el listado 7.3, incrementar green causa que 1 sea acarreado, llevando ceros a la derecha. El resultado es 00000100 en binario, o 4 decimales, como se muestra en 7.1.

Lo mismo pasa cuando incrementamos 255, con una diferencia critica: con solo 8 bits disponibles, el 1 es acarreado como se vera ahora, asi el valor de blue tiene 0a la izquierda como se muestra en el listado.
```go
var blue uint8 = 255
fmt.Printf("%08b\n", blue) // Imprime 11111111
blue++
fmt.Printf("%08b\n", blue) // Imprime 00000000
```
Envolver puede ser algo que sea deseable en alguna situacion pero no siempre. La forma mas simple de evitar envolver es el uso de enteros mas de tipo mas grande que el valor que esperes almacenar.

### 7.3.2 Evita envolver en el tiempo
Sobre sistemas operativos Unix, el tiempo es representado como el numero de segundos desde el 1 de enero de 1970 UTC (Coordinated Universal Time). En el anio 2038, el numero de segundos desde el 1 de enero de 1970 habra excedido los 2 billones, la capacidad de int32.

Afortunadamente, int64 puede soportar fechas mas halla del 2038. Esta es una situacion donde int32 o int  simplemente no puede hacer nada. Solo los enteros de tipo int64 o uint64 pueden almacenar valores mas alla de los 2 billones en todas las plataformas.
El codigo listado en 7.5 usa la funcion unix del paquete time. Este acepta 2 parametros int64, correspondiente al numero de segundos y el numero de nanosegundos desde el 1 de enero de 1970. Usando un gran valor disponible (sobre los 12 billones) demostrando asi que las fechas mas alla del 2038 funcionan bien en Go.
```go
package main
import (
    "fmt"
    "time"
)
func main() {
    future := time.Unix(12622780800, 0)
    fmt.Println(future)  // Imprime 2370-01-01 00:00:00 +000 UTC
}
``` 



