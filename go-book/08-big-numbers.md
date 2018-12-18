Los lenguajes de programacion esta lleno de compensaciones. Tipos de punto flotante puede almacenar numeros de cualquier tamanio, pero ellos carecen de precision y exactitud a veces. Enteros son exactos pero tienen un rango limitado. Que si necesitas un numero realmente grande, y exacto? Esta leccion explota 2 alternativas a los tipos nativos *float64* e *int*.

### 8.1 Golpeando el Techo
Si no lo has realizado esto todavia, los enteros de 64 bits son alucinantemente grandes - muchos mas grandes que su contraparte de 32 bits.

Para alguna perspectiva, la estrella mas cercana es Alpha Centauri, esta a 41.3 trillones de kilometros de distancia. Un trillon es un 1 seguido de 12 ceros o 10^12. En lugar de typear laboriosamente todos los ceros, pudes escribir tales numeros en Go con un exponente, de la siguiente forma:
```go
var distance int64 = 41.3e12
```
Un *int32* o *uint32* no puede ser contenido tal como un gran numero, pero en int64 no es necesario transpirar. Ahora puedes ir sobre tus negocios, quizas calculando cuandos dias podria tomarnos viajar a Alpha Centauri, una tarea que asumimos en la siguiente lista.
```go
const lightSpeed = 299792 // km/s
const secondsPerDay = 86400   // Imprime: 41300000000000 km

var distance int64 = 41.3e12
fmt.Println("Alpha Centauri esta", distance, "km de distancia.")

days := distance / lightSpeed / secondsPerDay
fmt.Println("Hay", days,"dias de viaje a la velocidad de la luz.")
// Imprime: Hay 1594 dias de viaje a la velocidad de la luz
```
Tan grande como los enteros de 64 bits, hay algo mas grande: el espacio. La galaxia de andromeda es 24 quintillones (10^18) kilometros de lejania. Incluso en entero sin signo mas grande (uint64) puede solo contener numeros por encima de los 18 quintillones. Intenta declarar una variable mas alla de 18 quintillones reportanto error de overflow.
```go
var distance uint64 = 24000000000000000000   // overflow
```
Pero no entres en panico -  todavia hay una pocas opciones. Puedes usar matematica de punto flotante. Que no es una mala idea, ya que conoces como trabaja el punto flotante. Pero hay otra forma. En la siguiente seccion echaremos  un vistazo al paquete de Go *big*

Nota: Si una variable no tiene un tipo explicito, Go inferira float64 para numeros que contiene exponentes.

### 8.2 El paquete big
El paquete big provee 3 tipos:
- *big.Int* es para los enteros, cuando 18 quintillones no abastece.
- *big.Float* es para precisiones arbitrarias de numeros de punto flotante.
- *big.Rat* es para las fracciones como 1/3

Nota: Tu codigo puede declarar nuevos tipos tambien, veremos esto en leccion 13.

El tipo *big.Int* puede felizmente almacenar y operar en la distancia de la galaxia de Andromeda, unos meros 24 quintillones de kilometros.

Optar usar big.Int. requiere que uses esta para todo en tu ecuacion. incluso las constantes que tenias. La funcion NewInt toma n int64 y retorna un big.Int:
```go
lightSpeed := big.NewInt(299792)
secondsPerDay := big.NewInt(86400)
```
NewInt no va servir para un numero de 24 quintillones. este no llenara un int64, asi que en su lugar puede crear un bit.Int a partir de un string:
```go
distance := new(bit.Int)
distance.SetString("2400000000000000000000", 10)
```
Despues de crear un nuevo big.Int, asignar el valor de 24 quintillones llamando al metodo SetString. El numero 24 quintillones esta en base 10 (decimal), asi el segundo argumento es 10.

*Nota: * Metodos son similares a las funciones. Aprendereras sobre estos en la leccion 13. la funcion new es para los punteros, que son cubiertos en la leccion 26.

Con todos los valores en su lugar, el metodo Div realizara la division necesaria  asi el resultado puede ser mostrado, como sigue en la lista.
```go
package main

import (
    "fmt"
    "math/big"
)

func main() {
     lightSpeed := big.NewInt(299792)
     secondsPerDay := big.NewInt(86400)

     distance := new(big.Int)
     distance.SetString("24000000000000000000", 10)
     fmt.Println("La Galaxia de Andromeda esta", distance, "Km de distancia")
     seconds := new(big.Int)
     seconds.Div(distance, lightSpeed)

     days := new(big.Int)
     days.Div(seconds, secondsPerDay)
    
     fmt.Println("Hay", days, "dias de viaje a la velocidad de la luz.")
}

// Salida:
// La Galaxia de Andromeda esta 24000000000000000000 Km de distancia
// Hay 926568346 dias de viaje a la velocidad de la luz.
```
Como puedes ver, estos tipos grandes son mas incomodos para trabajar que los tipos nativos int y float64. Ellos son tambien mas lentos. Esas son las compensaciones de ser capaz de manejar representaciones de numeros de cualquier tamanio.

### 8.3 Constantes de tamanio Inusual
Constantes pueden ser declaradas  con un tipo, asi como las variables. y solo  como las variables, para una constante *uint64* no es posible contener 24 quintillones
```go 
const distance uint64 = 24000000000000000000 // constante con overflow uint64
```
Se pone interesante  cuando declaras una constante sin un tipo. Para variables , Go usa inferencia de tipo para determinar el tipo, y en el caso de 24 quintillones, sobrepasara al tipo *int*. Las constantes son diferentes. En lugar de inferir un tipo, constantes pueden ser sin tipo. La siguiente linea no causa un error de desbordamiento:
```go 
const distance = 24000000000000000000
```
Constantes son declaradas con la palabra clave const. pero todo valor literal en tu programa es una constante tambien. Esto significa que extraodinariamente el tamanio de los numeros puede ser directamente usado, coo se muestra en la siguiente lista.
```go
fmt.Println("Galaxia de Andromeda esta", 24000000000000000000/299792/86400, "dias luz de distancia.")
// Imprime:
// Galaxia de Andromeda esta a 926568346 anios luz de distancia.
```
Calculos sobre las constantes y literales son realizados durante la compilacion en vez de cuando el programa esta corriendo, el complilador de Go esta escrito en Go. Bajo el capot, las constante numericas sin tipo son tratados por el paquete big, permitiendo todas las operaciones usuales con numeros mas alla de los 18 quintillones, como se muestra en la siguiente lista.
```go
const distance = 24000000000000000000
const lightSpeed = 299792
const secondsPerDay = 86400 

const days = distance / lightSpeed / secondsPerDay

fmt.Println("Galaxia de Andromeda esta", days, "dias luz de distancia.")
// Imprime: Galaxia de Andromeda esta a 926568346 dias luz de distancia.
```

Valores constantes pueden ser asignados a variables siempre y cuando quepan. Un int no puede contener 24 quintillones, pero 926,568,346 llena esto muy bien:
```go
km := distance
days := distance / lightSpeed / secondsPerDay     // 926568346 llena un entero
```
Hay una advertencia de constantes de tamanio inusual. Aunque el compilador Go utiliza el paquete big para constantes numericas sin tipo, constantes y big.Int valores no son intercambiables. La lista muetra un big.Int contiene 24 quintillones, pero no puedes mostrar la distancia constante debido a  un error de desbordamiento.
```go
fmt.Println("Galaxia de Andromeda esta", distance, "km de distancia") 
// constante 24000000000000000000 entero con desbordamiento.
``` 
Las constantes grandes son ciertamente utiles, pero ellas no son un reemplazo del paquete big.