### Limpieza a traves de disenos emergentes
Segun Kent Beck, un diseno es sencillo si cumple estas cuatro reglas:
- Ejecuta todas ls pruebas
- No contiene duplicados
- Expresa la intencion del programador
- Minimiza el numero de clases y metodos

### Primera regla del diseno sencillo: Ejecutar todas las pruebas

Un diseno debe generar un sistema que actue de la forma prevista. Un sistema minuciosamente probado y que supera todas las pruebas en todo momento se denomina estable. Los sistemas que no se pueden probar no se puede verificar, y un sistema que nos puede verificar no debe implementarse.

Resulta mas sencillo probar clases que cumplen el SRP, cuantas mas pruebas se disenen mas cerca estamos de elementos mas faciles de probar.

Cuantas mas pruebas creemos mas usaremos principios DIP y herramientas con inyeccion de dependencias, interfaces y abstraccion para minimizar dichas conexiones.

La creacion de pruebas conduce a obtener mejores disenos.

### Reglas 2 a 4 del diseno sencillo:

Debemos mantener limpio el codigo y las clases.Para ello, refacotirizamos el codigo progresivamente. La presencia de las pruebas hace que perdamos el miedo a limpiar el codigo y que resulte danado.

En la fase de refactorizacion es donde podemos aplicar las otras tres reglas del diseno correcto: eliminar duplicados, garantizar capacidad de expresion y minimizar el # de clases y metodos.

### Eliminar duplicados
Los duplicados suponen un esfuerzo adicional, riesgos aniadidos y una complejidad a mayores innecesaria. Las lineas de codigo similar puede modificarse para que parezcan refactorizadas, y otras formas de duplicacion como la de implementacion. 

### Expresividad
Es facil crear codigo que entendamos, ya que durante su creacion nos centramos en comprender el problema que intentamos resolver. Los encargados de mantener el codigo no lo comprenderan de la misma forma.

Al aumentar la complejidad de los sistemas, el programador necesita mas tiempo para entenderlo y aumentar las posibilidades de errores. Cuanto mas claro sea el codigo, menos tiempo perderan otros en intentar comprenderlo. Esto reduce los defectos y el coste de mantenimiento

Escoger nombres adecuados, reducir el tamanio de funciones y clases, usar una nomenclatura estandar.

Las pruebas de unidad bien escritas tambien son expresivas, lo que tambien sirve como documentacion.

Pero la forma mas importante de ser expresivo es la practica. 

### Clases y metodos minimos 
Incluso conceptos tan basicos como la eliminacion de codigo duplicado, la expresividad del codigo y SRP pueden exagerarse. Esta regla sugiere minimizar la cantidad de funciones y clases.

Evite los dogmas sin sentido y busque un enfoque mas pracmatico.

Aunque es importante reducir la cantidad de clases y funcionos, es mas importante contar con pruebas, eliminar duplicados y expresarse correctamente.

