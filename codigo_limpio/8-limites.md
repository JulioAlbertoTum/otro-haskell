# Limites 

Con frecuencia adquirimos librerias de terceros. En otros casos dependemos de equipos para producir componentes o subsistemas. De algun modo debemos integrar este codigo externo con el nuestro. Aqui definiremso los limites de nuestro software.

### Utilizar codigo de terceros

Hay tension entre proveedores de interfaz que abogan por una capacidad amplia y global para poder trabajar en diversos entornos. Por otro lado los usuarios abogan por una interfaz centrada en sus necesidades concretas.

Por ejemplo si usamos la clase Map de java para guardar objetos Sensor y el mismo sera compartido por otras clases todas tendran acceso a todos los metodos incluido clear() que es bastante peligroso si se va ha compartir.
Ademas que se puede aniadir objetos de cualquier tipo a un mapa.
```java
Map sensors = new HashMap();
// para acceder a cualquier sensor
Sensor s = (Sensor)sensors.get(sensorId);
```
Cada usuario debera convertir el objeto al tipo correcto, esto esta bien pero no es un codigo limpio y no hace bien a la legibilidad.
Para mejorar este codigo podriamos hacer uso de genericos
```java
Map<Sensor> sensors = new HashMap<Sensor>();
// ....
Sensor s = sensors.get(sensorId);
```
Esto no soluciona que Map<Sensor> ofrezca mas prestaciones de las que se necesita. La forma mas limpia de usar Map es:
```java
public class Sensors {
	private Map sensors = new HashMap();

	public Sensor getById(String id) {
		return (Sensor) sensors.get(id);
	}

	// corte
}
```
Con esto la interfaz esta oculta, el uso de generico ya no es problema ya que la conversion y admin de tipos se hace en la clase Sensors. Ademas se limita el codigo con menos probabilidad de errores. No es necesario encapsular siempre Map pero cuando se pase Map por el sistema mantengala dentro de la clase o familia de clases  en la que se use.

### Explorar y aprender limites 

Nuestra intencion no es probar el codigo pero si crear pruebas para el codigo de terceros que utilicemos.

No deberia sorprendernos tener que realizar extensas sesiones de depuracion intentendo localizar errores en nuestro codigo o en el suyo.

En lugar de experimentar y probar el nuevo material en nuestro codigo de produccion podriamos crear pruebas que analizen nuestro entendimiento del codigo de terceros denominadas **Pruebas de Aprendizaje**

Ver Aprende log4j pagina 150

### Las pruebas de aprendizaje son algo mas que gratuitas

Las pruebas son gratuitas ademas de rentables cuando haya nuevas versiones de paquetes ejecutamos las pruebas de aprendizaje para comprobar si hay diferencias de comportamiento. Los creadores del codigo deberan cambiarlo y ajustarlo.

Ademas es necesario un conjunto de pruebas que ejerciten la interfaz de la misma forma que hace el codigo de produccion.

### Usar codigo que todavia no existe.

Hay otro tipo de limite que separa lo conocido de los desconocido. Lo que hay al otro lado del limite es desconocido.

Podemos disenar nuestro propia interfaz, de acuerdo a lo que deseariamos tener, lo mejor de esto es que podemos controlarlo.

Podemos usar una interfaz con adaptadores para hacer mas facil el manejo del codigo asi como la elaboracion de codigo para pruebas.

### Limites limpios

Los disenos de codigo correcto acomodan los cambios sin necesidad de grandes modificaciones. Cuando usamos codigo que no controlamos hay que proteger nuestra inversion y asegurarnos que los cambios futuros no son demasiado costosos.

Es mas segura depender de algo que controlemos que de algo que no controlemos o que nos controla. 






















