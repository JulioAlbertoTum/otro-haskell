Las computadoras almacenan y manipulan numeros reales como 3.14159 usando el standard IEEE-754. Los numeros de punto flotante pueden ser muy grandes o increiblemente pequenos: piensa en galaxias y atomos. Con tal versatilidad, los lenguajes de programacion como javascript y Lua usna numeros de punto flotante exclusivamente. Las computadoras tambien soportan integers para numeros enteros, que es tema de la siguiente leccion.

### 6.1 Declaracion de variables de punto flotante
Toda variable tiene un tipo. Cuando declaras e inicializas una variable con un numero real, estas usando un tipo punto flotante. Las siguientes tres lineas de codigo son equivalentes porque el compilador de go infiere que *days* es un *float64*, incluso si no lo especificas:
```go
days := 365.2425 // declaracion corta
var days = 365. 2425
var days float64 = 365. 2425
```
Es valioso conocer que *days* tiene un tipo *float64*, pero es un poco superflu especificar *float64*. Entre tu y yo el compilador de Go puede inferir el tipo de *days* viendo solo el valor correcto. Siempre que el valor es un numero con un punto decimal, el tipo sera float64.

*Tip:* la herramienta golint provee pistas sobre estilo de codificacion. Este desaconseja el desbarajuste con el siguiente mensaje:
*Deberia omitir type float64 de la declaracion de var days; este sera inferido del lado derecho de la declaracion*

Si inicializas una variable con un numero entero. Go no conoce que quieres un punto flotante a menos que espefiques un tipo punto flotante.
```go
var answer float64 = 42
```
### 6.1.1 Numeros de punto flotante de precision simple
Go tiene 2 tipos de punto flotante. El tipo punto flotante por defecto es *float64*, un tipo punto flotante de 64 bit que usa 8 bytes de memoria. Algunos lenguajese usan el termino doble precision para describir tipos punto flotante de 64 bit

El tipo float32 usa la mitad de memoria de float64 pero ofrece menos precision. Este tipo algunas veces llamado de precision simple. Para usar *float32*, debes especificar el tipo cuando declaras la variable. La siguiente lista muestra el uso.
```go
var pi64 = math.Pi
var pi32 float32 = math.Pi
fmt.Println(pi64) // Imprime 3.141592653589793
fmt.Println(pi32) // imprime 3.1415927
```
Cuando trabajamos con una gran cantidad de datos, tales como miles de vertices en juegos 3D, Tiene sentido sacrificar precision por memoria haciendo uso de *float32*
*Tip:* Las funciones en el paquete math operan con float64, asi que el preferido es float64 a menos que haya buenas razones para hacer otra cosa.

### 6.1.2 El valor cero

En Go, cata tipo tiene un valor por defecto, llamado el *el valor cero*. Por defecto aplica cuando declaras una variable pero no la inicializas con un valor, como puedes ver en la siguiente lista.
```go
var price float64
fmt.Println(price) // Imprime 0
```
La lista previa declara *price* sin valor, asi que Go iniciliza con cero. Para la computadora es identico a usar
```go
price := 0.0
```
Para el programador, la diferencia es sutil. Cuando declaramos price := 0.0, es como decir que el precio es gratuito. No especificar un valor para el precio, como en el listado 6.2, esconde el valor que llegara a tener.

### 6.2 mostrando tipos punto flotante
Cuando usamos *Print* o *Println* con tipos punto flotante. el compartamiento por defecto es mostrar tantos digitos como sea posible. Si ni es lo que quieres puedes usar Printf con el verbo de formato *%f* para especificar el numero de digitos , como la lista muestra:
```go third := 1.0 / 3
fmt.Println(third)             // Imprime: 0.33333333333333333333333333
fmt.Printf("%v\n", third)      // Imprime: 0.33333333333333333333333333
fmt.Printf("%f\n", third)      // Imprime: 0.333333
fmt.Printf("%.3f\n", third)    // Imprime: 0.333
fmt.Printf("%4.2f\n", third)   // Imprime: 0.33
```
El verbo *%f* formatea el valor de *third* con un ancho con una posicion, como se muestra
```go
"%4.2f"   // 4 es el ancho, 2f representa la precision
```
La Precision especifica cuantos digitos deberian aparecer despues del punto decimal; los 2 digitos para %.2f, por ejemplo se muestra a continuacion
```go
*0.33*   // 0.33 es el ancho total, 33 es la precision de 2 digitos
```
Ancho especifica el numero minimo de caracteres a mostrar, incluyendo el punto decimal y los digitos antes y despues del decimal (por ejemplo 0.33 tiene un ancho de 4). Si el ancho es mas grande que el numero de caracteres necesarios. *Printf* pondra  al lado izquierdo espacios que sean necesarios. Si el ancho no es especificado, Printf usara el numero de caracteres necesarios para mostrar el valor.
las almohadillas izquierdas se pueden reemplazar con ceros en lugar de espacios, prefijando el ancho con cero, como se ven en la lista.
```go
fmt.Printf("%05.2f\n", third)  // Imprime: 00.33
```
### 6.3 Exactitud de punto flotante
En matematicas, algunos numeros racionales no pueden ser representados exactamente en forma decimal.
El numero 0.33 es solo una aproximacion de 1/3. No es de sorprender, que un calculo con valores aproximados tiene un resultado aproximado.
```go
1/3 + 1/3 + 1/3 = 1
0.33 + 0.33 + 0.33 = 0.99
```
Numeros de punto flotante sufren de errores de redondeo tambien, exeptuando el hardware de punto flotante usa una representacion binaria (usando solo 0s y 1s) en lugar de decimal (usa 1 - 9). La consecuencia es que las computadoras pueden representar exactamente 1/3 pero tienen errores de redondeo con otros numeros , tal como ilustra la lista.
```go
third := 1.0 / 3.0
fmt.Println(third + third + third)  // imprime: 1
piggyBank := 0.1
piggyBank += 0.2
fmt.Println(piggyBank)   // Imprime: 0.30000000000000000000004
```
Como puedes ver, punto flotante no es la mejor eleccion par representar dinero, Una alternativa es almacenar el numero en centavos con un tipo entero, que es cubierto en la siguiente leccion.

En la otra mano, incluso si tu *piggyBank* *were off* por un penique, bien, no es una mision critica. Asi como ahorraste suficiente para el viaje a marte,  eres feliz. Para barrer los errores de redondeo bajo la alfombra, puedes usar Printf con una precision de 2 digitos.

Para minimizar los errores de redondeo, recomentados que realices multiplicaciones antes que divisiones. El resultado tiende a ser mas exacto de esa forma, como se demuestra con los ejemplos de conversion de temperatura en las siguientes listas.
```go
// Division primero genera errores de redondeo 
celsius := 21.0
fmt.Print((celsius / 5.0*9.0) + 32, " F\n")    // Imprime 69.800000000000001 F
fmt.Print((9.0 / 5.0*celsius) + 32, " F\n")    // Imprime 69.800000000000001 F
```
```go
// Multiplicacion primero
celsius := 21.0
fahrenheit := (celsius * 9.0 / 5.0) + 32.0
fmt.Print(fahrenheit, " F")    // Imprime: 69.8 F
```
### 6.4 Comparando numeros de punto flotante
En la lista 6.5 el *piggyBank* contiene 0.30000000000000004, en lugar del deseado 0.30. Ten en mente esto que cada vez que necesites comparar numeros de punto flotante
```go
piggyBank := 0.1
piggyBank += 0.2
fmt.Println(piggyBank == 0.3)   // Imprime: false
```
En lugar de comparar numeros de punto flotante directamente, determine la diferencia absoluta entre los 2 numeros y entonces asegure que la diferencia no es tan grande. Para tomar el valor absoluto de un *float64*, el paquete *math* provee una funcion Abs:
```go
fmt.Println(math.Abs(piggyBank - 0.3) < 0.0001)  // Imprime: true
```
*Tip:* La cota superior para errores de tipo punto flotante para una sola operacion es conocido como epsilon de la maquina, que 2^-52 para *float64* y 2^-23 para *float32*. Desafortunadamente,  los erroes acumulativos de punto flotante crecen rapidamente. Adiciona 11 monedas ($0.10 cada uno) para un alcancia y redondea el error, excedera  2^-52 cuando comparamos a $1.10. que significa que es mejor escoger un limite especifico de tolerancia para tu aplicacion- en este caso. 0.0001.
