En las lecciones previas cubren booleanos, cadenas, y una docena de diferentes tipos numericos. Si tienes variables de diferentes tipos, debes convertir los valores en el mismo tipo antes de poder usarlos juntos.

### 10.1 Tipos no se mezclan

Una tipo de variable establece el comportamiento que es apropiado para este. Los numeros pueden  ser adicionados, las cadenas pueden ser concatenadas. Para concatenar dos cadenas, usa el operador suma.
```go
countdown := "Lanzamiento en T menos " + "10 segundos."
```
Si tratas de concatenar un numero a una cadena, el compilador de Go reportara un error.
```go
countdown := "Lanzamiento en T menos " + 10 + " segundos." // operacion invalida
```
Otro ejemplo de mal muestreo de tipos ocurre cuando intentamos calculo con una mezcla tipos enteros y flotantes. Numeros reales como 365.2425 son representados con un tipo de punto flotante, en Go se infiere que los numeros enteros son integers.
```go
age := 41
marsDays := 687
earthDays := 365.2425
fmt.Println("I am",age*earthDays/marsDays, "years old on Mars.")
```
Si todas las variables fueran enteras, los calculos serian exitosos, pero entonces *earthDays* deberia ser 365 en lugar del mas preciso 365.2425. Alternativamente, los calculos deberian ser mas exitosos si *age* y "marsDays" serian del tipo punto flotante (41.0 y 687.0 respectivamente). Go no puede asumir directamente que es  lo que se prefiere, pero puedes convertir explicitamente  entre tipos, que se cubre en la siguiente seccion.

### 10.2 Conversion de tipos Numericos
La conversion de tipos es muy facil, Si necesitas que el entero *age* sea un de punto flotante para realizar un calculo, envuelve la variable con el nuevo tipo.
```go
age := 41
marsAge := float64(age)
```
Variables de diferentes tipos no se mezclan, pero con la conversion de tipos, el calculo en la siguiente lista trabaja.
```go
age := 41
marsAge := float64(age)

marsDays := 687.0
earthDays := 365.2425
marsAge = marsAge * earthDays / marsDays
fmt.Println("I am", marsAge, "years old on Mars.")
```
Puedes convertir de un tipo de punto flotante a un entero tambien, aunque los digitos despues  del punto decimal seran truncados sin hacer redondeo:
```go
fmt.Println(int(earthDays)) // imprime: 365
```
La conversion de tipos son requeridos entre tipos de enteros con signo y sin signo, y entre tipos de diferentes tamanios. Esto es siempre seguro convertir a un tipo con un rango mas grande, tal como *int8* a un *int32*. Otra conversion de enteros viene con riesgos. Un int32 podra contener un valor de 4 billones, pero un int32 solo soporta numeros de hasta 2 billones. Asi tambien, un *int* puede contener un numero negativo, pero un *uint* no puede.

Ahi la razon de porque Go requiere que la conversion de tipos sea explicita en el codigo. Cada vez que usas un tipo de conversion, considera las posibles consecuencias.

### Convierte tipos con precaucion 
En 1996, el cohete no tripulado Arianne se salio de su recorrido, rompiendose y explotando, solo 40 segundos despues del lanzamiento. La causa reportada fue un error de conversion de tipo desde un float64 a un int16 con un valor que excede 32.767 - el maximo  valor que *int16* puede guardar. La falla afecto al sistema de control de vuelo dejando sin datos de orientacion, causando el fuera de curso, rompiendo el apartado, y en ultimo la autodestruccion.

Nosotros no vimos el codigo del Arianne 5, no somos cientificos de cohetes, pero permitenos ver como Go manejaria la misma conversion de tipos. Si el valor esta en rango, como en la siguiente lista, no habra problemas.
```go
var bh float64 = 32767
var h = int16(bh)
fmt.Println(h)
```
Si el valor de bh es 32,768, que es tan grande para un *int16*, el resultado que esperaremosde los enteros en Go: este envuelve a este, llegando a ser un numero menor posible para un int16, -32768.

El lenguaje ADA  usado en el Arianne 5 se comportade de manera diferente. La conversion de tipos de float64 a int16 con un valor fuera de rango causo una excepcion en el software. De acuerdo al reporte, este particular calculo era solo significativo antes del despegue, asi que el enfoque en go pudo haber sido mejor en esa instancia, pero usualmente es mejor evitar datos incorrectos.

Para detectar si la conversion de un tipo int16 resultara  en un valor invalido.

Para detectar si convertir un tipo a int16 resultara en un valor invalido el paquete math provee constantes min/max
```go
if bh <  math.MinInt16 || bh > math.MaxInt16 {
    // manejamos los valores fuera de rango
}
```
*Nota: * Las constantes min/max  no tienen tipo, permitiendo la comparacion de bh, con un valor de punto flotante, a MaxInt16. La leccion B habla mas de constantes sin tipo.

### 10.4 Conversion de Strings
Para convertir un *rune*a un *string*, puedes usar la misma sintaxis de conersion de tipo como las conversiones numericas, que se muestran en la siguiente lista. Se da el mismo resultado usando el verbo de formato %c introducido en la leccion 9 para mostrar runes en bytes como caracteres.
```go
var pi rune = 960
var alpha rune = 940
var omega rune = 969
var bang byte = 33
fmt.Print(string(pi), string(alpha), string(omega), string(bang))
```
Convirtiendo un codigo numerico puntual a un string trabaja de la misma forma con cualquier otro tipo entero. Despues de todo, *rune* y *byte* son solo alias para *int32* y *uint8*.

Para convertir digitos a un *string*, cada digito debe ser convertido a un punto codigo, comenzando por 48 para el caracter 0, hasta el 57 para el caracter 9. Afortunadamente la funcion *Itoa* en el paquete *strconv* hace esto por ti.
```go
countdown := 10
str := "Lanzado en T minus " + strconv.Itoa(countdown) + " seconds."
fmt.Println(str) 
```
*Nota:* Itoa es corta para  enteros ASCII, Unicode es un superconjunto del viejo standard ASCII. El primer punto codigo 128 son lo mismo, que incluye digitos (usados aqui), Letras en Ingles, y signos de puntuacion comunes.

Otra forma de convertir un numero a un string es usar Sprintf, un primo de Printf que retorna un string en lugar de mostrar este:
```go
countdown := 9
str := fmt.Sprintf("Lanzamiento en T minus %v seconds.", countdown)
fmt.Println(str) 
```
Si vamos de otra forma, el paquete *strconv* provee la funcion *Atoi*  (ASCII a entero). Porque un string puede contener "gibberish" o un numero que es tambien grande, la funcion *Atoi* puede retornar un error:
```go
countdown, err := strconv.Atoi("10")
if err != nil {
    // codigo si algo sale mal
}
fmt.Println(countdown)  // Imprime 10
```
Un valor *nil* para err indica que no hay error ocurrida y todo esta bien. Leccion 28 trata el topico de errores.

### 10.5 Convertir valores Booleanos
La familia de funciones *Print* muestra los valores booleanos *true* y *false* como texto. Tal es asi, la siguiente lista usa la funcion Sprintf para convertir la variable Booleana *launch* al texto. si quieres convertirlos valores numericos a textos diferentes, un humilde sentencia *if* trabaja bien.
```go
launch := false
launchText := fmt.Sprintf("%v", launch)
fmt.Println("Ready for launch:", launchText) // Imprime: Ready for launch:false

var yesNo string
if launch {
    yesNo = "yes"
} else {
    yesNo = "no"
}
fmt.Println("Listo para lanzar:", yesNo) // Imprime: Readyfor launch: no
```
La conversion inversa  requiere menos codigo porque puedes asignar el resultado de una condicion directamente a una variable, como en la siguiente lista.
```go
yesNo := "no"

launch := (yesNo == "yes")
fmt.Println("Ready for launch:",launch) // Imprime: Ready for launch: false
```
El compilador de Go reportara un error si intentas convertir un Booleano con *string(false), int(false)*, o similar, e igualmente *bool(1)* o *bool("yes")*.

*Nota:* En lenguajes de programacion sin un tipo bool dedicado, los valores 1 y 0 a menudo son equivalentes a true y false, respectivamente. Boolenos en Go no tienen un equivalente numerico.


