# GET READY, GET SET, GO

Go es un lenguaje contemporaneo de la computacion en la nube. Amazon, Apple, Canonical, Chevron, Disney, Facebook, General Electric, Google, Heroku, Microsoft, Twitch, Verizon, y Walmart son algunas de las companias que adoptan Go para proyectos serios. Mucha de la infraestructura de la web se hace en Go.

Go es excelente en centros de datos, sin embargo tambien es util para librerias para controlar robots y hardware. 

La comunidad de personas que han adoptado Go se llaman a si mismos gophers, en honor a la mascota de go. La programacion esta cambiando, pero con Go y este libro, esperamos descubrir la diversion de codificar.

En este leccion experimentaremos con el programa Go en tu navegador.

### Que es Go 
Go es un lenguaje de programacion compilado. Antes de ejecutar un programa, Go usa un compilador para traducir tu codigo a 1 y 0 que la maquina habla. Este compila tu codigo en un solo ejecutable para para correr o dsitribuir. Durante este proceso el compilador puede reconocer tipos y errores.

No todos los lenguajes empleando este enfoque. Python, Ruby, y otros varios lenguajes populares usan un interprete para traducir una sentencia a la vez cuando un programa esta corriendo. Esto significa que los bugs pueden tomar caminos que no han sido testeados.

En la otra mano, interpretes hacen el proceso de escribir codigo rapido e interactivo, con lenguajes que son dinamicos, sin mucho cuidado, y divertido. Lenguajes compilados tienen la reputacion de ser estaticos robots inflexibles que los programadores estan forzados a apaciguar, y los compiladores son ridiculizados por ser mas lentos.  Pero es necesario que sea de esta forma?

Go es manipulado con una gran trato de consideracion para la experiencia de escribir software. Grandes programas compilan en segundos con un solo comando. El lenguaje omiten caracteristicas que tratan la ambiguedad, con codigo que es predecible y facilmente entendible. Y go provee una alternativa ligera a las rigidas estructuras impuestas por los lenguajes clasicos como java.

Cada nuevos lenguajes de programacion refina ideas del pasado. En Go, usando la eficiencia de memoria es mas facil y menos propenso a errores que lenguajes anteriores,  y Go toma ventaja de maquinas de un nucleo o multinucleo. La mejora de eficiencia es una razon para cambiar a Go. Iron.io  fue capaz de reemplazar 30 servidores corriendo con ruby con 2 servidores usando Go.

Go provee la ventajas y facilidad de los lenguajes interpretados, con una ventaja de eficiencia y confiabilidad. Como un pequeno lenguaje, con solo unos pocos conceptos, es relativamente rapido de aprender. Estos tres principios forman parte del lema para Go:

- Go es una lenguaje de programacion de codigo abierto que permite la produccion de software a escala simple, eficiente, y confiable.

### Jugando con Go
La forma rapida de comenzar con Go es ir a play.golang.org. En este sitio se puede editar ejecutar y experimentar con Go sin necesitar de instalar nada. Cuando hacemos click en el boton run, el playground compila y ejecuta tu codigo en servidores de google y muestra el resultado. Si hacemos click en el boton Share, recibiremos un link con el codigo que escribiste. Puedes convertir el link con amigos al bookmark para salvar el codigo.

### Paquetes y funciones
Cuando visitas  el playground de Go, veremos el siguiente codigo, que es un buen punto de inicio
```go
package main // declara el paquete de el codigo debajo

import "fmt"  // Hace el paquete fmt (format) disponible para el uso

func main() { // Declara una funcion llamada main
    fmt.Println("Hello") // Imprime Hello, en la pantalla
}
```
Aunque corto, la lista precedente introduce tres palabras claves: package, import, y func. Cada palabra clave es reservada para un proposito especial.

La palabra clave package declara el paquete del codigo debajo, en este caso un paquete llamado main. Todo el codio en Go esta organizado en paquetes. Go provee un conjunto de paquetes para matematica, compresion, criptografia, manipulacion de imagenes, y mas. Cada paquete corresponde a una sola idea. 

La siguiente linea usa la palabra clave import para especificar paquetes que esete codigo usara.Paquetes contienen cualquier numero de funciones. Por ejemplo, el paquete math provee funciones como Sin, Cos, Tan y Sqrt. El paquete fmt usado aqui provee funciones para el formateado de entrada y salida. Mostrar texto en  la pantalla es una operacion frecuente, asi este paquete es abreviado como fmt. Gophers pronuncian fmt como "FOOMT!", asi aunque este esta escrito en letras grandes explosivas de un comic.

La palabra func declara una funcion, en este caso una funcion llamada main. El cuerpo de cada funcion esta encerrada con llaves. que es como Go sabe donde empieza y termina la funcion.

El identificador main es especial. Cuando ejecutas el programa escrito en Go, la ejecucion comienza con la funcion main en el paquete main. Sin main el compilador de Go reportara un error, porque no sabe donde comienza el programa.

Para imprimir una linea de texto, puedes usar la funcion Println. Println es prefijado con fmt seguido por un punto porque este es provisto por el paquete fmt. Cada vez que usas una funcion de un paquete importado , la funcion es prefijada con el nombre del paquete y un punto. Cuando leemos el codigo escrito en Go, el paquete de cada funcion queda inmediatamente claro.

Corre el programa en el playground de Go para ver el texto **Hello**. El texto encerrado entre comillas es llevado a la pantalla. En ingles, una coma incorrecta puede cambiar el significado de una sentencia. La puntuacion es importante en los lenguajes de programacion tambien. Go depente de comillas, parentesis y llaves para entender el codigo que escribes.

### 1.4 El estilo de una llave

Go es un poco exigente sobre el lugar de las llaves. En el listado 1.1, La llave de apertura esta en la misma linea de la palabra clave func, mientras que la llave de cierre esta solo en una linea. Este es **one true brace style**. 
Para entender porque  Go es tan estricto, necesitamos viajar atras en el tiempo  al nacimiento de Go. En esos dias, el codig estaba escrito con puntos y comas. No se podia escapar de ellos puntos y comas estan en una sola sentencia como un cachorro perdido.

En diciembre de 2009, un grupo de ninjas gophers eliminaro los puntos y comas del lenguaje. Bien, no exactamente. Realmente el compilador de Go inserta estas adorables puntos y comas por ti, y esto trabaja perfectamente. Perfectamente siempre que uses el estilo senalado antes.

Si omitimos el estilo el compilador de Go reportara un error de sintaxis.










