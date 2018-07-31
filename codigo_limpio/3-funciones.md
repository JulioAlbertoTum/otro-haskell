## Tamanio Reducido

La primera regla es que debe ser de tamanio reducido.
La segunda es que deben ser todavia mas reducidas.

Las lineas no deben tener mas de 150 caracteres, Las funciones deben tener la menor cantidad de lineas posibles 

### Bloques y Sangrado

Los bloques  if, else while deben tener una longitud que sea la invocacion de una funcion. De esta forma se reduce el tamanio ademas que se aniade valor argumental. Ademas las funciones no deben tener tamanios excesivos que tenga estructuras anidadas.Por tanto el nivel de sangrado no debe ser mayor que uno dos.

### Hacer una cosa

**Las Funciones solo deben hacer una cosa. Deben hacerlo bien o debe ser lo unico que hagan**

Si una funcion solo realiza los pasos situados un nivel por debajo del nombre de la funcion, entonces hace una cosa.

Otra forma de saber que una funcion hace mas de una cosa es extraer de la misma con un nombre que no sea una reduccion de su implementacion.

### Secciones en funciones 

Las funciones que hacen una sola cosa no se pueden divider en secciones.

### Un nivel de abstraccion por funcion

Asegurese que las instrucciones de la funcion esten en el mismo nivel de abstraccion. 

La mezcla de niveles de abstraccion siempre resulta confusa. Los lectores no sabran si una expresion es un concepto esencial o un detalle.

### Leer codigo de arriba a abajo la regla descendente

Queremos que tras todas las funciones apareceran las del siguiente nivel de abstraccion para poder leer el programa, descendiendo un nivel de abstraccion por vez mientras leemos la lista de funciones.  

### Instrucciones Switch

Es complicado escribir un switch de tamanio reducido, o que haga una sola cosa. Es mejor asegurarnos que esten en un nivel inferior y no repetirlas. 

La regla para las instrucciones switch es que pueden tolerar si solo aparecen una vez, se usan para crear objetos polimorficos y se ocultan tras una relacion de herencia para el resto del sistema.

### Usar nombres descriptivos 

Es necesario poner nombres adecuados para pequenas funciones que hacen una cosa. Cuando mas concreta sea una funcion, mas sencillo es elegir un nombre descriptivo. No le tema a los nombres extensos que son descriptivos.

### Argumentos de funciones 

Evite la presencia de tres o mas argumentos, a menos que sea estrictamente necesario.

Los argumentos son todavia mas complicados si se tratan de pruebas, si de todas las combinaciones que se generan y se deben verificar para garantizar el funcionamiento.

### Formas monadicas habituales

Las funciones que verifican algo, o que transforma una entrada en otra, son casos comunes. Otra forma menos habitual es el manejo de eventos. Elija nombres y  contextos con atencion. 

### Argumentos de indicador

Pasar un valor Booleano a una funcion es una practica totalmente desaconsejable. Complica la firma del metodo e indica que la funcion hace mas de una cosa.

### Funciones diadicas 

Aproveche todos los mecanismos posibles para convertirlas en unarias. En los casos en los que no se pueda evitar los argumentos deberian ser del mismo tipo o seguir algun orden.

### Triadas

Trate de evitarlas 

### Objeto de argumento

Cuando parezca necesitar mas de dos argumentos, es probable que alguno se incluya en una clase propia.
La reduccion del numero de argumentos mediante creacion de objetos puede parecer una trampa pero no lo es.

### Listas de argumentos

En ocasiones sera necesario pasar un numero variable de argumentos. Si se procesan de la misma forma sera equivalente a un unico argumento de tipo List. 

### Verbos y palabras clave 

La seleccion de nombres correctos para una funcion mejora la explicacion de su cometido asi como el orden y el cometido de los argumentos:
- Si son monadicos la funcion y el argumento deben formar un verbo y  un sustantivo.
- Asi mismo para mas argumentos se deberia buscar nombres que mitiguen el problema de tener que recordar el orden de los argumentos.

### Sin efectos secundarios 

Efectos secundarios son iguales a mentiras. Promete hacer una cosa, pero tambien hace otras ocultas. 

### Argumentos de salida

Por lo general, los argumentos de salida deben evitarse. si su funcion tiene que cambiar el estado de un elemento, haga que cambie el estado de su objeto contenedor.

### Separacion de consultas de comando

Las funciones deben hacer algo o responder a algo, pero no ambas. Esto genera instrucciones extranas como 
```php
if(set ("username", "tioBob"))
```
Es complicado saber lo que hace ya que el verbo set es un verbo o un adjetivo. Se podria cambiar el nombre pero no mejoraria la legibilidad de la instruccion if. La mejor solucion es separar el comando de la consulta.
```php
if (attributeExists("username")) {
	setAttribute("username", "tiobob");
	...
}
```
### Mejor Excepciones que devolver codigos de error

Devolver codigos de error de funciones de comando es un sutil incumplimiento de la separacion de comando de consulta. hace que los comandos asciendan a expresiones en los predicados de if
```php
if(deletePage(page) == E_OK)
```
Al devolver un codigo de error se crea un problema: el invocador debe procesar el error inmediatamente.

Por otro lado si, se usa excepciones en lugar de codigos de error, el codigo de error, el codigo de procesamiento del error se puede separar del codigo de ruta y se puede simplificar:
```java
try{
	deletePage(page);
	registry.deleteReference(page.name);
	configKeys.deleteKey(page.name.makeKey());
}catch( Exception e){
	logger.log(e.getMessage());
}
```
### Extraer bloques Try/Catch

Estos bloques confunden la estructura del codigo y mezclan procesamiento de errores con el normal. Por eso se debe extraer el cuerpo de los bloques try y catch en funciones individuales.

La separacion facilita la comprension y la modificacion del codigo.

### El procesamiento de errores es una cosa 

Una funcion que procese errores no debe hacer nada mas. Si una funcion incluye la palabre clave try, debe ser la primera de la funcion y no debe haber nada mas despues de los bloques catch/finally.

### El iman de dependencias Error.java

el usos de codigos de error implica que existe una clase o enumeracion que define los codigos de error.

Esta clase es un iman para las dependencias; por eso si cambia la enumeracion Error, es necesario volver a compilar las clases. Al usar excepciones las nuevas excepciones son derivaciones de la clase excepcion. por lo que no es necesario volver a compilar o implementar.

### No repetirse 

La duplicacion es un problema ya que aumenta el tamanio del codigo y requerira mayor modificacion si algo cambia en el codigo, lo que incrementa el riesgo de errores.

### Programacion Estructurada

En la programacion estructurada, las reglas indican que solo debe haber una instruccion return, no debe haber instrucciones break o continue en un bucle y nunca bajo ningun motivo una instruccion goto.

El verdadero beneficio del a programacion estructurada se aprecia en funciones de gran tamanio.

### Como crear este tipo de funciones 

La primera vez que se crean funciones esta pueden ser extensas y complicadas, con abundancia de sangrados y bucles anidados. Con extensas listas de argumentos, nombres arbitrarios y codigo duplicado.

Posteriormente podemos retocar el codigo, dividiendolo en funciones, cambiamos nombres y eliminamos duplicados. 

Al final obtendremos funciones que cumplan las reglas detalladas descritas aqui.













































































































































































