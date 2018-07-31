## 13 Explorando tipos mas aun

En estes punto vimos algunas signaturas te tipos e incluso construimos tipos propios no triviales.
Para saber mas de tipos de una funcion podemos usar **:t** o mas verboso **:type** 

Si exploramos algunos tipos como la adicion
```hs
:t (+)
(+) :: Num a => a -> a -> a
```
La pregunta aqui es que significa "Num a =>"

## 13.2 Clases de tipos 
Las clases de tipos en haskell son una forma de describir grupos de tipos que se comportan de la misma forma. Si estamos familiarizados con Java o C#, las clases de tipos nos puede recordar a las interfaces. Cuando vemos **Num a** la mejor forma de entender esta sentencia **es decir que el tipo a es de la clase Num**. Pero que es lo que significa **clase de tipo Num**. Num es una clase de tipos generaliza la idea de un numero. Todos en la clase Num deben tener definida una funcion (+) en ellos. hay otras funciones en esta clase de tipo tambien. Una de las herramientas mas valiosas es **:info** que provee informacion sobre tipos y clases de tipos. Si usamos :info sobre Num obtendremos la siguiente  salida.
```hs
class Num a where
  (+) :: a -> a -> a
  (-) :: a -> a -> a
  (*) :: a -> a -> a
  negate :: a -> a
  abs :: a -> a
  signum :: a -> a
  fromInteger :: Integer -> a
```
Esta es la definicion de este clase de tipo. La definicion es una lista de funciones que todos los miembros de la clase deben implementar, vemos las signaturas de todos estas funciones. La familia de funciones que describen un numero es +, -, \*, negate, abs, y signum (da el signo de un numero). cada signatura de tipos muestra el mismo tipo de variable a para todos los argumentos y salidas. Ninguna de estas funciones puede retornar un tipo diferente a los que se toma como argumento. Por ejemplo, podemos no podemos adicionar dos Ints y obtener un Double

## 13.3 Los beneficios de clases de tipos
Para que necesitamos classes de tipos? Hasta ahora en haskell, cada funcion habia definido como trabajar para un conjunto especifico de tipos. Sin clases de tipos, necesitariamos un nombre diferente para cada funcion que adiciona un diferente tipo de valor. Tu tienes tipos variables, pero son muy flexibles. Si definimos
```hs
myAdd :: a -> a -> a
```
Entonces necesitaremos la habilidad de verificar manualmente que estamos adicionando solo tipos para los que tenga sentido usar add.
Clases de tipos tambien nos permite  definir funciones sobre una variedad de tipos en las que incluso no has pensado. Supon que queremos escribir una funcion addThenDouble como sigue.
```hs
addThenDouble :: Num a => a -> a -> a
addThenDouble x y = (x + y)*2
```
Como hemos usado la clase de tipo **Num**, este codigo trabajara automaticamente para Int y para Double, pero tambien sobre cualquier otro programa que has escrito e implementado la clase Num. Si has experimentado con la libreria de numeros romanos. el author a implementado la clase de tipo Num, esta funcion todavia trabaja.

#13.4 Definiendo clases de tipo
La salida de  Num en ghci es la definicion literar de esta clase de tipo. se ve como:
```hs
class TypeName a where
	fun1 :: a -> a
	fun2 :: a -> String
	fun3 :: a -> a -> Bool
``` 
En la definicion de Num, veras tipos variables. De hecho todas las funciones requeridas en cualquier definicion de clase de tipo sera expresada en terminos de tipos variables, porque por definicion estas describiendo una clase completa. Cuando defines una clase de tipo. estas haciendo precisamente eso porque no queremos definir funciones para solo un tipo. Una forma de pensar en clases de tipo es como un constraste de las categorias de tipos que un tipo puede representar.

Para solidificar estas ideas, escribiremos una clase de tipos propia. Como estamos aprendiendo Haskell, un gran clase tipo puede ser **Describable**. Cualquier tipo que sea una instancia de Describable puede describirse a si misma en idioma plano. Asi que requerimos solo una funcion, que es describe. Para cualquier tipo que tengas, este sera Describable, llamando describe sobre una instancia de el tipo nos dira todo sobre esta. Si Bool es Describable esperaremos algo como:
```hs
> describe True
"Un miembro de la clase Bool, True es opuesto a False"
> describe False
"Un miembro de la clase Bool, False es opuesto a True"
```
En este punto deberia preocupartnos implementar la clase de tipos solo definiendo esta. Sabemos que requerimos solo de una funcion, que es describe. La unica otra cosa que nos deberia preocupar sobre la signatura del tipo de la funcion. En cada caso, el argumento para la funcion es cualquier tipo que ha implementado la clase de tipo, y el resultado siempre es un string. necesitamos usar tipos variables para este primer tipo y un string para el valor retornado. Podemos poner todo junto y definir la clase de tipo como:
```hs
class Describable a where
	describe :: a -> String
```
Eso es todo, si quisieramos, podriamos construir un grupo mucho mas grande de herramientas para esta clase de tipo para proveer una documentacion automatica para tu codigo, o generar tutoriales  para ti.

## 13.5 Clases de tipo Comunes
Haskell define muchas clases de tipos para tu conveniencia, sobre los que aprenderemos a lo largo del libro. En esta seccion veremos los 4 mas basicos: Ord, Eq, Bounded, Show.

#13.6 Clases de tipo Ord y Eq
Veamos otro operador facil, mayor que (>)
```hs
:t (>)
(>) :: Ord a => a -> a -> Bool
```
Para Ord la signatura dice: "Toma cualquier dos del mismo tipo que implementa Ord y devuelve un booleano" Ord representa todas las cosas en el universo que se pueden comparar y ordenar. Numeros pueden ser comparados, pero tambien string y muchas otras cosas. Aqui la lista de funciones que Ord define
```hs
class Eq a => Ord a where
  compare :: a -> a -> Ordering
  (<) :: a -> a -> Bool
  (<=) :: a -> a -> Bool
  (>) :: a -> a -> Bool
  (>=) :: a -> a -> Bool
  max :: a -> a -> a
  min :: a -> a -> a
```
Por supuesto haskell hace cosas complicadas. Nota que en el lado en la definicion de la clase hay otra clase de tipo. En este caso, este es la clase de tipo Eq. Antes de entender Ord deberiamos ver Eq.
```hs
class Eq a where
  (==) :: a -> a -> Bool
  (/=) :: a -> a -> Bool
```
La clase de tipo Eq necesita solo 2 funciones == y /=. Si puedes decir que dos tipos son iguales o no. Este tipo esta en la clase de tipo Eq. Esto explica porque la clase de tipo Ord incluye la clase de tipo Eq en su definicion. Para decir que algo esta ordenado, claramente necesitamos ser capaces de decir si dos cosas son iguales. Pero el inverso no es cierto. Podemos describir muchas cosas diciendo "Estas cosas son iguales" pero no "Esto es mejor que otro". 

### 13.6.1 Bounded
En la leccion 11, mencionamos la diferencia entre los tipos **Integer** e **Int**. Esta diferencia esta tambien capturada por las clases de tipos. El comando :info es util para aprender sobre clases de tipo, pero tambien util para aprender sobre tipos. Si usas :info sobre un tipo veras la siguiente informacion:
```hs
data Int = GHC.Types.I# GHC.Prim.Int#   -- Defined in ‘GHC.Types’
instance Bounded Int -- Defined in ‘GHC.Enum’
instance Enum Int -- Defined in ‘GHC.Enum’
instance Eq Int -- Defined in ‘GHC.Classes’
instance Integral Int -- Defined in ‘GHC.Real’
instance Num Int -- Defined in ‘GHC.Num’
instance Ord Int -- Defined in ‘GHC.Classes’
instance Read Int -- Defined in ‘GHC.Read’
instance Real Int -- Defined in ‘GHC.Real’
instance Show Int -- Defined in ‘GHC.Show’
```
Puedes hacer lo mismo con el tipo Integer. Encontraras solo una diferencia entre estos tipos. Int es una instancia de la clase de tipo Bounded, e integer No. Entender las clases de tipos involucrados en un tipo ayuda a entender como un tipo se comporta. Bounded es otra clase de tipo simple que requiere solo de 2 funciones.
```hs
class Bounded a where
  minBound :: a
  maxBound :: a
```
Los miembros de bounded deben proveer una forma de obtener sus cotas superiores e inferiores. Lo interesante es que miBound y maxBound no son funciones solo valores. No toman argumentos solo valores de cualquier tipo que se le pase. Ambos Char e Int son miembros de la clase de tipo Bounded, nunca tendras que preguntar por cotas superior inferior para usar estos valores.

### 13.6.2 Show
Hemos mencionado las funciones show y read en leccion 11. Show y Read son clases de tipos increiblemente utiles que hacen show y read funciones posibles.
```hs
class Show a where
  showsPrec :: Int -> a -> ShowS
  show :: a -> String
  showList :: [a] -> ShowS
```
La funcion show cambia un valor a un String. cualquier tipo que implemente Show puede ser impreso. hemos estado haciendo un uso mas fuerte de la funcion show. Cuando usamos Ghci imprimimos porque este es miembro de la clase de Tipo. 
```hs
data Icecream = Chocolate | Vanilla

> Chocolate
No intance for ...
```
Obtenemos un error porque haskell no tiene idea de como convertir constructores de datos en strings. Cada valor que hemos impreso es por que tiene la clase de tipo Show.
```hs
data Icecream = Chocolate | Vanilla deriving (Show)

> Chocolate 
Chocolate
> Vanilla
Vanilla
```
Muchos de los mas populares clases de tipos tienen una definicion por defecto razonable. Pero puedes adicinar la clase de tipo Eq.
```hs
data Icecream = Chocolate | Vanilla deriving (Show, Eq, Ord)
> Vanilla == Vanilla
True
> Chocolate == Vanilla
False
> Chocolate /= Vanilla
True
```
En la siguiente leccion, veras mas de cerca como implementar tus propias clases de tipos, y como haskell no siempre es capaz de adivinar tus intenciones.









