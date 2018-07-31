# Nombres con Sentido

- Usar nombres con sentido y si se encuentran mejores cambiarlos (int d; // no es un buen nombre).
- El codigo debe ser lo mas explicito posible, un codigo con logica por mas sencilla que sea, es menos entendible si los nombres no dicen nada es mas dificil de entender.

### Evitar la desinformacion

- Evita nombres o abreviaciones que alejen el entendimiento del codigo por mas que parezca lo correcto Ej. hp, nombre para hipotenusa

- Evita nombres parecidos o con variaciones minimas

- Evita usar caracteres que puedan confundirse con otros que representen algo distinto Ej l es parece a 1, 0 se parece a O.

### Realizar distinciones con sentido

- Nombres distintos deben tener significados diferentes.
- Usa prefijos como a , an, the mientras la distincion tenga sentido.
- Evita palabras adicionales que sean redundates Ej. Nombre *variable* para una variable.
- Aprender a diferenciar los nombres de forma que el lector aprecie las diferencias.

### Usar nombres que se puedan pronunciar 

- Un nombre que no se puede pronunciar, no se podra explicar, de lo contrario incluso pronunciar alguna "adaptacion" de dicho nombre te desvia de su entendimiento.

### Usar nombres que se puedan buscar 

- Nombres muy pobres o cortos de una letra o numero tienden a ser dificiles a encontrar. La longitud de un nombre dee estar en correspondencia con  el tamaño de su ambito.

### Evitar codificaciones

Los nombres codificados resultan impronunciables y suelen escribirse de forma incorrecta.

#### Notacion hungara

Es una notacion importante en la api C de Windows donde todo era un entero, puntero long, puntero void, implementaciones de string. Hoy esta en desuso debido a la gran cantidad de editores que verifican el tipo.

### Prefijos de Miembros

Tampoco es necesario poner prefijos a las variables, dado que los usuarios tienden a ignorar el prefijo.

### Interfaces e implementaciones

Un caso especial para uso de codificaciones. Una forma de llamar a una interfaz es IShapeFactory (por ejemplo) esto puede o no ser recomendable, dependiendo de si quiero que mis usuarios sepan que se trata de una interfaz.

### Evitar asignaciones mentales 

- Los lectores no tienen porque traducir mentalmente sus nombres en otros que ya conocen. Por ejemplo *i, j, k* se suele usar para los contadores de bucles, sin embargo en otro contexto esto no es buena idea.

- Un programador profesional sabe que la claridad es lo que importa, y crean codigo que otros puedan entender.

### Nombres de clases

Las clases deben tener nombres o frases de nombre Ej. Customer, WikiPage, Account, AddressParser, el nombre de una clase no debe ser un verbo.

### Nombres de metodos

- Deben tener nombres de verbo *Ej. postPayment, deletePage o save*. Metodos de acceso, de modificacion, y predicados deben tener como prefijo *get, set e is*
- En constructores para la sobrecarga use nombres que describan los argumentos.

### No se exceda con el atractivo

Antes que ver el atractivo opte por la claridad.Ej evite eatMyShorts()  si quiere decir abort().

### Una palabra por concepto 

- Elija una palabra por cada concepto abstracto y mantengala. 
- Los nombres de funciones deben ser independientes y coherentes para que pueda elegir el metodo correcto sin necesidad de busquedas adicionales.
- Un lexico coherente es una gran ventaja para los programadores que tengan que usar codigo.

### No haga juegos de palabras

- Evite usar la misma palabra con dos fines distintos. Imagine el metodo *add* en diferentes clases lo cual esta bien siempre y cuando sean semanticamente equivalentes.

- Queremos que el estudio del codigo sea algo rapido, no un estudio exhaustivo.

### Usar nombres de dominios de soluciones 

Busque usar terminos informaticos, algoritmos, nombres de patrones, terminos matematicos y demas. No extraiga todos los nombres del dominio de problemas, para evitar que sus colegas tengan que preguntar sobre su significado si ya lo conocen con un nombre diferente.

### Usar nombres de dominios de problemas

Cuando no exista un termino de programacion para lo que estas haciendo, use el nombre del dominio de problemas. Separar los conceptos de dominio de soluciones y de problemas es parte del trabajo de un buen programador y disenador. 

### Añadir contexto con sentido

- Algunos nombrs tienen significado por si mismos, pero la mayoria no. Por eso debe incluirlos en un contexto, en clases, funciones y namespaces con nombres adecuados. Si todo falla puede usar prefijos como ultimo recurso.

### No Añadir contextos innecesarios

Los nombres breves suelen ser mas adecuado que los extensos, siempre que sean claros. No  añada mas contexto del necesario a un nombre. 


### Conclusiones

Escoger un nombre requiere de habilidad descriptiva y acerbo cultural. Es un problema de formacion, por tal razon no siempre se lo hace bien.

Cambiar nombres es una buena practica, siempre que este mejore el entendimiento del codigo.

Practique cambiando nombres y compruebe que la legibilidad del codigo mejora.













































































































