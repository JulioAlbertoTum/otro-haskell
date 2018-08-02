En esta unidad se discutiremos como los tipos pueden ser adicionados y multiplicados, como los datos.
Como las funciones, los tipos tambien pueden tener argumentos. Tipos toman argumentos usando variables tipo en sus definiciones (sus argumentos son siempre otros tipos). Tipos definidos usando paremetros son llamados tipos parametricos. Tipos parametrizaos realizan un importante rol en Haskell, asi definiremos estructuras de datos genericos trabajan con una amplio rango de datos existentes.

## 18.1 Tipos que toman argumentos
Si estas familiarizado con tipos genericos de lenguajes tales como C# o Java, los tipos parametrizados son similares. Los tipos parametrizados permiten crear containers  que pueden guardar otros tipos. Por ejemplo, List<String> representa una lista de cadenas, y KeyValuePair<int, string> representa un par de valores en que un int sirve como una llave para un string. Usualmente, usamos tipos genericos para constrenir los tipos de valores a un Tipo Container que puede hacer mas facil trabajar con el. En haskell lo mismo es cierto.

El tipo parametrizado mas basico es Box que sirve como contenedor para otro tipo cualquiera. El tipo Box es equivalente a una funcion simple. pero para tipos parametrizados. La definicion seria:
```hs
data Box a = Box a deriving Show -- declaramos un tipo variable
```
El tipo Box es un contenedor abstracto que puede guardar cualquie otro tipo.  Si ponemos in tipo dentro  Box, El tipo Box toma  un valor concreto.
```hs
n = 6 :: Int
:t Box n
Box n :: Box Int
word = "box"
:t Box word
Box word :: Box [Char]
f x = x
:t Box f
Box f :: Box (t -> t)
otherBox = Box n
:t Box otherBox
Box otherBox :: Box (Box Int)
```
Tambien puedes hacer funciones simples para Box. Tal como wrap unwrap par poner items dentro o sacarlos de la caja.
```hs
wrap :: a -> Box a
wrap x = Box x

unwrap :: Box a -> a
unwrap (Box x) = x
```
Nota que ambas funciones no conocen el tip concreto de la caja. pero todavia son capaces de trabajar con el.

## 18.1.1 Un tipo parametrizado mas util: Triple
Como la funcion simple, El tipo Box es un poco primitivo para cualquier uso. Un contenedor mas util es Triple, que nosotros definimos como tres valores que son el mismo.
```hs
data Triple a = Triple a a a deriving Show
```
Es valioso notar que Triple no es lo mismo que una 3-tupla (a,b,c). Tuplas en Haskell pueden tener distintos valores. En este tipo Triple, todos lo valores deben tener el mismo tipo. Hay muchos caso practicos en que los valores tiene esta propiedad. Por ejemplo, los puntos en el espacio tridimensional puede ser visto como un Triple de tipo Double
```hs
type Point3D = Triple Double

aPoint :: Point3D
aPoint = Triple 0.1 53.2 12.3
```
Los nombres de personas tambien pueden ser representados como un Triple de Strings.
```hs
type FullName = Triple String

aPerson :: FullName
aPerson = Triple "Howard" "Phillips" "Lovecraft"
```
Asi tambien un Triple de Char
```hs
type Initials = Triple Char 

initials :: Initials
initials = Triple 'H' 'P' 'L'
```
Ahora que tenemos un modelo para Triples homogeneos, puedes escribir funciones para que funcionen para todos los casos. La primera cosa que puedes hacer es crear una forma de acceder a cada uno de los valores en Triple. Asi como fst y snd son definidos apra 2-tuplas, en grandes tuplas no hay formas de acceder a sus valores.
```hs
first :: Triple a -> a
first (Triple x _ _) = x

second :: Triple a -> a
second (Triple _ x _) = x

third :: Triple a -> a
third (Triple _ _ x) = x
```
Tambien puedes cambiar Triple a una lista
```hs
toList :: Triple a -> [a]
toList (Triple x y z) = [x,y,z]
```
Finalmente, podemos hacer una simple herramienta para transformar cualquier  Triple y guardar este Triple de la misma forma.
```hs
transform :: (a -> a) -> Triple a -> Triple a
transform f (Triple x y z) = Triple (f x) (f y) (f z)
```
Este tipo de transformaciones es util para una variedad de cosas. Puedes ahora mover este punto en todas las direcciones por un valor constante.
```hs
> transform (* 3) aPoint
Triple 0.30000000000000004 159.60000000000002 36.900000000000006
```
Puedes invertir todas las letras en el nombre de una persona
```hs
> transform reverse aPerson
Triple "drawoH" "spillihP" "tfarcevoL"
```
O importar Data.Char y hacer tus iniciales minusculas:
```hs
> transform toLower initials
Triple 'h' 'p' 'l'
```
Para combinar  esta ultima transformacion con toList obtenemos un string con letras minusculas
```hs
> toList (transform toLower initials)
"hpl"
```

### 18.1.2 Listas
El tipo parametrizado mas comun es List. El tipo List es interesante porque tiene un constructor diferente que la mayoria de los otros tipos que hemos visto. Como sabes usamos brackets para construir una lista y poner valores en ella. Esto es por conveniencia pero hace que buscar informacion sobre listas mas dificil que tipos que tiene un constructor de tipo mas tipico.En GHCi, puedes obtener mas informacion de List tipeando :info []. La definicion formal del tipo List es:
```hs
data [] a = [] | a:[a]
```
Lo facinante  es que esta es una completa y funcional implementacion de una lista! Si has escrito una linked list eun otro lenguaje de programacion esto deberia ser una sorpresa. Para entender mejor esto, puedes reimplementar una lista sobre si misma. el uso especial de brackets alrededor del tipo de valor es una built-in syntax para listas, una que no puede ser emulada.
Igualmente no puedes usar constructor de datos : cons. Para esta definicion, usamos los terminos List, Cons, y Empty. Aqui la definicion.
```hs
data List a = Empty | Cons a (List a) deriving Show
```
Note que la definicion de List es recursiva! En ingles plano, puedes leer esta definiciono como sigue: "Una lista de tipo a es o Empty o el valor consignado a con otra lista de tipo a". Que puede ser dificil de creer es que este tipo de definicion por si misma es un definicion completa de tu estructura de datos List! Pero aqui son listas que son identicas.
```hs
builtinEx1 :: [Int]
builtinEx1 = 1:2:3:[]
ourListEx1 :: List Int
ourListEx1 = Cons 1 (Cons 2 (Cons 3 Empty))
builtinEx2 :: [Char]
builtinEx2 = 'c':'a':'t':[]
ourListEx2 :: List Char
ourListEx2 = Cons 'c' (Cons 'a' (Cons 't' Empty))
```

Como una demostracion final, puedes implementar map para tu lista
```hs
ourMap :: (a -> b) List a -> List b
ourMap _ Empty = Empty
ourMap func (Cons a rest) = Cons (func a) (ourMap func rest)

-- ejecutandose en GHCi
GHCi> ourMap (*2) ourListEx1
Cons 2 (Cons 4 (Cons 6 Empty))
```

Ahora que sabemos la proxima vez que vayas a una entrevista de trabajo si te preguntan por implementar una lista linkeada, tu primera pregunta sera "Puedo hacerlo en Haskell?"

## 18.2 Tipos con mas de un parametro
Asi como las funciones, tipos tambien pueden tomar mas de un argumento. Lo importante a recordar es que mas de un tipo parametrico significa que el tipo puede ser un contenedor para mas de un tipo. Esto es diferente de contener mas de un valor el mismo tipo, como se hizo en Triple

### 18.2.1 Tuplas
Las tuplas son los tipos multiparametro mas ubicuos en Haskell y el unico tipo multiparametro que hemos visto hasta ahora. Como las listas, las tuplas son un constructor tipo built-in, (). Si quieres puedes usar :info sobre una tupla, tenemos que usar () con una coma dentro para todo n-1 item en la tupla. Por ejemplo, si quieres la definicion de una 2-tupla en GHCi sera:
```hs
data (,) a b = (,) a b
```
Nota que la definicino de tipo 2-tupla incluye 2 tipos de variable. Como hemos mencionado antes. esto da a la tupla la capacidad util de contener valores de 2 tipos. En muchos lenguajes de tipado dinamico tales como Python, Ruby y javascript, listas ordinarias pueden contener multiples tipos. Es importante realizar que las tuplas en haskell no son lo mismo que listas en otros lenguajes. La razon es que despues que hagamos nuestro tipo, este tomara un valor concreto. Esto es mejor verlo si tratamos de hacer una lista de tuplas. Supon que en un sistema de inventarioestse guarda el rastro de itens en sus cuentas.
```hs
itemCount1 :: (String,Int)
itemCount1 = ("Erasers",25)

itemCount2 :: (String,Int)
itemCount2 = ("Pencils",25)

itemCount3 :: (String,Int)
itemCount3 = ("Pens",13)
```
Puedes hacer una lista de estos items para guardar el rastro de tu inventario
```hs
itemInventory :: [(String,Int)]
itemInventory = [itemCount1,itemCount2,itemCount3]
```
Nota que estamos especificando el tipo concreto de la tupla: (String, Int)

### 18.2.2 Tipos: tipos de tipos

Otra cosa que los tipos de Haskell tienen en comun con las funciones y datos es que ellos tienen sus propios tipos tambien. Este tipo de un tipo es llamado **kind**. Como deberias esperar kinds son abstractos. Pero ellos se han elevado en profundidad en las clases de tipos mas avanzadas cubiertos en la unidad 5.
El *kind de un type* indica el numero de parametros que los tipos toman, que son expresados unsaod un asterisco (\*). Pueden no tener parametros teniendo un tipo de \* , tipos que toman un parametro tienen el tipo *->*, tipos con mas de 2 parametros tienen el tipo \*->\*->\*, etc.

En GHCi, usamos el comando :kind para buscar los kinds de cualquier tipo si no estas seguro de el (no olvides importar Data.Map):
```hs
GHCi> :kind Int
Int :: *
GHCi> :kind Triple
Triple :: * -> *
GHCi> :kind []
[] :: * -> *
GHCi> :kind (,)
(,) :: * -> * -> *
GHCi> :kind Map.Map
Map.Map :: * -> * -> *
```
Vale la pena apuntar que los tipos concretos tiene un diferente kind que su equivalentes no concretos:
```hs
GHCi> :kind [Int]
[Int] :: *
GHCi> :kind Triple Char
Triple Char :: *
```
Kinds pueden inicialmente paracer abstractos sin sentido. Pero entender kinds puede ser util cuando tratamos de hacer instancias de clases de tipos tales como Functor y Monad (cubierto en la unidad 5)

### 18.2.3 Data.Map
Otro tipo parametrizado util es el Map de Haskell (no confundir con la funcion map). Para usar Map, primero hay que importar Data.Map. Porque el modulo Data.Map  comparte algunas funciones con Prelude, vamos ha hacer una importacion cualificada. Para realizar una importacion cualificada,  adicionamos los detalles dados abajo al principio del archivo.
```
import qualified Data.Map as Map --  damos al modulo importado un nombre para evitar conflictos con funciones existentes.
```
Con la importacion cualificada, toda funcion y tipo del modulo debe ser prefijado con Map. Map permite buscar valores usando una clave. En muchos otros lenguajes, este tipo de dato es llamado Dictionary. El tipo parametrizado Map son los tipos de las claves y valores. A diferencia de List's y Tuple's, la implementacion de Map's  es no trivial. La mejor forma para entender este tipo es a traves de un ejemplo concreto.

Digamos que trabajamos en un laboratorio de un cientifico loco y tenemos una lista de numeros que corresponden a varios organos usados para crear horribles monstruos. Puedes comenzar haciendo un tipo suma de partes de cuerpo relevantes.
```hs
data Organ = Heart | Brain | Kidney | Spleen deriving (Show, Eq)
```
Supon que en tu inventario tienes los siguientes organos. (Duplicados estan bien; Nunca tenemos basos suficientes!)
```hs
organs :: [Organ]
organs = [Heart, Heart, Brain, Spleen, Spleen, Kidney]
```
Ahora cada organo es colocado en una gabeta numerado para ser devuelto un tiempo despues. Cada gabeta tiene un numero encima. Como las gabetas se usan para buscar items, cada numero debe ser unico. Adicionalmente, es importante que  cualquier ID que uses, este debe ser de la clase Ord. Si las gabetas no tienen orden, sera dificil buscar un organo eficientemente.

#### Mapas y tablas hash
* Mapas son similares a otro tipo de estructura llamada un tabla hash. Ambos permiten buscar valores con claves. La gran diferencia entre estas 2 estructuras es la forma en que los valores son buscados. En una tabla hash, una funcion transforma la llave en el indice de un array donde el valor esta almacenado. Esto permite una rapida busqueda de items, pero requiere una gran cantidad de memoria para almacenar y para prevenir colisiones. Un map busca los valores usando una busqueda de arbol binario. Esto es mas lento que una tabla hash pero todavia es rapido. El map busca valores  por la busqueda de claves necesitan tener la propiedad de ser de la clase Ord. Asi puedes comparar 2 claves y encontrarlos eficientemente en un arbol*

Aqui tenemos una lista de ID's (no todas las gabetas tienen un organo)
```hs
ids :: [Int]
ids = [2,7,13,14,21,24]
```
Con los organis y los ID's, tienes toda la informacion necesaria para construir un Map! Esto nos servira como un catalogo de las gabetas y ver facilmente que items estan en que gabetas.
La forma mas comun de construir un Map es con la funcion fromList. Usando :t en GHCi, pueder ver el tipo de fromList como se muestra en la figura 18.4.
Ahora podemos ver el tipo parametrico para tu tipo mapa Map:k y a , Lo que es interesante aqui es que el tipo de la clave, k, debe ser de la clase Ord. Esta restriccion es debido a la forma en que las claves son almacenadase buscadas internamente. La otra cosa a notar es que fromList espera una lista de tuplas, que representa pares clave valor. Puedes reescribir tus dos lista de la siguiente forma.
```hs
fromList :: Ord k => [(k,a)] -> Map k a

pairs = [(2,Heart),(7,Heart),(13,Brain)...]
```
Pero para listas suficientemente largas, esto es un dolor de cabeza! En su lugar, puedes usar la funcion zip de la leccion 6. La funcion zip toma 2 listas y retorna una lista de pares.
```hs
organPairs :: [(Int,Organ)]
organPairs = zip ids organs

-- Tenemos todas las partes, ponemos todo en el catalogo

organCatalog :: Map.Map Int Organ
organCatalog = Map.fromList organPairs
```
Finalmente podemos buscar in item usando Map.lookup. Cuando haces esto en GHCi, conseguimos un interesante resultado:
```hs
Map.lookup 7 organCatalog
Just Heart
```
Obtenemos Heart como se esperaba, pero este es precedido por el constructor de datos Just. So buscas la signatura del tipo para Map.lookup, obtendras la respuesta.
```hs
Map.lookup :: Ord k => k -> Map.Map k a -> Maybe a
```
Map.lookup returna un nuevo tipo parametrizado: Maybe.Maybe es simple pero poderoso tipo que es sujeto de la siguiente leccion.

