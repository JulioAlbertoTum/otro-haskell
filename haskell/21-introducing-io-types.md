En la leccion 1, vimos un programa hola mundo, En Esta leccion, revisaremos un programa similar  para conseguir un mejor sentido de como IO trabaja en Haskell. Aqui un ejemplo del programa usando IO que lee un nombre del comando en linea e imprime "Hola <name>".
```hs
holaPersona :: String -> String
holaPersona name = "Hola " ++ " " ++ name ++ "!"

main :: IO ()
main = do
  putStrLn "Hola! Cual es tu nombre?"
  name <- getLine
  let statement = holaPersona name
  putStrLn statement
```
Ante de ver cualquier cosa en haskell, pudimos leer este programa bastante bien. Desafortunadamente, ahora que ya conocemos mas sobre haskell,  esto probablemente suena mas confuso. La funcion holaPersona es muy simple, pero todo cambia con la funcion main que es diferente de todo lo que has visto hasta ahora. Tendriamos las siguientes preguntas.
- Que el tipo IO () ?
- Porque esta do despues de main ?
- putStrLn retorna algun valor?
- Porque algunas variables estan asignadas con <- y otras con let?

Al final de esta lecion, tendremos una razonable explicacion de tosa esta cosas, y ayudara a tener un mejor entendimiento de las bases de IO en Haskell.

## 21.1 IO tipos - tratando con el mundo impuro
Como es menudo el caso con haskell, si no estas seguro de que estas haciendo, es mejor mirar los tipos! El primer tipo que hay que entender es el tipo IO. En la unidad precedente, dimos un vistazo al tipo Maybe que es un tipo parametrizado (un tipo que toma otro tipo como un argumento) que representa un contexto cuando un valor puede ser olvidado. IO en Haskell es un tipo parametrizado que es similar a maybe, La primera cosa que ellos comparten en comun es que ellos son tipos parametrizados del mismo tipo, Puedes ver esto buscando el kind de IO y Maybe:
```hs
GHCi> :kind Maybe
Maybe :: * -> *
GHCi> :kind IO
IO :: * -> *
```
La otra cosa que tienen Maybe e IO en comun es que (a diferencia de List o Map) ellos describen un contexto para sus parametros en lugar de un contenedor. El contexto para el tipo IO es que el valor viene de una operacion input/Output. Ejemplos comunes de esto incluyen lectura de entradas de usuario, imprimiendo en la salida estandar, y leyendo un archivo.

Con un tipo Maybe, estamos creando un contexto para un problema especifico: algunas veces los valores de un programa no estaran ahi. Con IO, estamos creando un contexto para un amplio rango de problemas que pueden ocurrir en IO. No solo IO es propenso a errores, pero tambien es inherentemente con estado (escribiendo cambios en un archivo) y tambien  a menudo impuro (llamando getLine muchas lineas pueden ser facilmente tratadas como un resultado diferente cada vez que el usuario ingresa una entrada diferente). Aunque esto puede causar problemas en I/O, esa es la esencia de la forma en la que I/O trabaja. Que tan bueno es un programa que no cambia el estado del mundo en alguna forma? Para guargar el codigo Haskell puro y predecible, usamos el tipo IO para proveer  un contexto para  los datos que puede no comportarse de la forma que el resto de tu codigo haskell hace. Las acciones IO  no son funciones.

En esta ejemplo de codigo, solo vemos el tipo IO siendo declarado, el tipo de main: 
```hs
main :: IO ()
```
El primer () puede ser visto como un simbolo especial, pero en realidad esta es solo un tupla de cero elementos. En el pasado, encontramos tuplas representadas por pares o triples que sean utiles, pero como puede ser una tupla de cero elementos util? Aqui hay algunos tipos similares con Maybe asi que puedes ver que IO () es solo IO parametrizado con (), y puedes tratar de descifrar porque () seria util.
```hs
GHCi> :type Just (1,2)
Just (1,2) :: (Num t, Num t1) => Maybe (t, t1)
GHCi> :type Just (1)
Just (1) :: Num a => Maybe a
GHCi> :type Just ()
Just () :: Maybe ()
```
Para Maybe, ser parametrizado con () es inutil. Este puede tener solo 2 valores, Just () y Nothing. Pero discutiblemente, Just () es Nothing. Esto resulta que esta representando nada es exactamente nada porque queremos parametrizar IO con una tupla vacia.

Puedes entender esto de mejor forma pensando sobre que pasa cuando tu funcion main se ejecutado tu ultima linea de codigo es:
```hs
putStrLn statement
```
Como sabes, este imprime put oracion, que typo es el que putStrLn retorna? Este envia un mensaje al mundo, pero no es claro que nada significativo se va a tener de vuelta. En un sentido literal, putStrLn retorna nada en absoluto. Como haskell necesita un tipo para asociar con main, pero main no retorna nada, usamos la tupla () para parametrizar tu tipo IO, Porque () es esencialmente nada, esta es la mejor forma de transmitir este concepto en el sistema de tipos de Haskell.

Aunque esto puede ser satisfactorio en el sistema de tipos de Haskell, algo deberia ser problematico sobre tu main. En el comienzo del libro, vimos tres propiedades de funciones que hacen un programa funcional predecible y seguro:
- Todas las funciones deben tener un valor
- Todas las funciones deben retornar un valor
- Toda vez que el mismo argumento es suministrado, el mismo valor debe ser retornado (transparencia referencial).

Claramente, main no retorna ningun valor significativo; Este simplemente realiza una accion. Esto resulta en que main no es una funcion, porque este rompe una de las reglas fundamentales de funciones: Este no retorna un valor.Como hace esto, nosotros nos referimos a main como una **Accion IO** las acciones trabajan como  funciones excepto que ellas violan al menos una de las tres reglas establecidas para las funciones de este libro. Algunas acciones IO no retornan valor, algunas no toman entrada, y otras no siempre retornan el mismo valor dada la misma entrada.

### 21.1.1 Ejemplos de acciones IO
Si main no es una funcion. lo que sigue es putStrlLn. Puedes aclarar esto buscando el tipo de putStrLn:
```hs
putStrLn :: String -> IO ()
```
Como puedes ver, el tipo retornado de putStrLn es IO (). Como main y putStrLn son acciones IO porque estas violan la regla de que las funciones retornan valores.

La siguiente funcion confusa es getLine. Claramente, esta trabaja diferente a cualquier otra funcion vista porque no toma argumentos! Aqui el tipo de getLine:
```hs
getLine :: IO String
```
A diferencia de putStrLn, que toma un argumento y no retorna valor, getLine no toma ningun valor pero reporna un tipo IO String. ESto significa que getLine viola nuestra regla que todas las funciones deben tomar un argumento. Como getLine viola esta regla de funciones, esta tambien es una accion IO.

Ahora veamos una caso mas interesante. Si importamos **System.Random** , puedes usar randomIO, que toma un par de valores en una tupla que representan el minimo y maximo de un rango y entonces generar un numero aleatorio en este rango. Aqui un simple programa llamado roll.hs qu usa randomIO y, cuando se ejecuta, actua como se tira un dado.
```hs
import System.Random

minDie :: Int
minDie = 1 

maxDie :: Int
maxDie = 6

main :: IO ()
main = do 
  dieRoll <- randomRIO (minDie, maxDie)
  putStrLn (show dieRoll)
```
Puedes compilar tu programa en GHC y tirar el dado:
```hs
ghc roll.hs
./roll
2
```
Que hay sobre randomRIO? Este toma un argumento (el par min/max) y retorna una argumento (un tipo IO  parametrizado con el tipo del par), as que es una funcion?  Este ejecuta tu programa mas de una vez, veremos este problema.
```hs
$ ./roll
4
$ ./roll
6
```
Cada ve que llamamos a randomRIO, tendremos un resultado diferente, incluso con el mismo argumento. Este viola la regla de transparencia referencial. Asi randomRIO, asi como getLine  y putStrLn, es una accion IO.

### 21.1.2 Guardando valores en el contexto de IO 
Lo interesante sobre getLine es que tenemos un valor de retorno util del tipo IO String. Asi como Maybe String significa que tienes un tipo que podria ser olvidado, IO String significa que tienes un tipo que viene de I/O. En la leccion 19 discutimos el hecho de que un gran rango de errores  es causado por valores olvidados que Maybe previene de fugas dentro del codigo. Aunque valores null causan un amplio rango de errores, piensa como muchos errores pueden ser encontrados causados por I/O!

Como I/O es tan peligroso e impredecible, despues de que tenemos el valor desde I/O  Haskell no permite que uses este valor fuera del contexto del tipo IO. Por ejemplo, si tu eliges un numero aleatorio usando randomRIO, no puedes usar este valor fuera de main o una accion IO similar.  Con Maybe podemos usar pattern matching para tomar un valor seguro fuera del contexto este deberia ser olvidado. Esto es porque solo una sola cosa puede ir mal con un tipo Maybe: el valor es Nothing. con I/O, Una interminable variedad de problemas pueden ocurrir. Porque pasa esto, despues de que estuvimos trabajando con datos en el contexto de IO, este debe permanecer ahi. Esto inicialmente podria parecer una carga. Despues de que no familiaricemos con la forma que Haskell separa la logica I/O de todo lo demas, Probablemente querriamos replicar este comportamiento en otros lenguajes de programacion (aunque no tenemos un poderoso sistema de tipos que te fuercen a esto).

## 21.2 Notacion Do
No ser capaz de escapar del contexto de IO significa que necesitamos una forma conveniente de realizar un secuencia de computaciones con el contexto IO. Este es el proposito de la palabra reservada do. Esta notacion do permite tratar con tipos IO como si fueran tipos regulares. Esto tambien explica porque algunas variables usan let y otras usan <-. Variables asignadas con <- te permite actuar como si un tipo IO fuera solo de tipo a. Usamos sentencias let cuando creas variables que no son de tipos IO. La figura 21.1 muestra como 2 lineas en tu accion main usan <-  y ley para entender esto mejor.

Sabiamos que getLine retorna un tipo IO String. El tipo de name debe ser IO String. Pero queremos usar name como un argumento para holaPersona. Mira el tipo de holaPersona de Nuevo.
```hs
holaPersona :: String -> String
```
Como ves holaPersona trabaja solo con String ordinarios, no del tipo IO String. La notacion do permite asignar una variable IO String usando <-, para que actue como un String, ordinario y entonces permite que esta fucncion trabaje como un String regular. 

Volviendo a nuestro programa original de nuevo, esta vez con las anotaciones resaltadas donde usamos IO tipos y tipos regulares
```hs
name <- getLine  -- Este retorna un tipo IO String
  let statement = holaPersona name  -- holaPersona retornan un tipo String
                                    -- como asignamos name usando  <- podemos
                                    -- tratarla como un String normal
```
```hs
holaPersona :: String -> String
holaPersona name = "Hola " ++ " " ++ name ++ "!"

main :: IO ()
main = do
  putStrLn "Hola! Cual es tu nombre?"
  name <- getLine -- retorna un tipo IO String
  let statement = holaPersona name --holaPersona es funcion tipo String->String
  putStrLn statement -- es una accion IO que toma un string normal
```
Lo que hace tan poderoso es que puedes mezclar funciones que trabajan con valores seguros y valores de tipo IO y usar estos sin problemas con datos en un contexto IO.

## 21.3 Un ejemplo: calculadora de costo de pizza en linea de comandos.
Para entender de mejor forma  como la notacion do trabaja, permitenos tratar un ejemplo mas extenso. Crearemos una herramienta en linea de comandos que pregunta la usuario por el tamanio el  costo de 2 pizzas, y entonces dice al usuario cual es mas barata por pulgada cuadrada. Como estamos usando IO ahora, podemos crear un programa compilado realmente. llamaremos a este **pizza.hs** Este programa preguntara por el costo el tamanio de dos pizzas y te dira cual es mejor en terminos de su costo por pulgada cuadrada. Aqui una muestra de la compilacion y ejecucion del programa.
```hs
$ ghc pizza.hs
$ ./pizza
What is the size of pizza 1
12
What is the cost of pizza 1
15
What is the size of pizza 2
18
What is the cost of pizza 2
20
The 18.0 pizza is cheaper at 7.859503362562734e-2 per square inch
```
Cuando disenamos programas que usan I/O en Haskell, esto significa escribir mas codigo que no usa tipos IO. Esto hace que razonar sobre problemas mas facil y permite facilmente testear y experimentar con funciones puras. La mayoria del codigo que escribes no esta en el contexto de IO. La mayoria del codigo que conoces no sera vulnerable a errores IO.

Para comenzar necesitamos una funcion que calcule el costo de una pizza dado su diametro. La primera cosa que necesitas es calcular el area de una circulo dado su diametro. El area de un circulo es igual a pi*radio^2, y el radio es la mitad del diametro
```hs
areaDadaDiametro :: Double -> Double
areaDadaDiametro size = pi*(size/2)^2
```
Usaremos el par tamanio/costo para hacer mas facil la representacion de la pizza. Podemos usar un tipo sinonimo para esto.
```hs
type Pizza = (Double, Double)
```
Pra calcular el costo por pulgada cuadrada, dividimos el costo total por el area.
```hs
costoPorPulgada :: Pizza -> Double
costoPorPulgada (size, cost) = cost / areaDadaDiametro size
```
A continuacion comparamos 2 pizzas. la funcion comparaPizzas toma dos pizzas y retornamos la mas barata de las 2.
```hs
compararPizzas :: Pizza -> Pizza -> Pizza
compararPizzas p1 p2 = if costP1 < costP2
                       then p1
                       else p2
  where costP1 = costoPorPulgada p1
        costP2 = costoPorPulgada p2
```
Finalmente si quieres imprimir una oracion al usuario que indique que pizza es mas barata y su precio por pulgada cuadrada.
```hs
describePizza :: Pizza -> String
describePizza (size, cost) = "La pizza de tamanio " ++ 
                             show size ++ "es mas barato " ++
                             show costoSqInch ++
                             "por pulgada cuadrada"
  where costoSqInch = costoPorPulgada (size, cost)
```
Ahora que tenemos todo esto hecho lo juntaremos en un main. Este es todavia un problema interesante a resolver. getLine retorna un IO String, pero necesitamos valores del tipo Double. Para resolver esto usamos read.
```hs
main :: IO ()
main = do 
  putStrlLn "Cual es el tamanio de la pizza 1"
  size1 <- getLine
  putStrlLn "Cual es el costo de la pizza 1"
  cost1 <- getLine
  putStrlLn "Cual es el tamanio de la pizza 2"
  size2 <- getLine
  putStrlLn "Cual es el costo de la pizza 2"
  cost2 <- getLine
  let pizza1 = (read size1, read cost1)
  let pizza2 = (read size2, read cost2)
  let betterPizza = compararPizzas pizza1 pizza2
  putStrlLn (describePizza betterPizza)
```
La clave aqui es que debemos preocuparnos sobre las partes del programa que esta hecho en el contexto de IO, que es quien captura y manipula tus entradas.

### 21.3.1 Una ojeada a las Monadas-notacion do y Maybe
IO puede usar la notacion do porque es un miembro de una poderosa clase de tipos llamada Monad. Discutiremos monadas en la unidad 5. La notacion do no tiene nada que hacer con IO en particular y puede ser usado por cualquier miembro de Monad para realizar computaciones en un contexto. El contexto para valores en un Maybe es que ellos podrian no existir. El contexto de IO es que estamos interactuando con el mundo real y tus datos podrian no comportarse como lo hacen en el resto de tu programa Haskell.

Maybe es tambien un miembro de la clase de tipo Monad y mas aun puede usar la notacion do. Supon que en lugar de obtener los valores de pizza de la entrada de usuario, devuelves estos valores de 2 Maps: uno con tamanios y otro con costos. Aqui un programa casi identico al programa escrito usando solo Maybe. En lugar de usar la informacion de un usuario, buscaremso el costo de la pizza por ID en n Map costData
```hs
costData :: Map.Map Int Double
costData = Map.fromList [(1,18.0),(2,16.0)]
```
Igualmente, tamanio esta en otro Map
```hs
sizeData :: Map.Map Int Double
sizeData = Map.fromList [(1,20.0),(2,15.0)]
```
Ahora tenemos una funcion maybeMain que luce casi igual.
```hs
maybeMain :: Maybe String
maybeMain = do
  size1 <- Map.lookUp 1 sizeData
  cost1 <- Map.lookUp 1 costData
  size2 <- Map.lookUp 2 sizeData
  cost2 <- Map.lookUp 2 costData
  let pizza1 = (size1,cost1)
  let pizza2 = (size2,cost2)
  let betterPizza = comparePizzas pizza1 pizza2
  return (describePizza betterPizza)
```
La unica cosa nueva que hemos adicionado es el return de la funcion, que toma un valor de un tipo y pone este dentor del contexto de la notacion do. En este caso, un String es retornado como un Maybe String. No necesitas hacer esto en tu funcion main porque putStrLn retorna un tipo IO (). En GHCi, puedes ver que esto trabaja.
```hs
GHCi> maybeMain
Just "The 20.0 pizza is cheaper at 5.729577951308232e-2 per square inch"
```
Si has escuchado antes de monadas y estas entusiasmado por esto, puedes encontrar este ejemplo descepcionante. Pero el tipo Monad te permite escribir programas generales que pueden trabajar en un amplio rango de contexto. Asi con notacion do, puedes escribir un programa diferente, usando el mismo nucleo de funciones como el original. En La mayoria de otros lenguajes de programacion, tendrias que reesecribir toda la funcion para traducir este de uno que usa IO a uno que trabaja con valores potencialmente null en un diccionario. En la unidad 5, iremos mas profundo en este tema.Por ahora, esta perfectamente bien pensar que la notacion do es una forma conveniente de realizar acciones IO en Haskell.