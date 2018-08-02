Las clases de tipos pueden ser a menudo mucho mas abstractas que interfaces en OOP, tipos parametrizados juegan un rol mayor que los genericos de la mayoria de lenguajes. ESta leccion introduce un importate tipo parametrizado: Maybe. A diferencia de List o Map, que representan contenedores de valores, **Maybe es el primero de muchos tipos que veremos para representar contextos** para un valor. tipos Maybe representa valores que podrian estar faltando. En la mayoria de lenguajes, un valor faltante, es representado por el valor *null*. Para usar un contexto representando un valor que debera estar faltando, el tipo Maybe te permite escribir codigo mas seguro. Debido al poder del tipo Maybe, errores relacionados a valores null son sistematicamente removidos de programas Haskell.

## 19.1 Introduciendo Maybe: resolviendo valores faltantes con tipos

Al final de la leccion 18, estuvimos trabajando en organizar una coleccion de organos humanos de un cientifico loco. Usamos el tipo Map para almacenar una lista de organos para una busqueda facil. Permitenos continuar explorando el ejercicio. Aqui el codigo importante de la leccion precedente:
```hs
import qualified Data.Map as Map
data Organ = Heart | Brain | Kidney | Spleen deriving (Show, Eq)

organs :: [Organ]
organs = [Heart, Heart,Brain,Spleen,Spleen,Kidney]

ids :: [Int]
ids = [2,7,13,14,21,24]

organPairs :: [(Int, Organ)]
organPairs = zip ids organs

organCatalog :: Map.Map Int Organ
organCatalog = Map.fromList organPairs
```
Todo ha ido bien hasta que decidimos usar Map.lookup para buscar un Organ en tu Map. Cuando hacemos esto, pasamos a traves de un nuevo tipo, Maybe.
Maybe es un simple pero poderoso tipo. Hasta ahora, todos nuestros tipos parametrizados han sido vistos como contenedores. Maybe es diferente. Maybe es mejor entenderlo como un tipo en un contexto. El contexto en este caso es que el tipo contenido debe ser faltante. Aqui una definicion.
```hs
data Maybe a = Nothing | Just a
```
Algo de un tipo Maybe puede ser o Nothing o Just solo del tipo a. Que es lo que en este mundo podria significar? Permitenos abrir GHCi y ver que pasa:
```hs
> Map.lookup 13 organCatalog
Just Brain
```
Cuando busquemos in ID que esta en el catalogo, tendremos el constructor de datos Just y el valor que se espera para el ID. Si buscamos el tipo de este valor, tendremos:
```hs
Map.lookup 13 organCatalog :: Maybe Organ
```
En la definicion de lookup, el tipo retornado es Maybe a. Ahora que hemos usado lookup, el tipo retornado esta hecho concreto y el tipo es Maybe Organ. El tipo Maybe Organ mas o menos significa: Este dado *deberia* ser una instancia de Organ. Cuando no deberia ser? Permitenos ver que pasa cuando preguntamos  por el valor de un ID que sabemos que no esta en la coleccion:
```hs
Map.lookup 6 organCatalog
Nothing
```

## 19.2 El problema con null
El organCatalog no tiene el valor 6. En la mayoria de lenguajes de programacion, una de 2 cosas pasaria si buscamos un valor que no esta en el diccionario. Ocurre un error o obtenemos un valor null. Ambas respuestas tienen mayores problemas.

### 19.2.1 Manejando valores faltantes con errores
En el caso de lanzar un error, muchos lenguajes no requieren que atrapemos errores que deberian ser lanzados. Si un programa requiere un ID que no esta en el diccionario. el programador debe recordar recoger el error, o si no el programa podria romperse (crash). Adicionalmente, el error deberia ser manejado al mismo tiempo que la excepcion es lanzada. Este no deberia ser un grna problema, porque esto deberia ser sabio par siempre para el error en su fuente. Pero supon que quieres manejar el caso de un Spleen faltante diferente de un Heart faltante.
Cuando el error de ID faltante es disparado, es posible que no tenga informacion para manejar apropiadamente los diferentes casos de tener un valor faltante.

### 19.2.2 Retornando valores null
Retornar null tiene mas problemas discutibles. el problema mas grande es que el programador de nuevo tiene que recordar verificar los valores null siempre que un valor que puede ser null va a ser usado. No hay forma que el programa forzar al programador recordar la verificacion. Valores Null son tambien extremadamente propensos a causar un error porque ellos no se comportan tipicamente como el valor que el programa espera. Una simple llamada de toString pueder facilmente causar un valor null o lanzar un error en una parte del programa. Si eres desarrollador Java o C#, la mera frase null pointer exception deberia ser argumento suficiente que el valor null es complicado.

### 19.2.3 Usando Maybe como una solucion para valores olvidados
Maybe resuelve todos estos problemas un una forma inteligente. Cuando una funcion retorna un valor del tipo Maybe, el programa no puede usar este valor sin tratar con el hecho que el valor esta envuelto en un Maybe. Valores faltantes pueden nunca causar error en Haskell porque Maybe hace esto imposible olvidar que un valor podria ser null. Al mismo tiempo, el programador nunca debe preocuparse sobre esto hasta que sea absolutamente necesario. Maybe es usado en todos los tipicos lugares que el valor Null puede aparecer, incluido estos:
- Abrir archivos que podrian no existir.
- Leer de una base de datos que podria tener valores null.
- Hacer un requerimiento API RESTful a un recurso potencialmente faltante.

La mejor forma de ilustrar la magia de Maybe es con codigo. Permitenos ahora asistir al cientifico loco. Periodicamente necesitamos hacer un inventario  para descifrar que nuevas partes de cuerpos deben ser recolectados. No podemos recorddcar que gabinete tiene que parte, o incluso si no tiene nada en ellos. La unica forma de consultar todos los gabinetes e usar todos los ID en el rango de 1 a 50.
```hs
possibleDrawers :: [Int]
possibleDrawers = [1 .. 50]
```
A continuacion necesitamos una funcion que obtenga el contenido de cada gabinete. El siguiente mapea esta lista de posibles gabinetes con la funcion lookup.
```hs
getDrawerContents :: [Int] -> Map.Map Int Organ -> [Maybe Organ]
getDrawerContents ids catalog = map getContents ids
   where getContents = \id -> Map.lookup id catalog
```
Con getDrawerContents, estamos listos para buscar en el catalogo.
```hs
availableOrgans :: [Maybe Organ]
availableorgans = getDrawerContents possibleDrawers organCatalog
```
Si este hubiera sido un lenguajes de programacion que maneja excepciones o nulls, tu programa ya hubiera explotado. Nota que tus tipos es todavia una List de Maybe Organ. Nota que tambien evitamos el problema de retornar un valor especial null. No hay forma de hacer esto con esta lista, hasta que trates explicitamente con esta posibilidad de valores faltantes, deberias guardar este dato como un tipo Maybe.

Para finalizar necesitamos ser capaces de obtener una cuenta de un organo en particular en la que estes interesado.En este punto, necesitamos tratar con Maybe.
```hs
countOrgan :: Organ -> [Maybe Organ] -> Int
countOrgan organ available = length (filter  (\x -> x == Just organ) available)
```
Lo interesante aqui es que ni siquiera tenemos que remover el organo del contexto Maybe. Maybe implementa Eq, asi que puede solo comparar dos Maybe organs. No solo no tienes que manejar cualquier error, porque tu computacion nunca tratara con valores que no existen, nunca tendras que preocuparte sobre manejar este caso! Aqui el resultado final:
```hs
> countOrgan Brain availableOrgans
1
> countOrgan Heart availableOrgans
2
```

## 19.3 Calculando con Maybe

Seria muy util ser capaz de imprimir la lista de availableOrgans para poder ver lo que tenemos. Ambos tipos Organ y Maybe soportan Show para poder imprimir  fuera de GHCi.
```hs
show availableOrgans [Nothing, Just Heart, Nothing, Nothing,Nothing,Just Heart,....]
```
Aunque hemos conseguido que se impriman esto esta feo, La primera cosa que queremos hacer es remover todos los valores Nothing. Puedes usar filter y patrones de muestreo para lograr esto.
```hs
isSomething :: Maybe Organ -> Bool
isSomething Nothing = False
isSomething (Just _) = True
```
Y ahora podemos filtrar la lista de organos que no son faltantes.
```hs
justTheOrgans :: [Maybe Organ]
justTheOrgans = filter isSomething availableOrgans

-- en GHCi vemos la mejora
> justTheOrgans
[Just Heart, Just Heart, Just Brain, Just Spleen, Just Spleen, Just Kidney]
```
El problema es que todavia tenemos el constructor da datos Just en frente de todos. Podemos limpiar esto con patrones de muestreo tambien. Haremos la funcion showOrgan que cambiara Maybe Organ a un String. Puedes adicionar el patron Nothing incluso si no lo necesitamos esto porque es un buen habito siempre muestrear todos los patrones en cada caso.

*isJust y isNothing El modulo Data.Maybe contiene 2 funciones, isJust y isNothing, que resuelve el caso generalde manejo de valores Just. isJust es identico a la funcion isSomething pero trabaja sobre todos lo tipos Maybe. Con Data.Maybe importado, puedes resolver este problema asi: justTheOrgans filter isJust availableOrgans*
```hs
showOrgan :: Maybe Organ -> String
showOrgan (Just organ) = show organ
showOrgan Nothing = ""

-- vemos como trabaja en GHCi
> showOrgan (Just Heart)
"Heart"
> showOrgan Nothing
""
```
Ahora podemos mapear la funcion showOrgan sobre justTheOrgans
```hs
organList :: [String]
organList = map showOrgan justTheOrgans
```
Como toque final, insertaremos comas para hacer la lista mas bonita. Puedes usar la funcion intercalate (palabra lujosa para insertar) que esta en el modulo Data.List (asi que necesitamos adicionar Data.List arriba del archivo)
```hs
cleanList :: String
cleanList = intercalate ", " organList

> cleanList 
"Heart, Heart, Brain, Spleen, Spleen, Kidney"
```

## 19.4  De vuelta al laboratorio Calculos mas complejos con Maybe
Supon que necesitamos hacer varias cosas para evaluar en un Maybe. El cientifico loco tiene mas proyectos interesantes. Hemos dado un ID de gabinete. Necesitamos devolver un item del gabinete. Entonces ponemos el organo en el contenedor apropiado (un valdo, un refrigerador o una bolsa). Finalmente, ponemos el contenedor en la localizacion correcta. Aqui las reglas para contenedores y localizaciones:
Para contenedores:
- Brains van a un valde.
- Hearts a un refrigerador
- Spleens y kidneys van a una bolsa
Para localizaciones
- Vats y coolers van al laboratorio
- Bags van a la cocina 
Comenzaremos escribiendo esto, asumiendo que todo va bien y no tienes que preocuparte por Maybe.
```hs
data Container = Vat Organ | Cooler Organ | Bag Organ

instance Show Container where
   show (Vat organ) = show organ ++ " in a vat"
   show (Cooler organ) = show organ ++ "in a cooler"
   show (Bag organ) = show organ ++ " in a bag"

data Location = Lab | Kitchen | Bathroom deriving Show

organToContainer :: Organ -> Container
organToContainer Brain = Vat Brain
organToContainer Heart = Cooler Heart
organToContainer organ = Bag organ

placeInLocation :: Container -> (Location,Container)
placeInLocation (Vat a) = (Lab, Vat a)
placeInLocation (Cooler a) = (Lab, Cooler a)
placeInLocation (Bag a) = (Kitchen, Bag a)
```
Una funcion, process, manejara tomando un Organ y poniendolo en el contenedor y localizacion apropiado. Entonces la funcion report tomara tu contenedor y localizacion, dara a la salida el reporte al cientifico.
```hs
process :: Organ -> (Location, Container)
process organ = placeInLocation (organToContainer organ)

report :: (Location, Container) -> String
report (location, container) = show container ++ " in the " ++ show location
```
Estas 2 funciones son escritas asumiendo que ningun organo falta. Puedes testear como trabajaantes de preocuparte de trabajar en el catalogo.
```hs
GHCi> process Brain
(Lab,Brain in a vat)
GHCi> process Heart
(Lab,Heart in a cooler)
GHCi> process Spleen
(Kitchen,Spleen in a bag)
GHCi> process Kidney
(Kitchen,Kidney in a bag)
GHCi> report (process Brain)
"Brain in a vat in the Lab"
GHCi> report (process Spleen)
"Spleen in a bag in the Kitchen"
```
Todavia no hemos manejado el Maybe Organ a la salida del catalogo. En Haskell, otros tipos tales como Maybe manejan muchos casos en software donde las cosas pueden salir mal.
Lo que hemos hecho aqui con la funcion process es un patron comun en Haskell: Separamos las partes del codigo, para lo cual debes preocuparte de un problema,  (por ejemplo valores faltantes) de la que no tienen. A diferencia de la mayoria de lenguajes de programacion, es imposible para valores de Maybe accidentalmente encontrar su forma dentro de process. Imagina que pudiras escribir codigo sobre el que no es posible tener valores null.
Ahora permitenos poner todo junto para tener los datos fuera del catalogo. Queremos algo como la funcion siguiente, excepto que todavia necesitamos manejar el caso de Maybe.
```hs
processRequest :: Int -> Map.Map Int Organ -> String
processRequest id catalog = report (process organ)
   where organ = Map.lookup id catalog
```
El problema es que tu valor organ es un tipo Maybe Organ y este process toma un Organ. Para resolver esto dada la herramienta que tenemos ahora, tenemos que combinar report y process dentro una funcion que maneje Maybe Organ.
```hs
processAndReport :: (Maybe Organ) -> String
processAndReport (Just Organ) = report (process organ)
processAndReport Nothing = "error, id not found"

-- ahora podemos usar esta funcion para procesar el requerimiento.

processRequest :: Int -> Map.Map Int Organ -> String
processRequest id catalog = processAndReport organ
  where organ = Map.lookup id catalog

-- La funcion maneja ambos null y organos existentes.
GHCi> processRequest 13 organCatalog
"Brain in a vat in the Lab"
GHCi> processRequest 12 organCatalog
"error, id not found"
```
Hay un problema menor desde la perspectiva de diseno. ahora tu funcion processRequest maneja reportando cuando hay un error. Idealmente, te gustaria una funcion report que maneje esto. Pero hace que el conocimiento vaya mas alla. Tendrias que reescribir process para aceptar un Maybe. Estariamos en una situacion peor, porque no tendriamos mas la ventaja de escribir una fucnion processing que pueda garantizar que no tengas que preocuparte de valores faltantes.
