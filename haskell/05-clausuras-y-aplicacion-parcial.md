### 5.1 Clausuras-creando funciones con funciones
En la anterior leccion la clase ifEven tomaba un argumento que nos permitia abstraer un patron de computacion. de Esta forma creabamos las funciones ifEvenInc, ifEvenDouble, ifEvenSquare.

Usar funciones como argumentos nos ayudan a limpiar el codigo. Pero si notas todavia estas repitiendo un patron de programacion. Cada definicion es identica excepto por la funcion que se pasa. Esto se puede solucionar con una funcion que retorne funciones, llamado **genIfEven**
```hs
ifEvenInc n = ifEven inc n
ifEvenDouble n = ifEven double n
ifEvenSquare n = ifEven square n
-- Existe le patron ifEvenX n = ifEven X n
-- generador de funciones

genIfEven f = (\x -> ifEven f x)
```
La funcion f que pasas es capturada dentro de la funcion lambda!. Cuando capturas un valor dentro de una funcion lambda, esto es lo que se conoce como un **clausura**. Podemos ahora crear funciones con esta.
```hs
ifEvenInc = genIfEven inc
-- es lo mismo que 
ifEvenInc = (\x -> ifEven inc x)
```
### Ejemplo Generando URLs para un API 

Para obtener datos solemos acudir a un API RESTful, el tipo mas simple es con un GET Request, que necesita los siguientes parametros:
- El hostname
- El nombre del recurso que se solicita.
- El ID del recurso
- API key
Para construir la URL podemos usar
```hs
getRequestURL host apiKey resource id = host ++
										"/" ++
										resource ++
										"/" ++
										id ++
										"?token=" ++
										apiKey
```
Se puede observar que el orden en que pedimos los argumentos no es el mismo en que aparecen en la url.

**En haskell el orden de los argumentos debe ser del mas  al menos general**

Dado que el equipo podria querer visitar varias hosts, es necesario no ser tan especificos. Lo que se necesita es una funcion que todos puedan usar para generar un request URL.
```hs
genHostRequestBuilder host = (\apiKey resource api -> 
								getRequestUrl host apikey resource id) 
-- se puede aplicar como
exampleUrlBuilder = genHostRequestBuilder "http://example.com"
exampleUrlBuilder "1337fsf321" "book" "123"
```
Este codigo todavia tiene un problema cuando usamos un mismo apiKey, es tedioso
```hs
genApiRequestBuilder hostBuilder apiKey = (\resource id -> 
											hostBuilder apiKey resource id)
```
Finalmente podemos construir una funcion que haga la creacion de requerimiento mas facil.
```hs
myExampleUrlBuilder = genApiRequestBuilder exampleUrlBuilder "1337fsf321"
-- usamos como
myExampleUrlBuilder "book" "123"
```
### Aplicacion parcial: haciendo clausuras simples
Clausuras son poderosas y utiles, pero el uso de funciones lambda mas dificil de leer y razonar. ademas todas las clausuras que hemos escrito tienen una patron identico se provee algunos parametros que una funcion toma y crea una nueva funcion esperando el resto
```hs
addd4 a b c d = a + b + c + d
-- si queremos crear una funcion que tome un argumento y retorne una clausura que espere
-- tres argumentos
addXto3 x = (\b c d -> add4 x b c d)
-- si quisieramos un addxyto2
addXYto2 x y = (\c d -> add4 x y c d)
```
El abarrotamiento de funciones lambda le quita claridad.
Para solucinar este problema haskell nos da una solucion. si llamas a add4 con pocos argumentos no se genera un error si no una rama con una nueva funcion. A esta caracteristica se le llama **aplicacion parcial** 

Gracias a la aplicacion parcial raramente escribiras o pensaras explicitamente sobre clausuras en haskell.
```hs
exampleUrlBuilder = getRequestUrl "http://example.com"
myExampleUrlBuilder = exampleUrlBuilder "1337fs311"
```
### Poniendo todo junto
Aplicacion parcial es tambien la razon que creamos una regla para los argumentos del mas al menos general. Cuando usamos aplicacion parcial, los argumentos son aplicados del primero al ultimo. 
En el caso que quisieras cambiar el ordel de tus argumentos una solucion ingeniosa seria:
```hs
flipBinaryArgs binaryFunction = (\x y -> binaryFunction y x)
```
Para operadores infijos tales como + - * / podemos volverlos infijos usando parentesis.
```hs
> (+) 5 6
11
> (/) 14 2
7
```
Para la division y sustraccion, el orden de los argumentos es importante. Es facil de entender porque quisieras crear una clausura alrededor del segundo argumento. 

LEER UNA VEZ MAS LA ULTIMA PARTE




