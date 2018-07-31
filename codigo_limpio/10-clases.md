### Organizacion de las Clases

Segun convenciones como la de java una clase comienza con una lista de variables. Las constante estaticas publicas son primero. Despues las variables estaticas privadas y despues las variables de instancia privadas. 

A continuacion las funciones publicas, esto permite la norma descendente y permite que el programa se lea como un articulo.

### Encapsulacion

Es deseable que las variables y funciones de utilidad sean privadas. La regla manda que su una regla del mismo paquete tiene que invocar una funcion y acceder a una variable, hacemos que tenga ambito protected o de paquete.

### Las clases deben ser el de tamano reducido

- Primera regla es que sean de tamanio reducido.
- Segunda regla es que deben ser todavia mas reducidos.

La pregunta es que nivel de reduccion. En las clases la medida son **Las responsabilidades** 

Por lo general una clase con muchos metodos (mas de 30 o 40) se conoce como clase Dios y muestra sintomas como el de tener demasiadas responsabilidades.

El nombre de una clase debe describir las responsabilidades. Si no podemos derivar un nombre conciso para una clase es probable que sea muy extenso. Por ejemplo Processor, Manager o Super  suelen indicar este problema. Tambien deberia ser posible describir la clase sin usar las palabras **si, o, pero** 

### El Principio de responsabilidad unica

El principio de responsabilidad unica indica una clase o modulo debe tener uno y solo un motivo para cambiar. 

SRP es uno de los conceptos mas importantes del diseno orientado a objetos y tambien uno de los mas sencillos de entender y cumplir, pero tambien es uno de los que mas se abusa al disenar clases. 

Software que funcione y software limpio son cosas muy diferentes. Muchos programadores temen que un elevado numero de pequenas clases con un unico proposito dificulten la comprension del conjunto. Les preocupa que tengan que desplazarse entre las clases para determinar como funciona un aspecto concreto.

La pregunda es si quiere organizar sus herramientas en cajas con muchos pequenos cajones que contengan componentes bien definidos y etiquetados, o usar varios cajones grandes en los que mezcle todo.

Los sistemas deben estar formados por muchas claves reducidas, no por algunas de gran tamanio. Cada clase reducida encapsula una unica responsabilidad, tiene un solo motivo para cambiar y colabora con algunas otras para obtener los comportamientos deseados del sistema.

### Cohesion
Las clases deben tener un numero minimo de variables de instancia. Los metodos de una clase deben manipular una o varias de dichas variables. Por lo general, cuantas mas variables manipule un metodo, mas cohesion tendra con su clase. 

Una clase en la que cada variable se usa en cada metodo tiene una cohesion maxima. Por lo general no es posible y recomendable crear este tipo de clases.

La estrategia de reducir el tamanio de las funciones y de las listas de parametros suele provocar proliferacion de variables de instancia usadas por un subjconjunto de los metodos. si esto sucede intente separar las variables y metodos en dos o mas clases para que las nuevas sean mas consistentes.

### Mantener resultados consistentes en muchas clases de tamanio reducido

La division de grandes funciones en otras mas pequenas aumenta la proliferacion de clases.

Por lo general cuando hacemos metodos mas pequenos perdemos cohesion ya que tienden a acumular mas y mas variables de instancia que solo existen para  que las funciones las compartan. Cuando las clases pierdan conhesion dividalas.

Dividir una gran funcion en otras mas reducidas tambien nos permite dividir varias clases mas reducidas, de esta forma mejora la organizacion del programa y su estructura resulta mas transparente.

ver pag 178

### Organizar los cambios 

En muchos sistemas el cambio es continuo. Cada cambio supone un riesgo de que el resto del sistema no funcione de la forma esperada. En un sistema limpio organizamos las clases para reducir los riesgos de los cambios.

ver pag 182

Las clases deben cumplir un principio denominado **Principio abierto/cerrado** las clases deben abrirse para su ampliacion para cerrarse para su modificacion. 

Debemos estructurar nuestros sistemas para ensuciarlos lo menos posible cuando los actualicemos con nuevas funciones o cambios. En un sistema ideal, incorporamos nuevas funciones ampliandolo, no modificando el codigo existente.

### Aislarnos de los cambios

Las necesidades cambiaran y tambien lo hara el codigo. En POO hay clases concretas que contienen detalle de implementacion (el codigo). y clases abstractas que solo representan conceptos.Una clase cliente que dependa de detalles concretos esta en peligro si dichos detalles cambian. Podemos recurrir a interfaces y clases abstractas para aislar el impacto de dichos detalles.

Las dependencias de detalles de concretos crean retos para nuestro sistema. A la eliminacion de conexiones, las clases tienden a cumplir otro principio de diseno:
**Dependency Inversion Principle (DIP)** o principio de inversion de dependencias. Afirma que nuestras clases deben depender de abstracciones, no de detalles concretos.

 















