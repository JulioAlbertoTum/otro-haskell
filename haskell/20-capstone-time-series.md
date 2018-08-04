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
Ahora que tenemos todos tur archivos de datos convertidos a tipos TS qu pueden tambien imprimir en pantalla es facil experimentar con ellos. A continuacion resolveremos el primer problema, combinar archivos usando Semigroup y Monoid