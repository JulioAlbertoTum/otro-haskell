## 11.1 Tipos en Haskell

Haskell es un lenguaje estaticamente tipado. En haskell no tienes que escribir ninguna informacion sobre el tipos de los valores que estan usando. Haskell hace la asignacion por ti. Haskell usa tipado por inferencia para determinar automaticamente los tipos de todos los valores en tiempo de compilacion tomando en cuenta como son usados. No necesariamente se debe depender de haskell para asignar tipos
```hs
x :: Int -- asignacion de tipo para una variable
x = 2
```
todos los tipos en haskell comienzan con una letra mayuscula para distinguirse de las funciones ( que comienzan con una letra o _) El tipo **Int** es una de los mas comunes y tradicionales en programacion. Int representa como las computadoras interpretan un numero por un numero fijo de bits. Por lo que existe un minimo y maximo para la representacion.
Cuando se excede alguno de los limites este retorna 0. Int es una etiqueta que le dice a la computadora como leer y entender memoria fisica. En haskell los tipos proveen una forma de entender como los valores se comportan y como se organizan los datos.
El tipo **Integer** se acerca mas a un entero en sentido matematico es decir cualquier numero entero.Integer no tiene limitaciones de memoria.
Haskell tiene todos los tipos comunes en otros lenguajes.
```hs
letter :: Char
letter = 'a'

interestRate :: Double
interestRate = 0.375

isFun :: Bool
isFun = True

values :: [Int]
values = [1,2,3]

testScores :: [Double]
testScores = [0.99,0.7,0.8]

letters :: [Char]
letters = ['a','b','c']

aPet :: [Char]
aPet = "cat"   -- una lista de caracteres es un string

anotherPet :: String -- Podemos usar String en lugar de [Char] ambas significan lo mismo.
anotherPet = "dog"
```
Otro tipo  importante es **Tuple**. Usamos tuplas antes. No son tan diferentes de una lista, pero son algo mas sofisticadas. Dos diferencias son que cada tupla tiene una tamanio especifico, y  pueden contener multiples tipos. Una lista de tipo [Char] es un string de cualquier tamanio. mientras que el tipo (Char) es una tupla de exactamente un caracter.
```hs
ageAndHeight :: (Int, Int)
ageAndHeight = (32, 77)
```
Las tuplas son utiles para modelar tipos de datos simples de forma rapida.
## Tipos de Funciones
Las funciones tambien tienen signaturas de tipo. En haskell **->** es usado para separar argumentos y retornar valores. 
```hs
doble :: Int -> int
doble n = n*2
```
Si quisieramos escribir una funcion para obtener la mitad de un numero entonces sera necesario retornar un Double. 
```hs
half :: Int -> Double
half n = n/2
```
Esto resultara en un error. El problema es que intentas dividir un numero entero a la mitad, y tal cosa no tiene sentido porque has declarado que vas a retornar un Double. necesitas convertir el valor de un Int a un Double. Otros lenguajes harian un casting de un tipo a otro. casting fuerza a un valor ser representado de otra forma. Haskell no tiene estas convenciones para hacer un casting de tipos.en lugar depende de funciones que transforman apropiadamente valores de un tipo a otro. Usamos la funcion fromIntegral.
```hs
half n = (fromIntegral n) / 2
```
Hemos transformado n de un Int a un numero mas generico.  Una buena pregunta seria "porque no llamara fromIntegral sobre 2 tambien". En muchos lenguajes, si quieres tratar un numero literal como un Double, solo necesitas adicinar un decimal a este. Haskell es mas estricto y mas flexible. Estricto porque nunca hace implicita el tipo de conversion como en ruby o python. Y es mas flexible porque en Haskell los numeros literales son polimorficos: Su tipo es determinado en tiempo de compilacion basado en la forma como se usa.
## 11.2.1 Funciones para convertir a y desde una cadena
Uno de los tipos mas comunes de conversion es convertir de un valor de a un entero. Haskell tiene dos utiles funciones que logran esto son **show** y **read** .
```hs
> show 6
"6"
> show 'c'
"'c'"
> show 6.0
"6.0"
```
La funcion **read** trabaja tomando un string y lo convierte a otro tipo. Pero este tiene un pequeno truco. 
```hs
z = read "6"
```
Es imposible decirle que usar (Int, Integen, Double). En este caso, la inferencia de tipo no nos salva. Hay unas pocas formas de fijar esto. Si usas el valor z haskell tomara en cuanta como usar este valor.
```hs
q = z / 2
```
Con esta informacion Haskell ya save como tratar z (como un Double), incluso Si tu representacion strin no tiene un decimal. Otra solucion es explicitamente usada para tu tipo de signatura.
```hs
otroNumero :: Int
otroNumero = read "6"
```
Aunque la signatura de tipos no es necesaria es ampliamente recomendable usarla siempre. Esto es porque en la practica la signatura de tipos ayuda a razonar sobre el codigo que escribimos. Esta anotacion extra ayuda  Haskell a conocer  que valores esperara **read** y hacer nuestras intenciones mas claras en nuestro codigo. Hay otras formas de forzar a haskell a entender que tipo se quiere obtener
```hs
> read "6" :: Int
6
> read "6" :: Double
6.0
```
## 11.2.2 Funciones  con multiples argumentos
Hasta ahora las signaturas vistas han sido simples. Una cosa que frecuentemente confunde a los principiantes es la signatura de tipos para funciones con multiples argumentos.
```hs
makeAddress :: Int -> String -> String -> (Int, String, String)
makeAddress number street town = (number, street, town)
```
Es confuso porque nos hay una separacion clara entre tipos de argumentos y los valores que no estan retornando. La forma mas facil  de recordar que el eltimo tipo es siempre el retorno. Una buena pregunta es  porque este tipo de signatura? La razon es que detras de escena en haskell, todas las funciones toman solo un argumento. Para reescribir makeAddress usamos una serie de lambdas anidadas, como se muestra en la figura.
```hs
makeAddress number street town = (number, street, town)
makeAddressLambda = (\number -> (\street -> (\town -> (number, street, town) )))
```
En este formato cada funcion retorna una funcion  esperando a la siguiente. Asi es como la aplicacion parcial trabaja!
De esta forma se desmitifica las signaturas multiargumento en aplicacion parcial
## Tipos para funciones de primera clase
Las funciones pueden tomar funciones como argumentos y retornar funciones como valores. para escribir esta signatura de tipos. Escribimos la funcion individuales entre parentesis. Por ejemplo, podemos escribir:
```hs
ifEven :: (Int -> Int) -> Int -> Int
ifEven f n = if Even n
             then f n
             else n
```
## 11.3 Tipos variables
Hemos cubierto uan rama comun de tipos y como trabajan en funciones. pero que hay de una funcion simple, que retorna cualquier valor que pasamos a este?.  
```hs
simpleInt :: Int -> Int
simpleInt n = n
simpleChar :: Char -> Char
simpleChar c = c
```
Esto se ve ridiculo, y claramente no es como haskell trabaja, porque la inferencia de tipo es capaz de entender *simple*. Para resolver este problema, haskell tiene tipos variables. Cualquier letra minuscula en una signatura de tipos indica que cualquier tipo puede ser usado en su lugar. La definicion de tipo seria.
```hs
simple :: a -> a
simple x = x
```
Tipos variables son literalmente variables para tipos. Tipos variables trabajan exactamente como variables regulares, pero en lugar de representar un valor, estos representan un tipo. Cuando usas funciones que tienen un tipo variable en su signatura, puedes imaginar Haskell sustituyendo la variable necesaria. 
La signatura de tipos contiene mas de un tipo de variables. Incluso aunque los tipos pueden ser cualquier valor, todos los tipos de la misma variable deben tener el mismo nombre.
```hs
makeTriple :: a -> b -> c -> (a,b,c)
makeTriple x y z = (x, y, z)
```
La razon de usar diferentes nombres para tipos variables es la misma por la que usamos diferentes nombres para variables regulares: ellos pueden contener diferentes valores. En el caso de makeTriple, puedes imaginar un caso en que tienes un String, un Char  y otro String.
```hs
makeTriple :: String -> Char String -> (String, Char, String)

nameTriple = makeTriple "Oscar" 'D' "Grouch"
```
La definicion de makeTriple y makeAddress son bastante identicas. Pero ellos tiene diferente signatura Porque makeTriple usa tipos variables y puede ser usada para clases de problemas mas generales que makeAddress. Por ejemplo, puedes usar makeTriple para reemplazar makeAddress. makeAddress tiene un tipo de signatura mas especifica, puedes hacer mas suposiciones sobre como se comporta. 
Usar diferentes nombres para diferentes variables de tipos no implica que los valores representados por las variables deban ser diferentes
```hs
f1 :: a -> a
f2 :: a -> b
```
f2 es una funcion que produce un rango mas amplio de posibles valores. f1  tiene un comportamiento de tomar un valor y retornar el mismo tipo: Int -> Int, Char -> Char,etc. f2 tiene un rango mas amplio
Int -> Char, Int -> Int, Int->Bool, etc.