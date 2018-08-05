En este fin de unidad , modelaresmos series temporales de datos usando herramientas construidas con haskell. datos Series temporales, es en teoria, relativamente simple: tiene una serie de valores y fechas para cada pieza de informacion. Por ejemplo datos de venta a partir de datos de Box&Jenkins que se configuran comunmente para demostrar una serie temporal (los datos usados en este capstone es tambien un subconjunto de los primeros 36 meses de estos mismos datos).
Aunque conceptualmente es facil trabajar con ellos, en la practica series temporales de datos presentan muchos cambios interesantes. A menudo datos faltantes necesitan multiples combinaciones con conjuntos de datos incompletos, en entonces necesitamos realizar analiticas en estos datos confusos, que a menudo requieren otras transformaciones para darles sentido. En este capstone, usaremos tecnicas cubiertas en esta unidad para hacer herramientas que trabajen con datos de series temporales. Exploraremos como combinar multiples series temporales en una sola, hacer sumario de estadisticas (tal como el promedio) de datos de series temporales con valores faltantes, y concluimos haciendo transformaciones sobre los datos tal como suavizado y eliminar ruido.

Todo el codigo de esta seccion estara en un archivo time_series.hs. los imports deberian estar hasta arriba del archivo.
```hs
import Data.List
import qualified Data.Map as Map
import Data.Semigroup
import Data.Maybe
```
## 20.1 Tus Datos y el tipo de datos TS
Supon que hemos comenzado a trabajar en una nueva compania y hemos estado haciendo tareas de organizacion y datos financieros. Tenemos 36 meses de (parcial) datos financieros que necesitas que tengan sentido. Los datos estan contenidos en 4 archivos, y ningun archivo tiene un conjunto de datos completo.
Como no hemos trabajado con archivos todavia, que hemos leido los datos que teniamos. Representaremos cada archivo como listas de tuplas (Int, Double)
```hs
file1 :: [(Int,Double)]
file1 = [ (1, 200.1), (2, 199.5), (3, 199.4)
        , (4, 198.9), (5, 199.0), (6, 200.2)
        , (9, 200.3), (10, 201.2), (12, 202.9)]

file2 :: [(Int,Double)]
file2 = [(11, 201.6), (12, 201.5), (13, 201.5)
        ,(14, 203.5), (15, 204.9), (16, 207.1)
        ,(18, 210.5), (20, 208.8)]

file3 :: [(Int,Double)]
file3 = [(10, 201.2), (11, 201.6), (12, 201.5)
        ,(13, 201.5), (14, 203.5), (17, 210.5)
        ,(24, 215.1), (25, 218.7)]

file4 :: [(Int,Double)]
file4 = [(26, 219.8), (27, 220.5), (28, 223.8)
        ,(29, 222.8), (30, 223.8), (31, 221.7)
        ,(32, 222.3), (33, 220.8), (34, 219.4)
        ,(35, 220.1), (36, 220.6)]
```
Cuando trabajamos con los datos de la compania, es comun encontrar un patron similar: tenemos los datos divididos en muchos archivos. los datos en los archivos tienen puntos faltantes, y hay sobreposicion entre los datos tambien. Si quieres ser capaz de hace lo siguiente:
- Apuntar estos archivos juntos facilmente
- Guardar un rastro de los datos faltantes
- Realizar analisis sobre series temporales sin preocuparse sobre los errores debido a valores faltantes.

Cuanto apuntemos lineas te tiempo juntas, combinaremos 2 lineas de tiempo para hacer una nueva.Este es un patron familiar cuando discutimos semigrupos. Puedes resolver el problema de apuntar juntos series de tiempos individuales para hacer tus series de tiempos una instancia de Semigroup. Si quieres combinar una lista de elementos de series de tiempos, tambien quisieramos implementar Monoid para usar mconcat. Para trabajar con valores faltantes, tomaremos la ventaja del tipo Maybe. Usando muestreo de patrones cuidadosamente  sobre valores Maybe, puedes realizar funciones sobre datos de series temporales y manejar el caso de valores faltante.

### 20.1.1 Contruyendo un tipo time-series basico
Si necesitas un tipo basico para tus series temporales. Simplificaremos las cosas, considerando que todos tus datos son solo Ints, que seria in indice relativo. Teniendo 36 meses,dias,o milisegundos de datos podria ser representado por los indices de 1-36. Para los valores en el tipo series, usaremos un tipo parametrico porque no queremos restringir el tipo de valores que vamos a permitir en tus series temporales. En este caso, queremos un tipo Double, pero podriamos tener series con Bools ("Se lograron la metas de venta?") o Series temporales de Strings ("Quien es principal de ventas?"). El tipo que usamos para representar  las series de tiempo sera un tipo parametrizado \*->\*  un tipo parametrizado que toma solo un argumento. Si quieres  usar le tipo Maybe para tus valores porque tener valores faltantes es un problema comun cuando trabajamos con cualquier dato. En analitica de datos, valores faltantes son referidos comunmente como tener un valor NA (por not available, como opuesto a Null en software). Aqui la definicion del tipo TS.
```hs
data TS a = TS [Int] [Maybe a]
```
A continuacion creamos una funcion que toma una lista de tiempos y una lista de valores y creamos un tipo TS. Como con los datos en tus archivos, asumiremos que los tiempos no deberian ser perfectamente contiguos cuando creamos un tipo TS. Cuando  usamos createTS, expandiremos la linea de tiempo a espacios contiguos. Entonces crearemos un Map para usar los tiempos y valores existentes. Mapearemos sobre la lista completa de tiempos y buscamos el tiempo en tu Map. Este automaticamente creara un maybe  una lista de tus valores, donde los valores existentes seran  un valor Just o un NA representado por Nothing.
```hs
createTS :: [Int] -> [a] -> TS a 
createTS times values = TS completeTimes extendedValues
  where completeTimes = [minimum times .. maximum times]
        timeValueMap = Map.fromList (zip times values)
        extendedValues = map (\v -> Map.lookup v timeValueMap)
                             completeTimes
``` 
Los archivos no estan en el formato correcto para la funcion createTS, asi que haremos una funcion helper que unzip los pares.
```hs
fileToTS :: [(Int,a)] -> TS a
fileToTS tvPairs = createTS times values
  where (times, values) = unzip tvPairs
```
Antes de avanzar mas, es bueno hacer una instancia de Showpara tu objeto TS. Primero crearemos una funcion que muestre el par tiempo/valor
```hs
showTVPair :: Show a =>  Int -> (Maybe a) -> String
showTVPair time (Just value) = mconcat [show time, "|",show value, "\n"]
showTVPair time Nothing = mconcat [show time, "|NA\n"]
```
Ahora hacemos una instancia de Show para usar zipWith y la funcion ShowTVPair.
```hs
instance Show a => Show (TS a) where
  show (TS times values) = mconcat rows
     where rows = zipWith showTVPair times values

-- si evaluamos tendremos
GHCi> fileToTS file1
1|200.1
2|199.5
3|199.4
4|198.9
5|199.0
6|200.2
7|NA
8|NA
9|200.3
10|201.2
11|NA
12|202.9
```
A continuacion convertimos todos los archivos a tipos TS
```hs
ts1 :: TS Double
ts1 = fileToTS file1

ts2 :: TS Double
ts2 = fileToTS file2

ts3 :: TS Double
ts3 = fileToTS file3

ts4 :: TS Double
ts4 = fileToTS file4
```
Ahora que tenemos todos tur archivos de datos convertidos a tipos TS qu pueden tambien imprimir en pantalla es facil experimentar con ellos. A continuacion resolveremos el primer problema, combinar archivos usando Semigroup y Monoid.

## 20.2 Apuntando juntos dato TS junto a Semigroup y Monoid
Con tu modelo basico de series temporales, queremos resolver el problema de apuntar juntas series temporales. Pensando este problema con tipos tenemos la siguiente signatura:
```hs
Ts a -> Ts a -> Ts a
```
necesitamos una funcion que tome dos tipos TS y retorne solo uno. Este tipo de signatura te deberia recordar una patron familiar. Si buscamos el tipo del operador <> de Semigroup, veras que es una generalizacion del tipo signatura que estabamos viendo
```
(<>) :: Semigroup a => a -> a -> a
```
Esta es buena senal que queremos acer Ts una instancia de Semigroup. Ahora hay que considerar como vamos a combinar los tipos TS.

Dado que el tipo TS es basicamente 2 listas, puede pensar tentativo pensar que puedes cocatenar 2 listas para cahr un tipo nuevo TS. Pero tenemos 2 problemas por resolver que hacer diferente de concatenar una lists de otra. Lo primero es que los puntos de los datos estan todos ligados por el rango en un archivo independiente; por ejemplo, file2 contiene valores para la fecha 11, pero file1 incluye para la fecha 12. El otro problema es que 2 series temporales tendria conflictos de valores para un solo punto en una fecha. Archivos 1 y 2 ambos contienen informacion de la fecha 12, pero ellos no son acordes el uno con el otro. Puedes resolver este problema teniendo un segundo archivo que tenga mas prioridad.

Puedes usar Map para resolve ambor problemas. Comenzamos tomando los pares tiempo/valor en el primer TS y los usaremos para construir un Map de pares tiempo/valor. Entonces insertaremos el par tiempo/valor del segundo TS.  Esto combinara sin problemas los 2 conjuntos de pares y manejara la sobreescritura de valores duplicados. 

Lo importante a realizar es que el Map para combinar todos los datos de ambas series  sera un tipo Map k v. donde k es la llave del tipo y v sera el valor del tipo. Ambos valores usando Ts sesran k y Maybe v. necesitas una pequena funcion de ayuda que permita insertar pares de tipo (k, Maybe v)  dentro de un Map de tipo k v. El siguiente es tu funcion insertMaybePair.
```hs
insertMaybePair myMap (_,Nothing) = myMap
insertMaybePair myMap (key,(Just value)) = Map.insert key value myMap
```
Con insertMaybePair, tienes las herramientas que necesitas para combinar 2 tipos TS en uno nuevo, seras capaz de juntar sin problemas cualquier conjunto de datos.
```hs
combineTS :: Ts a -> Ts a -> TS
combineTS (TS [] []) ts2 = ts2
combineTS ts1 (TS [] []) = ts1
combineTS (TS t1 v1) (TS t2 v2) = TS completeTimes combinedValues
   where bothTimes = mconcat [t1,t2]
         completeTimes = [minimun bothTimes .. maximum bothTimes]
         tvMap = foldl insertMaybePair Map.empty (zip t1 v1)
         updatedMap = foldl insertMaybePair tvMap (zip t2 v2)
         combinedValues = map (\v -> Map.lookup v updatedMap) completeTimes
```
Aqui vemos como combineTS trabaja: Lo primero que necesitas es resolver los casos que uno (o ambos) de los tipos TS son vacios. En este caso, retornamos el que no es vacio (o si ambos son vacios, uno vacio). Si tienes dos tipos TS no vacios, los combinamos primer combinando todos tiempos que ellos cubren. Usanod esto, puedes crear una linea te tiempo continua cubriendo los posibles tiempos. Entonces insertamos todos los valores existentes para el primer tipo TS en el Map usando insertMaybePair y foldeamos sobre una lista de pares valor/tiempo creados con zip e inicializamos la funcion foldl con un Map vacio. Despues de esto insertamos valores del segundo TS de la misma forma, solo que en lugar de usar foldl con una Map vacio, usamos el Map creado en el ultimo paso. Para insertar el segundo despues del primero, sabemos que el segundo tipo TS tiene los datos finales para cualquier duplicado. Finalmente, buscamos todos los valores en el Map en ambos tipos TS, que da una lista valores Maybe como en la funcion createTS.

Y combineTS es todo lo que necesitas implementar en un Semigroup! Podrias poner toda esta logica directamente en la definicion de <>. Personalmente, Encuentro mas facil separar la funcion con fines de depuracion.

Par evitar la duplicacion, es mejor pegar la definicion de combineTS como la definicion de <>. Pero para este ejemplo, definiremos <> como combineTS
```hs
instance Semigroup (TS a) where
   (<>) = combineTS
```  
Con TS en una instancia de Semigroup, puedes combinar ahora series temporales, automaticamente llenando valores faltantes y sobreescribiendo los valores duplicados.

### 20.2.1 Haciendo Ts una instancia de Monoid
Ser capaces de combinar 2 o mas tipos TS con <> es muy util. Pero dado que solo tenemos 4 archivos para combinar, seria incluso mas bonito combinar una lista de ellos.

Pensando en tipos de nuevo, tendremos esta signatura para describir el comportamiento que queremos 
```hs
[TS a] -> TS a
```
Buscanto este tipo de signatura deberiamos recordar la concatenacion de listas, que se hace con la funcion mconcat. El tipo de signatura de mconcat generaliza este patron.
```hs
mconcat :: Monoid a =>  [a] -> a
```
La unica cosa faltante ahora es que tu tipo TS no es una instancia de Monoid.

Como siempre, depues de haber implementado Semigroup, lo que necesitamos adicionar es el elemento mempty (que es la identidad). Sin un elemento identidad, no puedes concatenar automaticamente una lista de tipos TS.
```hs
instance Monoid (TS a) where
   mempty = TS [] []
   mappend = (<>)
```
Obtuvimos mconcat de forma libre con Monoid, podemos facilmente combinar lista de TS.
```hs
GHCi> mconcat [ts1,ts2]
1|200.1
2|199.5
3|199.4
4|198.9
5|199.0
6|200.2
7|NA
8|NA
9|200.3
10|201.2
11|201.6
12|201.5
13|201.5
14|203.5
15|204.9
16|207.1
17|NA
18|210.5
19|NA
20|208.8
```
Finalmente, podemos apuntar juntos todas las series temporales en una serie temporal ahora es posible a partir de todos tus archivos.
```hs
tsAll :: TS Double
tsAll = mconcat [ts1,ts2,ts3,ts4]
```
Aunque esto toma un poco de trabajo llegar aqui, para todos los datos de series temporales futuras con las que trabajes, tenemos una manera de segura de combinar archivos separados en un solo tipo TS.