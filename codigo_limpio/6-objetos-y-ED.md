# Objetos y Estructura de Datos

Las variables deben ser privadas para poder cambiar su implementacion cuando deseemos, porque hay tantos devs que crean metodos para mostrar sus variables privadas.

Hay que meditar seriamente la forma optima de representar los datos que tiene un objeto. La peor opcion es aniadir get's y set's a ciegas.

### Antisimetria de datos y objetos

la diferencia entre objetos y estructuras de datos es que los primeros ocultan sus datos tras abastracciones y muestran funciones que operan en dichos datos. En cambio las ED muestran sus datos y carecen de funciones con significado.

El oodigo por procedimientos facilita la inclusion de nuevas funciones sin modificar las estructuras de datos existentes. El codigo orientado a objetos, por su parte, facilita la inclusion de nuevas clases sin cambiar las funciones existentes.

El complemento dice: El codigo  por procedimienos dificulta la inclusion de nuevas estructuras de datos ya que es necesario cambiar todas las funciones. El codigo orientado a objetos dificulta la inclusion de nuevas funciones ya que es necesario cambiar todas las clases.

Los programadores experimentados saben que la idea que todo es un objeto es un mito.

### La ley de Demeter

Un modulo no debe conocer los entresijos de los objetos que manipula. Es decir un objeto no debe mostrar su estructura interna a traves de metodos de acceso ya que si lo hace, mostraria su estructura interna.

**Un metodo f de una clase c solo debe invocar los metodos de:**
- C
- Un objeto creado por f.
- Un objeto pasado como argumento a f.
- Un objeto en una variable de instancia de C.

El metodo no debe invocar metodos de objetos devueltos por ninguna de las funciones permitidas.(No hable con desconocidos, solo con amigos)

```java
final String outputDir = ctxt.getOptions().getScratchDir().getAbsolutePath();
```

### Choque de trenes

El codigo similar al anterior, suele denominarse choque de trenes ya que se asemeja a un grupo de vagones de tren. Este tipo de programacion se considera descuidada. Es mejor dividirla:
```java
Options opts = ctxt.getOptions();
File scratchDir = opts.getScratchDir();
final String outputDir = scratchDir.getAbsolutePath();
```
Saber que si incumple o no la ley de Demeter depende de si **ctxt, Options y ScratchDir** son objetos o estructuras de datos. Si son objetos, deberia ocultarse su estructura interna, no mostrarse, y conocer sus detalles internos. Entonces tendriamos un incumplimiento de la ley de Demeter. En cambio si son simples ED, mostraran su estructura y la ley de demeter no se aplica.

### Hibridos

Las estructuras hibridas mitad objeto y mitad estructura de datos genera confusion. Tienen funciones que realizan tareas significativas y tambien variables publicas o metodos publicos de acceso y mutacion que hacen que las variables privadas sean publicas, y tientan a otras funciones externas a usar dichas variables de la misma forma que un programa de procedimientos  usaria una ED.

Evite este diseno descuidado.

### Ocultar la estructura

Que pasa si **ctxt, options y scratchDir**  fueran objetos con comportamiento real, dado que deberian ocultar su estructura interna. Como obtendriamos la ruta absoluta del directorio scratch?
```java
ctxt.getAbsolutePathOfScratchDirectoryOption();
// o
ctxt.getScratchDirectoryOption().getAbsolutePath();
```
Esto genera un explosion de metodos en el objeto **ctxt**. La segunda asume que **getScratchDirectoryOption()** devuelve una estructura de datos, no un objeto. Fijese en eel siguiente codigo:
```java
String outFile = outputDir + "/" + className.replace('.','/') + ".class"
FileOutputStream fout = new FileOutputStream(outFile);
BufferedOutputStream bos = new BufferedOutputStream(fout);
```
Hay distintos niveles de detalles que resulta preocupante. Si ignoramos estos detalles vemos que la intencion de obtener la ruta absoluta del directorio scratch es crear un archivo de borrador de un nombre concreto.
```java
BufferedOutputStream bos = ctxt.createScratchFileStream(classFileName);
```
Parece razonable para un objeto. ctxt oculta sus detalles internos e impide que la funcion actual incumpla la ley de Demeter y se desplace por objetos que no deberia conocer.

### Objetos de transferencia de datos

La quintaesencia de una ED es una clase con variables publica y sin funciones. En ocasiones denominado Objeto de transferencia de datos (Data Transfer Object OTD). Los OTD son estructuras muy utiles, en especial para comunicarse con base de datos o analizar mensajes de conexiones, etc. Son los primeros de una serie de fases de traduccion que convierten datos sin procesar en objetos en el codigo de la aplicacion.

### Registro Activo

Son una forma especial de OTD. Son estructuras de datos con variables publicas (o de acceso) pero suelen tener metodos de navegacion como save o find. Por lo general son traducciones de tablas de base de datos u otros origentes.

El registro activo se debe considerar como una estructura de datos y crear objetos independientes que contengan reglas empresariales y que oculten sus datos internos.



















