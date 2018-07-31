# Pruebas de unidad

Los movimientos Agile y TDD han animado a muchos programadores a crear pruebas de unidad automatizadas y cada vez son mas. Sin embargo se han pasado por alto dos de los aspectos mas sutiles e importantes de disenar pruebas de calidad.

### Las tres leyes del DGP
DGP nos pide que primero creemos las pruebas de unidad, antes que el codigo de produccion. 
- **Primera ley**: No debe crear codigo de produccion hasta que haya creado una prueba de unidad que falle.
- **Segunda ley**: No debe crear mas de una prueba de unidad que baste como fallida y no compilar, se considera un fallo.
- **Tercera ley**: NO debe crear mas codigo de produccion que el necesario para superar la prueba de fallo actual.

Estas leyes generan un ciclo de 30 segundos de duracion. Las pruebas y el codigo de produccion se crean de forma conjunta. Trabajando asi crearemos decenas de pruebas al dia que abarcaran todos los aspectos de nuestro codigo de produccion. El tamanio de dichas pruebas, puede ser similar al codigo de produccion.

### Realizar pruebas limpias
Pruebas incorrectas llevan a muchos errores, ya que las mismas deben cambiar de acuerdo a la evolucion del codigo. Cuanto menos limpias mas dificil es cambiarlas. 

El codigo de prueba es tan importante como el de produccion. Requiere concentracion, diseno y cuidado como el codigo de produccion.

### Las pruebas propician posibilidades

Las pruebas hacen que el codigo sea flexibles y se pueda mantener y reutilizar ya que si tiene pruebas no tendra miedo a realizar cambios en el codigo. De esta forma se reduce la posibilidad  de aniador errores no detectados.

### Pruebas limpias
Los atributos de una prueba limpia son: legibilidad, legibilidad, legibilidad. La legibilidad es lo mas importante en las pruebas de unidad que en el codigo de produccion. Se deben considerar claridad, simplicidad y densidad de expresion. 

Debe existir un patron generar-operar-comprobar en la estructura de cada prueba. 

### Lenguaje de pruebas especifico del dominio
Debe existir un lenguaje especifico del dominio para las pruebas. creamos una serie de funciones y utilidades que usan dichas API y que facilitan la escritura y la lectura de las pruebas. Estas funciones y utilidades  se convierten en una API especializada usada el pruebas. 

Los programadores disciplinados refactorizan su codigo de prueba en versiones mas sucintas y expresivas.

### Un estandar dual
El codigo de la API de pruebas tiene un conjunto de  estandares de ingenieria diferentes al codigo de produccion, sin embargo no debe ser tan eficaz como el codigo de produccion.

ver codigo pag 164

### Una afirmacion por prueba
Hay un regla que senala que solo debe haber una instruccion de afirmacion por prueba.

Una convencion para nombrar funciones puede ser *dato-cuando-entonces* asi las pruebas son mas facilesde leer.

### Un solo concepto por prueba
Un concepto mas conveniente que el de una afirmacion por prueba. Es que un unico concepto en cada funcion de prueba. 

ver pag 166

### F.I.R.S.T.
Las pruebas limpias siguen otras cinco reglas:
- **Rapidez (Fast)**: Las pruebas deben ser rapidas y ejecutarse de forma rapida.- **Independencia**: las pruebas no deben depender entre ellas. Una prueba no debe establecer condicioens para la siguiente. Debe poder ejecutar cada prueba de forma independiente en el orden que desee. 
- **Repeticion**: Las pruebas deben poder repetirse en cualquier entorno. Debe poder ejecutarlas en el entorno de produccion, en el de calidad, y en su portatil de camino a casa en un tren sin red.
- **Validacion Automatica**: Las pruebas deben tener un resultado booleano: o aciertan o fallan. No debe tener que leer un extenso archivo de registro para saber si una prueba ha acertado, no comparar manualmente dos archivos de texto distintos para ello.
- **Puntualidad**: Las pruebas deben crearse en el momento preciso: antes del codigo de produccion que hace que acierten.




















































