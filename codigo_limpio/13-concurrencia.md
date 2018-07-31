# Concurrencia
La creacion de programas concurrentes limpios es complicada, muy complicada. Es mas sencillo crear codigo que se ejecute en un mismo proceso. Tambien es mas faicl crar codig de subproccesamieto multiple que parezca correcto en la superficie pero que este danado a niveles profundos. Este codigo funciona correctamente hasta que el sistema se somete a determinadas presiones.

### Por que concurrencia?
La concurrencia es una estrategia de desvinculacion. Nos permite desvincular lo que se hacen de donde se hace. En aplicacion de un solo proceso, el que y el cuando estan firmemente vinculados que el estado de la aplicacion se puede determinar analizando la huella de la pila. Un programador que depure este tipo de sistemas puede definir un punto de interrupcion y saber el estado de la aplicacion en funcion del punto al que se llegue.

Desde el punto de vista estructural, la aplicacion parece una serie de equipos colaboradores y no un gran bucle principal. 

### Mitos e imprecisiones
Si no presta la suficiente atencion, pueden darse casos desagradables. Las imprecisiones mas habituales son:
- **La concurrencia siempre mejora el rendimiento:** En ocasiones, pero solo cuando puede compartir tiempo entre varios procesos o procesadores. 
- **El diseno no cambia al crear programas concurrentes:** El diseno de un algoritmo puede ser muy distinto al de un sistema deun solo proceso. La desvinculacion entre el que y el cuando suele tener un efecto importante en la estructura del sistema.
- **No es importante entender los problemas de concurrencia al trabajar con un contenedor Web o EJB:** Debe saber lo que hace su contenedor y protegerlo de problemas de actualizaciones concurrentes y bloqueo.

Otros aspectos relacionados con la creacion de software concurrente:
- La concurrencia genera cierta sobrecarga, tanto en rendimiento como en la creacion de codigo adicional.
- La concurrencia correcta es compleja, incluso para problemas sencillos.
- Los errores de concurrencia no se suelen repetir, de modo que se ignoran en lugar de considerarse verdaderos problemas.
- La concurrencia suele acarrear un cambio fundamental de la estrategia de diseno.

### Desafios
Ej ver pag 217

### Principios de defensa de la concurrencia
Veremos una serie de principios y tecnicas para proteger a sus sistemas de los problemas del codigo concurrente.

### Principio de responsabilidad unica (SRP)
SRP establece que un metodo, clase o componente solo debe tener un motivo para cambiar. El diseno de concurrencia es lo bastante complejo como para ser un motivo de cambio cno derecho propio y, por tanto, debe separarse del resto del codigo.

Desafortunadamente, es habitual incrustar los detalles de implementacion de concurrencia directamente en otro codigo de produccion.

Tenga en cuenta los siguientes aspectos

- El codigo relacionado con la concurrencia tiene su propio ciclo de desarrollo, cambios y ajustes.
- El codigo relacionado con la concurrencia tiene sus propios desafios, diferentes y mas complicados, que los del codigo no relacionado con la concurrencia.
- El numero de formas en la que el codigo incorrecto basado en la concurrencia puede fallar lo complica ya de por si, sin la carga ananida del codigo de aplicacion circundante.

**Recomendacion:** Separe el codigo de concurrencia del resto del codigo.

### Corolario: Limitar el ambito de los datos
Dos procesos que modifican el mismo campo u objeto compartido pueden interferir entre ellos y provocar un comportamiento inesperado. **synchronized** nos permite proteger una seccion importante del codigo que use el objeto compartido, sin embargo es mejor limitar el uso de estas secciones.Cuantos mas puntos actualicen datos compartidos, es mas probable que:
- Se olvide de proteger un o o varios de esos puntos, y se dane el codigo que modifica los datos compartidos.
- Se duplique el esfuerzo necesario necesario para garantizar la proteccion de todos los elementos (incumplimiento de DRY)
- Resulta  complicado determinar el origen de los fallos, que por naturaleza son dificiles de detectar.
**Recomendacion:** Encapsule los datos y limite el acceso a los datos compartidos.

### Corolario: usar copias de datos
Una forma de evitar datos compartidos es no compartirlos. En algunos casos es mejor copiar objetos y procesarlos como si fueran de solo lectura. En otros, se pueden copiar objetos, recopilar los resultados de varios procesos en las copias y despues combinar los resultados en un mismo proceso. 

### Corolario: Los procesos deben ser independientes
Pruebe a crear el codigo de sus procesos de forma que cada uno sea independiente y no comparta datos con otros. Cada uno procesa una solicitud cliente y todos los datos necesarios provienen de un origen sin compartir y se almacenan como variables globales.
**Recomendacion:** Intente dividir los datos en subconjuntos independientes que se puedan procesar en procesos independientes, posiblemente en distintos procesadores.

### Conocer las bibliotecas
En java existen diversos aspectos que tomar en cuenta a la hora de crear codigo de procesos.
- Usar las colecciones compatibles con procesos proporcionadas.
- Usar la estructura de ejecucion de tareas no relacionadas.
- Usar soluciones antibloqueo siempre que sea posible.
- Varias clases de bibliotecas no son compatibles con procesos.

### Colecciones compatibles con procesos
Ver codigo pag 220
Recomendacion: Revise las clases de las que se disponga.

### Conocer los modelos de ejecucion
Existen ciertas definiciones que son necesarias conocer para dividir el compartamiento de una aplicacion concurrente.
- Recursos Vinculados: Recurso de tamanio o numero fijo usados en entorno concurrente, como por ejemplo conexiones a base de datos o buffer de lectura/escritura.
- Exclusion Mutua: Solo un proceso puede acceder a datos o a un recursos compartido por vez
- Inanicion: Se impide que un proceso o grupo de procesos continuen demasiado tiempo o indefinidamente. 
- Bloqueo: Dos o mas procesos esperan a que ambos terminen. Cada proceso tiene  un recurso y ninguno puede terminar hasta que obtenga el otro recurso.
- Bloqueo activo: procesos bloqueados, intentando realizar su labor pero estorbandose unos a otros. Por motivos de resonancia, los procesos siguen intentando avanzar pero no pueden durante demasiado tiempo, o de forma indefinida.

### Productor-Consumidor
Uno o varios procesos productores crean trabajo y lo anaden a un bufer o a una cola.
Uno o varios procesos consumidores adquieren dicho trabajo de la cola y lo completan.
La cola entre productores y consumidores es un recurso vinculado, lo que significa que los productores deben esperar a que se libere espacio en la cola antes de escribir y los consumidores deben esperar hasta que haya algo que consumir en la cola. La coordinacion entre productores y consumidores a traves de la cola hace que unos emitan senales a otros. Los productores escriben en la cola e indican que ya no esta vacia. Los consumidores leen de la cola e indican que ya no esta llena. Ambos esperan la notificacion para poder continuar.

### Lectores-Escritores
Cuando un recurso compartido actua basicamente como fuente de informacion para lectores pero ocasionalmente se actualiza por parte de escritores, la produccion es un problema. El enfasis de la produccion puede provocar la inanicion y la acumulacion de informacion caducada. Las actualizaciones pueden afectar a la produccion. La coordinacion de lectores para que no lean algo que un escritor esta actualizando y viceversa es complicada. Los escritores tienden a bloquear a los lectores durante periodos prolongados, lo que genera problemas de produccion.

El desafio consiste en equilibrar las necesidades de ambos para satisfacer un funcionamiento correcto, proporcionar una produccion razonable y evitar la inanicion. Una sencilla estrategia hace que los escritores esperen hasta que deje de haber lectores antes de realizar una actualizacion. Si hay lectores continuos, los escritores perecen de inanicion.

Por otra parte, si hay escritores frecuentes y se les asigna prioridad, la produccion se ve afectada. Determinar el equilibrio y evitar problemas de actualizacion concurrente es el objetivo de este modelo.

### La cena de los filosofos
Imagine varios filosofos sentados alrededor de una mesa redonda. A la izquierda de cada uno hay un tenedor. En el centro de la mesa, una gran fuente de espaguetis. Los filosofos pasan el tiempo pensando a menos que tengan hambre. Cuando tiene hambre, utilizan los tenedores situados a ambos lados para comer. No pueden comer a menos que tengan dos tenedores. Si el filosofo situados a la derecha o izquierda de otros ya tiene uno de los tenedores que necesita, tendra que esperar a que termine de comer y deje los tenedores. Cuando un filosofo termina de comer, vuelve a colocar los tenedores en la mesa hasta que vuelve a tener hambre. Cambie los filosofos por procesos y los tenedores por recursos y tendra un problema habitual en muchas  aplicaciones en las que los procesos compiten por recursos. 

La mayoria de los problemas de concurrencia que encontrara seran alguna variante de estos. Analice los algoritmos y cree propias para estar preparado cuando surjan problemas de concurrencia.
**Recomendacion:** Aprenda estos algoritmos basicos y comprenda sus soluciones

### Dependencias entre metodos sincronizados
Las dependencias entre metodos sincronizados generan sutiles errores en el codigo concurrente. Java cuenta con **synchronized** que protege metodos individuales.
Recomendacion: evite usar mas de un metodoen un objeto compartido.
En ocasiones tendra que usar mas de un metodo en un objeto compartido. En ese caso, hay tres formas de crear codigo correcto.
- **Bloqueo basado en clientes:** El cliente debe bloquear al servidor antes de invocar el primer metodo y asegurarse de que el alcance del bloque incluye el codigo que invoque el ultimo metodo.
- **Bloqueo basado en servidores:** Debe crear un metodo en el servidor que bloquee el servidor, invoque todos los metodos y despues anule el bloqueo. El cliente debe invocar el nuevo metodo.
- **Servidor Adaptado:** Cree un intermediario que realice el bloque. Es un ejemplo de bloqueo basado en servidores en el que el servidor original no se puede modificar.

### Reducir el tamanio de las secciones sincronizadas
La palabra clave **synchronized** presenta un bloqueo. Todas las secciones de codigo protegidas por el mismo bloqueo solo tendran un proceso que las ejecute en un momento dado. Los bloqueos son costosos ya que generan retrasos y anaden sobrecarga. Las secciones criticas deben protegerse, de modo que debemos disenar nuestro codigo con el menor numero posible de secciones criticas.

Recomendacion: Reduzca al maximo el tamanio de las secciones synchronized

### Crear codigo de cierre correcto es complicado
Crear un sistema activo y que se ejecute indefinidamente es distinto a crear algo que funcione de forma temporal y despues se cierre correctamente. Entre los problemas mas habituales  destacan los bloqueos, con procesos que esperan una senal  para continuar que nunca se produce.

Un proceso  principal que genera varios procesos  secundarios y que espera a que todos terminen antes de liberar sus recursos y  cerrarse.Si uno de los procesos secundarios esta bloqueado? el principal esperara indefinidamente y el sistema nunca cerrara.

Un sistema similar al que se indica que se cierre. El proceso principal indica a todos los secundarios que abandonen sus tareas y terminen. Pero imagine que dos procesos secundarios funcionan como par productor/consumidor y que el productor recibe una senal del principal y se cierra rapidamente.El consumidor espera un mensaje del productor y puede quedar bloqueado en un estado en el que no recibe la senal del principal, lo que tambien impide que este finalice.

Son situaciones habituales, por lo que es necesario construir codigo concurrente con cierres correctos,  tendra que dedicar tiempo a que el cierre se produzca de forma correcta.

### Probar codigo con procesos
Las pruebas adecuadas pueden minimizar los riesgos, en especial en aplicaciones de un solo proceso. Cuando hay dos o mas procesos que usan el mismo codigo y trabajan con datos compartidos, la situacion se vuelve mas compleja.

Recomendacion: Cree pruebas que puedan detectar problemas y ejecutelas periodicamente, con distintas configuraciones de programacion y del sistema, y cargas. Si fallan identifique el fallo. Algunas recomendaciones concretas:
- Considere los fallos como posibles problemas de los procesos.
- Consiga que primero funcione el codigo sin procesos.
- El codigo con procesos se debe poder conectar a otros elementos.
- El codigo con procesos debe ser modificable.
- Ejecute con mas procesos que procesadores.
- Ejecute en diferentes plataformas.
- Disene el codigo para probar y forzar fallos 

### Considerar los fallos como posibles problemas de los procesos
El codigo con procesos hace que fallen elementos que no deberian fallar. Los problemas del codigo con procesos pueden mostrar sus sintomas una vez cada mil o un millon de ejecuciones.
Es recomendable asumir que los fallos aislados no existen. Cuanto mas los ignore, mayor sera la cantidad de codigo que se acumule sobre un enfoque defectuoso.

Recomendacion: No ignore los fallos del sistema como algo aislado.

### Conseguir que primero funcione el codigo sin procesos
Asegurese de que el codigo funciona fuera de sus procesos. Por lo general, esto significa crear algunos POJO que los procesos deban invocar. Los POJO no son compatibles con los procesos y por tanto se pueden probar fuera de su entorno.

Recomendacion: No intente identificar fallos de procesos y que no sean de procesos al mismo tiempo. Asegurese de que su codigo funciona fuera de los procesos.

### El codigo con procesos se debe poder conectar a otros elementos.
Cree el codigo compatible con la concurrencia de forma que se pueda ejecutar en distintas configuraciones:
- Un proceso, varios procesos y variarlo durante la ejecucion.
- El codigo con procesos interactua con algo que puede ser real o probado.
- Ejecutar con pruebas dobles ejecutadas de forma rapida, lenta y variable.
- Configurar pruebas que ejecutar en diferentes iteraciones.

Recomendacion: El codigo con procesos debe poder conectar a otros elementos y ejecutar en distintas configuraciones.

### El codigo con procesos debe ser modificable
La obtencion del equilibrio adecuado de procesos suele requerir operaciones de ensayo y error. En las fases iniciales, compruebe el rendimiento del sistema bajo diferentes configuraciones Permite que se puedan modificar los distintos procesos y tambien durante la ejecucion del sistema. Tambien puede permitir la modificacion automatica en funcion de la produccion y la utilizacion del sistema.

### Ejecutar con mas procesos que procesadores
Cuando el sistema cambia de tarea, se producen reacciones. Para promover el intercambio de tareas, realice la ejecucion con mas procesos que procesadores o nucleos. Cuanto mayor sea la frecuencia de intercambio de las tareas, mas probabilidades existen de que el codigo carezca de una seccion critica o se produzcan bloqueos.

### Ejecutar en diferentes plataformas
En cada sistema operativo hay una politica de procesos diferente que afecta a la ejecucion del codigo. El codigo con procesos multiples se comporta de forma distinta en cada entorno. Debe ejecutar sus pruebas en todos los entornos de implementacion posibles.

Recomendacion: Ejecute el codigo con procesos en todas las plataformas de destino con frecuencia y en las fases iniciales.

### Disenar el codigo para probar y forzar fallos
Es habitual que los fallos del codigo concurrente se oculten. Las pruebas sencillas no suelen mostrarlos. En realidad, suelen ocultarse durante el procesamiento normal. Puede aparecer horas, dias o semanas despues.

La razon de que los problemas de procesos sean infrecuentes, esporadicos, y apenas se repitan es que solo fallas algunas de los miles de rutas posibles que recorren una seccion vulnerable. Por tanto, la probabilidad de adoptar una ruta fallida es realmente baja, lo que dificulta la deteccion y la depuracion.

Resulta mas adecuado que el codigo incorrecto falle lo antes posible y con frecuencia. Hay dos opciones de instrumentacion de codigo:
- Manual 
- Automatica

### Manual
Puede aniadir invacaciones  de **wait(), sleep(), yield(), priority()** manualmente a su codigo, en especial si tiene que probar un fragmento especialmente escabroso.

La invocacion yield() cambia la ruta de ejecucion adoptada por el codigo y posiblemente hace que el codigo falla donde no lo hacia antes. Si el codigo falla, no se debe a la invocacion de yield() anadida. Se debe a que el codigo es incorrecto y hemos hecho que el fallo sea mas evidente. Este enfoque presenta varios problemas.
- Tendra que buscar manualmente los puntos adecuados donde hacerlo.
- Como sabe donde incluir la invocacion y que tipo de invocacion a usar?
- La presencia de este codigo en un entorno de produccion ralentiza innecesariamente el codigo.
- Es un enfoque que puede o  no detectar  los fallos; de hecho, no las tiene todas consigo.

Lo que necesitamos es una forma de hacerlo durante la fase de pruebas, no de produccion. Tambien debemos poder mezclar configuraciones entre ejecuciones, lo que aumenta las probabilidades de detectar los errores.

###Automatica
Puede ser herramientas cmo la estructura orientada a aspectos para instrumentar su codigo mediante programacion.
Tras ello, use un sencillo aspecto que seleccione aleatoriamente entre no hacer nada, pausar y generar un resultado.

El objetivo es que los procesos del codigo se ejecuten en distinto orden en momentos diferentes. La combinacion de pruebas bien escritas y ejecuciones aleatorias puede aumentar considerablemente la capacidad de detectar errores.
Recomendacion: use estas estrategias para detectar errores.












