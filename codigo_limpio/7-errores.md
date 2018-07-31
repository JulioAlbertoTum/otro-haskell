# Procesar Errores

Las entradas pueden ser incorrectas y los dispositivos pueden fallar, y cuando lo hacen los programadores somos responsables  de comprobar que el codigo hace lo que debe hacer.

Mucho del codigo esta dominado por el control de errores. Es decir es imposible saber lo que el codigo hace debido al control de errores.

Es decir el control de errores es importante pero no debe oscurecer la logica del programa.

Detallaremos tecnicas para procesar los errores con elegancia.

### Usar excepciones en lugar de codigos devueltos

Antes se carecian de excepciones por lo que todo se debia hacer en el codigo delegando al invocador la tarea de decidir que hacer cuando se daba un error.

Es mas recomendable generar un excepcion.

### Crear primero la instruccion try-catch-finally

Las exception generan un ambito en el programa. con la instruccion try-catch-finally indicamos la ejecucion se puede cancelar en cualquier momento y despues retomar catch.

Los bloques try son como las transacciones. catch debe salir del programa de forma coherente.

Es aconsejable crear las excepciones acompanadas de una metodologia que use TDD para ir refactorando y refinando gradualmente el codigo.

### Usar excepciones sin comprobar

Las excepciones comprobadas no son necesarias para crear software robusto. 

Las excepciones comprobadas es el incumplimiento del principio  abierto/cerrado. 

### Ofrecer contexto junto a las excepciones

Las excepciones que genere deben proporcionar un contexto adecuado para
determinar el origen y la ubicacion de un error.
Redacte mensajes de error informativos y paselos junto a sus excepciones. Mencione la operaicon fallida y el tipo de fallo. Si guarda registros su aplicacion, incluya informacion suficiente  para poder registrar el error en la clausula catch.

### Definir clases de excepcion de acuerdo a las necesidades del invocador

Existen varias formas de clasificar los errores. Podemos hacerlo por origen (proviene de uno u otro componente?) o por tipo (son fallos del dispositivo, de red, o errores de programacion), sin embargo al crear clases de excepcion en una aplicacion, debemos preocuparnos de como se capturan.

En muchos casos es mejor crear un envoltorio que capture y traduce las excepciones  generadas por la clase ACMEPort

Ej. Pag 140

Es recomendable envolver API de terceros, de esta forma se minimizan las dependencias. A menudo una unica clase de excepcion para una zona concreta del codigo.

Use clases diferentes solo para capturar una excepcion y permitir el paso de otra distinta.

### Definir el flujo normal

Con los consejos anteriores hara una importante separacion entre logica empresarial y el control de errores. La mayoria de su codigo parecera un algoritmo limpio y sin adornos. Debe envolper API externas para poder generar sus propias excepciones y definir un controlador por encima del codigo para poder procesar calculos cancelados.

### No devolver Null

Una posibilidad de error reside en el hecho devolver null. 

Al devolver null, basicamente nos creamos trabajo y generamos problemas para los invocadores. Basta con que falte una comprobacion de null para que la aplicacion pierda el control.

Si se siente tentado de devolver null desde un metodo, pruebe a generar una excepcion o devolver un caso especial. Si invoca un metodo que devuelva null desde una API de terceros, envuelvalo en un metodo que genere una excepcion o devuelva un objeto de caso especial. 

Asi es mejor evitar la mayor cantidad de NullPointerException.

### No pasar Null

**Pasar null desde metodos es incorrecto, pero es peor pasar null a metodos**, a menos que trabaje con un API que espere que pase  null, debe evitarlo siempre que  sea posible.

En la mayoria de los lenguajes no hay una forma  correcta de procesar un null pasado por accidente. El enfoque mas racional es evitar que se pase null de forma predeterminada. Si lo hace, puede disenar codigo sabiendo que null en una lista de argumentos indica in problema y los errores seran menores.

 
























