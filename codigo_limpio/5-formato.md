# COMENTARIOS

El formato del codigo es muy importantes es una carta de presentacion sobre quienes crearon el codigo.

El formato del codigo debe cuidarse con "reglas sencillas" que se apliquen de forma coherente. Tambien es posible usar una herramienta que se encargue de aplicar las reglas.

### La funcion del formato

La legibilidad del codigo afectara profundamente a todos los cambios que realice sobre el codigo en un futuro. La capacidad de mantenimiento depende profundamente de esto. Los aspectos del formato que nos ayudaran son:

#### Formato vertical

Se refiere la tamano del archivo fuente. Por ejemplo en java se pueden crear sistemas con archivos de 200 lineas, con un limite maximo de 500. No es una regla pero si un limite aconsejable.

#### La metafora del periodico

Un archivo debe se como un articulo de periodico. El nombre debe ser claro y sencillo. Los elementos superiores deben indicarnos conceptos de algoritmos de nivel superior. Los detalles deben aumentar a medida que avanzamos, hasta que al
final encontremos las funciones de nivel  inferior.

#### Apertura vertical entre conceptos

El codigo se lee de izq a der, de arriba hacia abajo. Cada linea representa una expresion o una clausula, y cada grupo de lineas representa un pensamiento completo. Los pensamientos se separan por lineas en blanco.

#### Densidad vertical 

La densidad vertical implica asociaciones. Las lineas de codigo con relacion directa deben aparecer verticalmente densas.

#### Distancia vertical

Conceptos relacionados entre si debel permanecer verticalmente juntos. Por tanto no debe separar conceptos relacionados en archivos independientes a menos que tenga un motivo de peso. Para conceptos relacionados en un mismo archivo. la separacion verticla debe medir su importancia con respeco a la legibilidad del otro.

#### Declaracion de variables 

Las variables deben declararse de la forma mas aproximada a su uso. En funciones deben aparecer en la parte superior de cada funcion.

Las variables de control (ej. contadores, flags) deben declararse en la instruccion del bucle.

En casos excepcionales una variable se declara en la parte superior de un bloque o antes de un bucle en una funcion extensa.

#### Variables de instancia 

Las variables de instancia deben declararse en la parte superior de la clase. Esto no de aumentar la distancia vertical de las variables ya que en una clase  bien disenada se usan en muchos si no en todos sus metodos.

En C++ se suelen declarar en la parte inferior, lo importante es definirlas en un punto conocido.

#### Funciones de dependientes

Cuando **una funcion invoca otra deben estar verticalmente proximas**, y la funcion de invocacion debe estar por encima de la invocada siempre que sea posible.

#### Afinidad Conceptual 

De acuerdo a la afinidad conceptual de codigo, la distancia vertical deberia ser menor. La afinidad  tambien puede generarse  porque las funciones realicen una operacion similar.

#### Orden vertical

Por lo general, las dependencias de invocaciones deben apuntar hacia abajo. Es decir la funcion invocada debe situarse por debajo de la que realice la invocacion. 

#### Formato Horizontal

Lo mejor es reducir las lineas de codigo. con un maximo de 100 a 120 pero no mas.

#### Apertura y densidad Horizontal

Usamos espacios horizontales para asociar elementos relacionados y separa otros con una relacion menos estrecha. un espacion en los argumentos nos sugiere que los mismos son independientes y ademas acentuamos la coma (ej hola(nombre, apellido))

#### Alineacion Horizontal

En ensamblador quiza resulte util sin embargo en otros este tipo de alineacion no es util. por lo que es mejor no alinearlas.

#### Sangrado

Un archivo de codigo es una jerarquia mas que un contorno. Incluye informacion que pertenece a la totalidad del archivo, a sus clases individuales, a los metodos de las clases, a los bloques de los metodos y a los bloques de los bloques. Cada nivel es una jerarquia o un ambito.

Esta jerarquia es visible mediante el sangrado del codigo fuente, las instrucciones a nivel de archivo asi como las clases no se sangran. los metodos se sangran un nivel a la derecha, las implementaciones de dichos metodos tambien respecto al metodo, asi mismo los bloques respecto a su bloque contenedor.

#### Romper el sangrado

Es mejor evitar replegar ambitos a una linea (ej function hola() { return hola }), lo mejor es respetar el sangrado.

#### Ambitos ficticios

En ocasiones el cuerpo de una instruccion while o for es ficticio. Es mejor evitar estas. Si no se puede evitar lo que se hace es sangrar el cuerpo ficticio.
```java
while(dis.read(buf, 0, readBufferSize) != 1)
	;
```

####Reglas de equipo

Un equipo de programadores debe acordar un unico estilo de formato y todos los integrantes del equipo deben aplicarlo, para que el software tenga un estilo coherente.

Las reglas del equipo estan por encimas de las preferencias individuales.













































































