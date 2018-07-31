## 14.1 Un tipo que necesita clases

Comenzaremos modelando un six-sided die. Una implementacion por defecto es un tipo similar a Bool, solo que con 6 valores. Todos los constructores de datos iran de S1 a S6 para representar los 6 lados 
```hs
data SixSidedDie = S1 | S2 | S3 | S4 | S5 | S6
```
Si quieres implementar alguna clase de tipos util. Quizas la mas importante clase de tipos para implementar sea Show, porque siempre queremos tener una forma facil de mostrar instancias de tu tipo, especialmente en GHCi, mencionamos que podriamos adicionar la palabra  deriving para crear automaticamente una instancia de la clase. Podriamos definir SixSidedDie que de esta forma y llama a este dia.
```hs
data SixSidedDie = S1 | S2 | S3 | S4 | S5 | S6 deriving (Show)
```
En GHCi veremos una version simple de texto para nuestros constructores de datos cuando los tipeamos.
```hs
> S1
S1
> S2
S2
```
Esto es algo aburrido porque  solo estamos imprimiendo los propios constructores de datos, que son mas significativos de una implementacion desde el punto de vista de legibilidad. En lugar de esto permitenos imprimir la palabra en ingles para cada numero.

## 14.2 Implementacion de Show

Para hacer esto, tenemos que implementar primer la clase de tipos, Show. Es solo una funcion (o en el caso de clases de tipos, llamamos a estos **metodos**) que tienes que implementar, show. Ahora lo implementamos.
```hs
instance Show SixSidedDie where
   show S1 = "one"
   show S2 = "two"
   show S3 = "three"
   show S4 = "four"
   show S5 = "five"
   show S6 = "six"
```
Esto es todo ahora puedes retornar a GHCi y veras una salida mas interesante  que la vista con deriving
```hs
> S1
one
> S6
six
```
## 14.3 Clases de tipo y polimorfismo
Una pregunta que deberiamos estar haciendonos es. porque definimos show de esta forma? Porque necesitamos declarar una instancia de una clase de tipos. Sorprendendemente, si remueves tu declaracion de instancia, el siguiente codigo se compilara asi
```hs
show :: SixSidedDie -> String
show S1 = "one"
show S2 = "two"
show S3 = "three"
show S4 = "four"
show S5 = "five"
show S6 = "six"
```
Pero si cargas est codigo en tun GHCi,tendras 2 problemas. Primero, GHCi no podra imprimir tus constructores de datos por defecto. Segundo, incluso si usaste manualmente show, Obtendras un error
```hs
"Ambiguos occurrence 'show'"
```
No hemos aprendido del sistema de modulos de haskell todavia, pero al tratar haskell este tiene la definicion que escribiste de show esta en conflicto con otra que eta definida para la clase de tipo. 
Puedes ver que el problema cuando creas un tipo TwoSidedDie e intentar escribir show para esta.
```hs
data TwoSidedDie = One | Two
show :: TwoSidedDie -> String
show One = "one"
show Two = "two"

-- Obtenemos el error
Multiple declarations of 'show'
```
El problema es que por defecto tenemos mas de un comportamiento para show, dependiendo de tipo que estamos usando. Lo que estas viendo se llama **polimorfismo**. El polimorfismo significa que la misma funcion se comporta de forma diferente dependiendo del tipo de dato con el que se trabaja. Polimorfismo  es importante en programacion orientada a objetos e igualmente en haskell. La OOP equivalente de show podria ser el metodo toString, Una cosa comun sobre cualquier clase es que puede ser retornada como un string. Clases de tipos son una forma de usar polimorfismo en Haskell, es:
```hs
read "10"   ---- > :: Int -> 10
           |
            ---- > :: Double 10.0
```
Ahora que has producidos strings mas expresivos para tu SixSidedDie, sera util determinar que dos dados son el mismo. Esto significa que tienes que implementar la clase Eq. Esto es util tambien porque Eq es la supreclasede Ord. Vimos esta relacion brevemente antes. Hay que decir que Eq es una superclase de Ord significa que toda instancia de Ord debe tambien ser instancia de Eq. Ultimadamente, para comparar el constructor de datos SisSidedDie, que significa implementar Ord, asi que primero que necesitamos implementar Eq. Usando el comando :info en GHCi veremos la definicion de la clase
```hs
class Eq a where
  (==) :: a -> a -> Bool
  (/=) :: a -> a -> Bool
```
Hay que implementar solo dos metodos: el metodo igual (==) y el no es igual (/=). Dado lo inteligente de haskell ha llegado tan lejos, esto podria parecer que necesite mas trabajo que tenga sentido. Despues de todo, si sabes la definicion de (==). la definicion de (/=) es not (==). Seguro, puede haber alguna excepcion para esto, pero en la vasta mayoria de casos, si conoces uno entonces puedes determinar el otro.

Resulta que haskell es lo suficientemente inteligente para resolver esto. Clases de tipo pueden tener implementacion por defecto de los metodos. Si defines (==), Haskell puede descifrar que significa (/=) sin ayuda.
```hs
instance Eq SixSidedDie where
(==) S6 S6 = True
(==) S5 S5 = True
(==) S4 S4 = True
(==) S3 S3 = True
(==) S2 S2 = True
(==) S1 S1 = True
(==) _ _ = False

> S6 == S6
 True
> S5 == S5
 True
> S3 == S2
 False
``` 
Esto es muy util, pero en el mudndo que se supone que debes saber que metodos necesitaras implementar? El comando :info es un gran recurso, pero no es una documentacion completa. Una fuente mas completa de informacion es Hackage, que es la libreria de paquetes centralizada de haskell. hackage.haskell.org. Si vamos a Eq en esta pagina veremos mas informacion de la que incluso necesitamos. Para nuestros propositos, la parte mas importante es una seccion llamada "Minimum complete definition" Para Eq es la siguiente:
```hs
(==) | (/=)
```
Esto es mucho mas util para implementar la clase de tipo Eq, todo lo que tienes que definir es (==) o (/=). solo  es una declaracion de datos, | significa o. Si provees una de estas opciones, Haskell hara el resto por ti.

El uso de Hoogle es aconsejado permite buscar tipos y signatura de tipos.

## 14.5 Implementando Ord
Una de las caracteristicas mas importantes del dado es que hay un orden en sus lados. Ord define un manojo de funciones utiles para comparar un tipo
```hs
class Eq a => Ord a where
   compare :: a -> a -> Ordering
   (<) :: a -> a -> Ordering
   (<=) :: a -> a -> Bool
   (>) :: a -> a -> Bool
   (>=) :: a -> a -> Bool
   max :: a -> a -> a 
   min :: a -> a -> a
```
Afortunadamente, en hackage puedes encontrar que solo se necesita el metodo compare para ser implementado. El metodo compare toma 2 valores de tu tipo y retorna Ordering. Este es un tipo que vimos brevemente cuando aprendimos sobre sort en la leccion 4. Ordering  es como Bool, excepto que tiene 3 constructores
```hs
data Ordering = LT | EQ | GT

-- una definicion parcial es
instance Ord SixSidedDie where
   compare S6 S6 = EQ
   compare S6 _ = GT
   compare _ S6 = LT
   compare S5 S5 = EQ
   compare S5 _ = GT
   compare _ S5 = LT
```
Incluso con usos inteligentes de muestreo de patrones, llenar esta definicion completa sera mucho trabajo.. Imagina cuan grande seria esta definicion  para un dado de 60 lados.

## 14.6 Derivar o no derivar
como hemos visto toda clase ha sido derivable, significa que puedes usar la palabra deriving para implementar automaticamente esta para tu nueva definicion de tipo. Es comun en lenguajes de programacion ofrecer una implementacion por defecto para cosas tal como el metodo equals (que es el minimo a ser usado). La pregunta es, cuando deberia depender de Haskell para derivar tus clases de tipos versus hacer uno mismo?
Veamos Ord. En este caso, es mas sabio usar deriving (Ord), que trabaja mucho mejor en casos de tipos simples. El comportamiento por defecto cuando cuando derivamos Ord es usar el orden en que los constructores de datos son definidos. Por ejemplo considere
```hs
data Test1 = AA | ZZ deriving (Eq, Ord)
data Test2 = ZZZ | AAA deriving (Eq, Ord)

-- en GHCi
> AA < ZZ
True
> AA > ZZ
False
> AAA > ZZZ
True
> AAA < ZZZ
False
```
Con Ord, usando la palabra clave deriving nos salvamos de escribir un monton de codigo innecesario y que puede tener errores pontenciales.
Un caso incluso mas fuerte para el uso de deriving es cuando usas Enum. El tipo Enun permite representar los lados de tus dados como una lista enumerada de constantes. Esto es esencialmente que pensamos cuando nosotros pensamos en un dado asi que esto es util, Aqui una definicion
```hs
class Enum a where
  succ :: a -> a
  pred :: a -> a
  toEnum :: Int -> a
  fromEnum :: a -> Int
  enumFrom :: a -> [a]
  enumFromThen :: a -> a -> [a]
  enumFromTo :: a -> a -> [a]
  enumFromThenTo :: a -> a -> a -> [a]
```
De nuevo, nos hemos salvado de implementar solo 2 metodos: toEnum y fromEnum. Estos metodos traducen tus valores Enum  a unos tel tipo Int. Aqui una implementacion
```hs
instance Enum SixSidedDie where
  toEnum 0 = S1
  toEnum 1 = S2
  toEnum 2 = S3
  toEnum 3 = S4
  toEnum 4 = S5
  toEnum 5 = S6
  toEnum _ = error "No such value"

  fromEnum S1 = 0
  fromEnum S2 = 1
  fromEnum S3 = 2
  fromEnum S4 = 3
  fromEnum S5 = 4
  fromEnum S6 = 5
```
Ahora que hemos visto alguno de los beneficios de Enum. Para comenzar, puedes ahora genera listas de tu SixSidedDie Asi como otros otros valores de Int y Char
```hs
> [S1 .. S6]
[one,two,three,four,five,six]
> [S2,S4..S6]
[two, four, six]
>[S4..S6]
[four, five, six]
```
Esto es genial, pero que pasa si creamos una lista que no tiene fin?
```hs
> [S1 ..]
[one, two, three, four, five, six, ** Exception: No such value**]
```
Obtuvimos un error porque no manejamos el caso de tener un valor malo. Pero si solo derivas la clase de tipos, esto no deberia de ser un problema
```hs
data SixSidedDie = S1 | S2 | S3 | S4 | S5 | S6 deriving (Enum)
> [S1 .. ]
[one, two, three, four, five, six]
```
Haskell es magico cuando vamos a derivar clases de tipo. En general, si no tienes razon para implementar tu mismo, deriving es no solo facil si no  tambien mejor

## 14.7 Clases de Tipo para tipos mas complejos
En el capitulo 4 vimos que podemos usar funciones de primera clase para ordenar algo como un tupla de nombres.
```hs
type Name = (String, String)

names :: [Name]
names = [("Emilio","Ticona")
        ,("Eugenio","Derbez")
        ,("Federico","Nitro")]
```
Como podemos recordar habia un problema cuando se ordenaban:
```hs
> import Data.List
> sort names
[("Emilio","Ticona"),("Eugenio","Derbez"),("Federico","Nitro")]
```
Lo buen es que claramente tus tuplas se derivan automaticamente de Ord, asi que ellos son ordenados tambien. Desafortunadamente, no estan ordenados en la forma deseada por el ultimo y primer nombre. En la leccion 4, usamos una funcion de primera clase y pasamos esta a SortBy, pero esto es molesto de hacer mas de una vez. Claramente, podemos implementar tu propio Ord personalizado para Name
```hs
instance Ord Name where
   compare (f1,l1) (f2,l2) = compare (l1,f1) (l2,f2)
```
Pero cuando cargamos est codigo obtenemos un error! Esto es porque par Haskell Name es identica a     (String, String), y, como hemos visto. Haskell actualmente conocemos como ordenar estos. para resolver estos asuntos, necesitamos crear una nuevo tipo de dato, Podemos hacer esto para usar los datos anteriores
```hs
data Name = Name (String, String) deriving (Show, Eq)
```
Aqui la necesidad de constructores de datos es clara. Para haskell, ellos son una forma de notar "Esta tupla es especial de otras" Ahora que tenemos esto podemos implementar Ord personalizado.

```hs
instance Ord Name where
   compare (Name (f1, l1)) (Name (f2,l2)) = compare (l1,f1) (l2,f2)
```
Note que somos capaces de explotar el hecho que haskell deriva Ord sobre la tupla (String, String) para hacer la implementacion personalizamos compare mucho mas facil
```hs
names :: [Name]
names = [Name ("Emil", "Cioran")
        , Name ("Eugene", "Thacker")
        , Name ("Freddy", "Nitro")]

-- Veremos los datos ordenados

> import Data.List
> sort names
[Name ("Emil", "Cioran"), Name ("Freddy", "Nitro"), Name ("Eugene", "Thacker")]

```
## 14.8 Roadmap clases de tipos
El grafico muestra las clases de tipos definidos en la libreria standard de Haskell. las flechas de una clase a otra indica una relacion de superclase.  Esta unidad ha convertido la mayoria de clase de tipo basicas. En la unidad 3, comenzaremos explorando clases de tipos mas abstractos, Semigrupos y Monoides, y comenzaremos a ver las diferentes clases de tipos pueden hacer de interfaces. En la unidad 5, veremos una familia de clases de tipo-- Functor, Applicative, y Monad - que provee una forma de modelar el contexto de una computacion. Aunque este ultimo grupo es particularmente un desafio para aprender, permite algunas de las mas poderosas abstracciones de Haskell.













