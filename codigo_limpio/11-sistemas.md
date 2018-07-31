### Como construir una ciudad

Sera posible hacerlo solo, es complicado. Pero como funciona realmente, la clave es que existen equipos que controlan partes concretas de la ciudad.

Ademas las ciudades disponen de evolucionados niveles de abstraccion y modularidad que permite a individuos y componentes trabajar de forma eficaz, sin necesidad de entender el transfondo general.

Veremos como mantener la limpieza en niveles superiores de abstraccion, en el sistemas.

### Separar la construccion de un sistema de uso 

Los sistemas deben separar el proceso de inicio, en el que se crean los objetos de la aplicacion y se conectan las dependencias, de la logica de ejecucion que toma el testigo tras el inicio.

La separacion de aspectos es una tecnica de diseno mas antiguas e importantes. Muchas veces el proceso de inicio se mezcla con la logica de tiempo de ejecucion.

Un caso de inicializacion tardia no es un problema serio. Pero suele haber muchos casos de este tipo de configuracion en las aplicaciones. Por lo que la estrategia de configuracion se disemina por la aplicacion, restando modularidad e incrementando duplicacion.

No debemos permitir fallos de modularidad. Debemos modularizar el proceso de inicio y conexion y asegurarnos de contar con una estrategia global para resolver las depedencias principales.

### Separar Main
Una forma de separar la construccion del uso consiste en trasladar todos los aspectos de construccion a main o a modulos invocados por main, y disenar el resto del sistema suponiendo que todos los objetos sen han creado y conectado correctamente.

El flujo de control es facil de seguir. la funcion main crea los objetos necesarios y lso pasa a la aplicacion y esta los utiliza. 

### Factorias 
En ocasiones la aplicacion tendra que ser responsable de la creacion de un objeto. Por ejemplo en un sistema de procesamiento de pedidos. En este caso podriamos usar el patron de factoria abstracta para que la aplicacion controle cuando crear un item, pero mantener los detalles de  construccion separados del codigo de la aplicacion.

### Inyectar Dependencias
Un potente mecanismo para separar la construccion del uso, es la Inyeccion de dependencias, la aplicacion de Inversion de Control (Inversion fo Control o IoC) a la administracion de dependencias. La inversion de control pasa responsabilidades secundarias de un objeto a otros dedicados a este cometido, por lo que admite el principio de responsabilidad unica. en el contexto de la administracion de dependencias, un objeto no debe ser responsable de instanciar dependencias, si no que debe delegar esta responsabilidad en otro mecanismo autorizado, de modo que se invierte el control. 

La verdadera inyeccion de dependencias va un paso mas alla. La clase no hace nada directamente para resolver las dependencias, es totalmente pasiva. Ofrece metodos de establecimiento o argumentos de constructor (o ambos) que se usan para inyectar dependencias. En le proceso de construccion, el contenedor de inyeccion de dependencias crea instancias de los objetos necesarios y usa los argumentos de constructor o metodos de establecimiento proporcionados para conectar las dependencias.  Los objetos dependientes empleados suelen especificarse a traves de un archivo de configuracion o mediante programacion en un modulo de construccion de proposito especial.

Muchos contenedores de inyeccion de dependencias no crean objetos hasta que es necesario. 

### Evolucionar 
Debemos implementar hoy, y refactorizar y ampliar manana. Es la esencia de la gildiad iterativa e incrementar. El desarrollo controlado por pruebas, la refactorizacion y el codigo limpio que generan hace que funcione a nivel del codigo.

Los sistemas de software son unicos si los comparamos con los sistemas fisicos. Sus arquitecturas pueden crecer incrementalmente, si mantenemos la correcta separacion de los aspectos.

### Aspecto Transversales
En principio, puede razonar su estrategia de persistencia de una forma modular y encapsulada, pero en la practica tendra que distribuir el mismo codigo que implemente la estrategia de persistencia entre varios objetos. Usamos el termino transversales para este tipo de aspectos. De nuevo la estructura de persistencia podria ser modular  y la logica de dominios, aislada, tambien. El problema es la interseccion entre ambos dominios.

### Proxies de Java
Son utiles en casos sencillos, como envolver invocaciones de metodos en objetos o clases concretas. Sin embargo, los proxies dinamicos proporcionados en el JDK solo funcionan con interfaces.

ver pag 196

Los proxies dificultan la creacion de codigo limpio. 

### Estructuras AOP Java puras
Una herramienta mas de Java
Ver libro
### Aspectos de AspectJ
La herramienta mas completa de separacin a traves de aspectos es el lenguaje AspectJ,  que es una extension de java.
Ver libro
### Pruebas de unidad de la arquitectura del sistema
La separacion a traves de enfoques similares a aspectos no se puede menospreciar.
Su poeude crear la logica de dominios de su aplicacion mediante POJO, sin conexion con los aspectos arquitectonicos a nivel de codigo, entonces podra probar realmente la arquitectura.
No es necesario crear un Buen Diseno por adelantado. De hecho puede ser negativo ya que impide la adaptacion al cambio, debido a la resistencia fisiologica a descartar esfuerzos previos y la forma en que las decisiones arquitectonicas influyen en la concepcion posterior del diseno.

Podemos iniciar un proyecto  de software con una arquitectura simple pero bien desconectada, y ofrecer historias funcionales de forma rapida, para despues aumentar la infraestructura. 

Una arquitectura de sistema optima se compone de dominios de aspectos modularizados, cada uno implementado con POJO. Los distintos dominios se integran mediante aspectos o herramientas similares minimamente invasivas. Al igual que en el codigo, en esta arquitectura se pueden realizar pruebas.

### Optimizar la toma de decisiones
Lo modularidad y separacion de aspectos permite la descentralizacion de la administracion y la toma de decisiones. En un sistema sufientemente amplio, ya sea una ciudad o un proyecto de software, no debe haber una sola persona que adopte todas las decisiones.

Sabemos que conviene delegar responsabilidades  en las personas mas cualificadas. Tambien es conveniente posponer decisiones hasta el ultimo momento. De forma que se pueda tomar decisiones con la mejor informacion posible. Una decision prematura siempre es subjetiva. 

La agilidad que proporciona un sistema POJO con aspectos modularizados nos permite adoptar decisiones optimas a tiempo, basadas en los conocimientos mas recientes. Ademas, se reduce la complejidad de estas decisiones.

### Usar estandares cuando anadan un valor demostrable
Hay equipos obsesionados con estandares de moda y que se olvidaron de implementar el valor para sus clientes.

Los estandares facilitan la reutilizacion de ideas y componentes, reclutan individuos con experiencia, encapsulan buenas ideas y conectan componentes. Sin embargo, el proceso de creacion de estandares puede tardar demasiado para el sector y algunos pierden el contacto con las verdaderas necesidades de aquello para los que estan dirigidos.

### Los sistemas necesitan lenguajes especificos de dominio
En el mundo del software ha renacido el interes por crear Lenguajes especificos del dominio, pequenos lenguajes independientes de creacion de secuencias de comandos o API de lenguajes estandar que permiten crear codigo que se lea de una forma estructurada, como lo escribiria un experto del dominio.
Un buen DSL miniminza el vacio de comunicacion entre un concepto de dominio y el codigo que lo implementa, al igual que las practicas agiles optimizan la comunicacion entre un equipo y los accionistas del proyecto. Se tiene que implementar la logica de dominios en el mismo lenguaje usado por un experto del dominio, hay menos riesgo de traducir incorrectamente el dominio en la implementacion.

Los DSL, si se usan de forma eficaz, aumentan el nivel de abstraccion por encima del codigo y los patrones del diseno. Permiten al desarrollador revelar la intencion del codigo en el nivel de abstraccion adecuado.

Los lenguajes especificos del dominio permiten expresar como POJO todos los niveles de abstraccion y todos los dominios de la aplicacion, desde directivas de nivel superior a los detalles mas minimos.

 VOLVER A LEER COMPRENSION A MEDIAS

 