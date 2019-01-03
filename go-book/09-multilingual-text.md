Desde el principio, has estado usando textoen tus programas. Las letras individuales, digitos, y simbolos son llamados caracteres. Cuando tu string junta caracteres y los coloca juntos entre comillas, este es llamado "literal string".

## 9.1 Declarando variables String
Valores literales envueltos entre comillas son inferidos para ser del tipos *String*, asi las siguientes tres lineas son equivalentes:
```go
peace := "peace"
var peace = "peace"
var peace string = "peace"
```
Si declaramos una variable sin proveer un valor, este se inicializara con el valor cero para su tipo. El *valor cero* para el tipo *String* es una cadena *vacia* (""):
```go
var blank string
```
### 9.1.1 String Literales Crudos (Raw)
String literales pueden contener *secuencias de escape*, tal como *\n* mencianada en la leccion 2. Para evitas sustituir *\n* para una nueva linea, puedes envolver el texto con las comillas inversas (backticks) (`) en lugar de las comillas ("),  como se ve en la siguiente lista. Backticks indican una raw string literal.
```go
fmt.Println("la paz sea contigo\nque tengas paz")
fmt.Println(`strings pueden tener multiples lineas usando \n como secuencia de escape`)
```
La lista previa tiene la siguiente salida
```go
la paz sea contigo 
que tengas paz 
strings pueden tener multiples lineas usando \n como secuencia de escape
```
A diferencia de los string literales convencionales, los raw string literales pueden spanear multiples lineas de codigo fuente, como se muestra en la siguiente lista.
```go
fmt.Println(`
    la paz sea contigo
    que tengas paz`)
```
Ejecutando el codigo 9.2 producira la siguiente salida, incluyendo los tabs usados para la indentacion:
```go
   la paz sea contigo 
   que tengas paz
```
String literales y strings raw ambos resultan en strings, como se ve en la siguiente lista.
```go
fmt.Printf("%v es una %[1]T\n", "string literal") // imprime string literal como un string
fmt.Printf("%v es una %[1]T\n", `raw string literal`) // Imprime un raw string como un string
```
### 9.2 Caracteres, puntos codigo, runes, y bytes 
El consorcio Unicode asigna valores numericos, llamados puntos codigo *code points*, por sobre un millon de caracteres unicos. Por ejemplo, 65 es el punto codigo para la letra mayuscula A, y 128515 es una pequena cara de sonrisa.
Para representar un solo punto de codigo Unicode, Go provee *rune*, que es un alias para el tipo *int32*.

Un byte es un alias para el tipo *uint8*. Esta entendido para datos binarios, aunque *byte* puede ser usado para caracteres en ingles definidos por ASCII, y viejos subconjuntos de 128 caracteres.
*Tipo Alias: * Un alias es otro nombre para el mismo tipo, asi rune y int32 son intercambiables. Aunque byte y rune han estado en Go desde el principio, Go 1.9 introduce la habilidad para declarar su propio tipo alias. La sintaxis luce como:
```go
type byte = uint8
type rune = int32
```
Ambos *byte* y *rune* se comportant como tipos enteros ellos son tios alias, como se muestra en la siguiente lista.
```go
var pi rune = 960
var alpha rune = 940
var omega rune = 969
var bang byte = 33
fmt.Printf("%v %v %v %v\n", pi, alpha, omega, bang)
// imprime: 960 940 969 33
```
Para imprimir los caracteres en lugar sus valores numericos, el verbo de formato %c puede ser usado con Printf:
```go
fmt.Printf("%c%c%c%c\n", pi, alpha, omega, bang)  
```
*Tip: * Cualquier tipo entero trabajara con %c, pero el alias rune indica que el numero 960 representa un caracter.

En lugar de memorizar los puntos de codigo Unicode, Go provee un caracter literal. Solo encierra un caracter en comillas simples 'A'. Si ningun tipo es especificado, Go inferira el tipo rune, asi que las siguientes 3 lineas son equivalentes:
```go
grade := 'A'
var grade = 'A'
var grade rune = 'A'
```
La variable *grade* todavia contiene un valor numerico, en este caso 65, el punto codigo pora una letra mayuscula 'A'. Los caracteres literales pueden tambien ser usados con el alias *byte*: 
```go
var star byte = '*'
```
### 9.3 Traccion de strings
Un marionetista manipula una marioneta (by pulling on strings), pero strings en Go. No son susceptibles de manipulacion. Una variable pueden ser asignados a un string diferente, pero los strings en si mismos no pueden ser alterados:
```go
peace := "shalom"
peace = "salam"
```
Tu programa puede acceder a un caracter individual, pero este no puede alterar los caracteres de un string. La siguiente lista usa corchetes para especificar un indice dentro de un string, que accede a un solo byte (caracter ASCII). El indice comienza con cero.
```go
message := "shalom"
c := message[5]
fmt.Printf("%c\n", c) // Imprime m
```
Strings en Go son inmutables, asi son en Python, Java, y Javascript. A diferencia de los strings en Ruby y array de caracteres en C, no puedes modificar un string en Go:
```go
message[5] = 'd' // no pude ser asignado a message[5]
```
### 9.4 Manipulando caracteres con cifrado Cesar
Un metodo efectivo de enviar mensajes secretos en el siglo 2 fue cambiar todas las letras, asi 'a' llegara a ser 'd', 'b' sera 'e', etc. El resultado deberia parecer un lenguaje extranjero.

Para realizar la manipulacion de caracteres como valores numericos es realmente facil con las computadoras, como se muestra en la siguiente lista.
```go
c := 'a'
c = c + 3
fmt.Printf("%c", c)  // imprime d
```
El codigo en la lista tiene un problema, aunque.Este no cuenta para todos los mensajes sobre xilofonos, jacks y cebras.Para esto es necesario el original cifrado cesar alrededor asi 'x' llegara a ser 'a', 'y' llegara a ser 'b' y 'z' llegara a ser 'c'. Con 26 caracteres en el alfabeto Ingles, hay una simple forma
```go
if c > 'z' {
    c = c - 26
}
```
Para decifrar el cifrado cesar , substrae 3 en lugar de adicionar 3. Pero cuando necesitemos contar para c < 'a' adicionaremos 26. 

### 9.4.1 Una variante moderna
ROT13 (rotar 13) es una variante el siglo 20 del cifrado cesar. Este adiciona 13 en lugar de 3. con ROT13, cifrado y descifrado son usan la misma operacion conveniente.

Permitenos suponer que mientas escaneamos las comunicaciones de aliens en el cielo, Si el instituto SETI recibe una transmision con el siguiente mensaje.
```go
message := "uv vagreangvbany fcnpr fgngvba"
```
Sospechamos que el mensaje esta realmente ingles cifrado con ROT13. Llamemos a esto una corazonada. Antes de crackear el codigo, hay una cosa mas que debemos conocer. Este *message* tiene una longitud de 30 caracteres, que puede ser determinado con la funcion len:
```go
fmt.Println(len(message)) // Imprime 30
```
*Note :* Go tiene un conjunto muy util de funciones que no requieren de sentencias de importacion. La funcion len puede determinar la longitud de una variedad de tipos. En este caso, len retorna la longitud de un string en bytes.

La siguiente lista decifrara un mensaje desde el espacio. Si ejecutamos en el playground Go para encontrar lo que los aliens estan diciendo.
```go
message := "uv vagreangvbany fcnpr fgngvba"
  for i:= 0; i < len(message); i++ { // itera atraves de cada caracter ASCII
    c := message[i]
    if c >= 'a' && c <= 'z' { // adiciona espacios y signos de puntiacion
      c = c + 13
      if c > 'z' {
        c = c - 26
      }
    }
    fmt.Printf("%c", c)
  } 
```
Note qoe la implementacion en la lista previa es solo para caracteres (bytes) ASCII. Esto sera confuso para mensajes escritos en espanol  o ruso. La siguiente seccion muestra una solucion a este problema.

### 9.5 Decodificando Strings dentro de runes
Strings en Go son codificados con UTF-8, uno de varios codificadores para puntos de codigo Unicode. UTF-8 es una codificacion de longitud variable donde un solo punto de codigo puede usar 8, 16 o 32 bits. Para usar una codificacion de longitud variable, UTF-8 hace la transicion de ASCII facil, porque ASCII caracteres son indenticos a sus contrapartes codificadas en UTF-8.
*Note: * UTF-8 es el codificado de caracteres dominante para la WWW. Este fue inventado en 1992 por Ken Thompson, uno de los disenadores de Go.

El programa ROT13 listado accede a bytes individuales (8-bit) del string *message* son contar con  caracteres con multiples bytes de longitud  (16-bit o 32-bit) Esto es porque trabaja bien para caracteres en ingles (ASCII), pero produce resultados ilegibles para Ruso y espanol. Puedes hacerlo mejor *amigo*.

El primer paso para soportar otros lenguajes es decodifivar los caracteres al tipo *rune* antes de manipularlos. Afortunadamente, Go tiene funciones y caracteristicas del lenguaje para decodificar cadenas codificadas en UTF-8.

El paquete *utf-8* provee funciones para determinar la longitud de una string en runes en lugar bytes y para decodificar el primer caracter de un string. la funcion *DecodeRuneString* returna el primer caracter y el numero de bytes que el caracter consume, como se muestra en la lista.
*Nota: * A diferencia de muchos lenguajes de programacion, las funciones en Go pueden retornar multiples valores. Retorno de multiples valores se veran el la leccion 12.
```go
import (
    "fmt"
    "unicode/utf8"
)

func main() {
  question := "¿Cómo estás?"
  fmt.Println(len(question), "bytes")  // Imprime: 15 bytes
  fmt.Println(utf8.RuneCountInString(question), "runes") // Imprime: 12 runes
  c, size := utf8.DecodeRuneInString(question)
  fmt.Printf("First rune: %c %v bytes", c, size) // Imprime: First rune: ¿ 2 bytes
}
```
El lenguaje Go provee la palabra clave *range* para iterar sobre una variedad de colecciones (cubierto en la unidad 4). Este puede tambien decodificar  cadenas codificadas en UTF-8, como se muestra en la siguiente lista.
```go
question := "¿Cómo estás?"

for i, c := range question {
    fmt.Printf("%v %c\n", i, c)
}
```
En cada iteracion, las variables i y c son asignadas a un indice dentro el string y el punto codigo (rune) para esta posicion.

Si no necesitamos los indices, el identificador en blanck (underscore) te permitira ignorarlo:
```go
for _, c := range question{
    fmt.Printf("%c ", c) // Imprime: "¿Cómo estás?"
}
```
 
