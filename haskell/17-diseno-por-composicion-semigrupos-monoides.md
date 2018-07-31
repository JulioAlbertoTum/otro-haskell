Hemos visto tipos suma que permiten pensar fuera del diseno de patrones tipico basado en jerarquias presente en la mayoria de los lenguajes de programacion. Otra idea en que la diverge es la composicion (composability). Composicionalidad significa que creamos algo nuevo para combinar 2 cosas.

Podemos componer dos documentos y obtener otro, mezclar 2 colores y obtener uno nuevo. Haskell ofrece una forma estandar de combinar instancias de un mismo juntas.

## 17.1 Introduccion a la composicionalidad - combinando funciones
Antes de profundizar la combinacion de tipos, veamos algo mas fundamental componer funciones. Una funcion de alto orden que tomas 2 funciones como argumentos. Usando composicion de funciones es particularmente util para combinar funciones al vuelo y de una forma legible. Algunos ejemplos son:

```hs
myLast :: [a] -> a
myLast = head . reverse

myMin :: Ord a -> [a] -> a
myMin = head . sort   -- sort requiere importar Data.List

myMax :: Ord a -> [a] -> a
myMax = myLast . sort

myAll :: (a -> Bool) -> [a] -> Bool --  es true para todos los items en una lista
myAll testFunc = (foldr (&&) True ) . (map testFunc)
```
En muchos casos usamos una expresion lambda para crear funciones rapidamente, composicion sera mas eficiente y facil de leeer.

## 17.2 Combinando como tipos: Semigrupos
Exploraremos composicionalidad mas aun. Veamos el tipo simple llamado SemiGroup. Para esto importamos Data.Semigroup.
La clase Semigroup solo tiene un metodo importante que necesitamos, el operador <>. Podemos pensar en <> como un operador para combinar instancias del mismo tipo. Puedes trivialmente implementar Semigroup para Integer por la definicion <> como +
```hs
instance Semigroup Integer where   -- hacemos Integer una instancia de la clase tipo Semigroup
   (<>) x y = x + y                -- Definimos el operador <> como simple adicion
```
Parece trivial pero pensemos en lo que significa. Aqui la signatura par el tipo <>:
```hs
(<>) :: Semigroup a => a -> a -> a
```
Esta simple signatura es el corazon de la idea de composicionalidad; puedes tomar 2 cosas y combinarlas para tener una nueva del mismo tipo.

### 17.2.1 El Semigroup Color
Pareceria que este concepto es mas util solo en las matematicas, pero en realidad estamos familizarizados desde una edad temprana. El ejemplo mejor conocido de esto es la adicion de colores. podemos combinar colores para obtener otro.
- Azul y amarillo da verde
- Rojo y amarillo da naranja
- Azul y Rojo da purpura
Podemos usar tipos para representar este problema de mezclar colores. Primero, necesitamos simplemente usar tipo suma de  los colores
```hs
data Color = Red | Yellow | Blue | Green | Purple | Orange | Brown deriving (Show, Eq)

-- Implementamos Semigroup para el tipo Color

instance Semigroup Color where
   (<>) Red Blue = Purple
   (<>) Blue Red= Purple
   (<>) Yellow Blue = Green
   (<>) Blue Yellow = Green
   (<>) Yellow Red = Orange
   (<>) Red Yellow = Orange
   (<>) a b = if a == b
              then a
              else Brown

-- Ahora podemos jugar con los colores
> Red <> Yellow
Orange
> Red <> Blue
Purple
> Green <> Purple
Brown
```
Esto es genial, pero tendremos un problema cuando adicionamos mas de 2 colores, si queremos que la mezcla de colores sea asociativa. Asociatividad significa que el orden en que apliquemos el operador no importe. Para numeros esto significa que 1+(2+3) = (1+2)+3. Veremos claramente que no son asociativos.
```hs
> (Green <> Blue) <> Yellow
Brown
> Green <> (Blue <> Yellow)
Green
```
No solo esta regla tiene sentido intuitivamente, pero es formalmente requerida de la clase de tipo SemiGroup. Esta puede seruna de las partes mas confusas de las clases de tipos mas avanzadas que cubriremos en esta unidad. Muchos de ellos tiene leyes de clases de tipo que requieren el mismo comportamiento. Desafortunadamente, el compilador de Haskell no puede cumplir esto. La mejor advertencia a esto es que siempre tengamos cuidado de leer la documentacion cuando implementamos una clase de tipo no trivial, nosotros mismos.

### Haciendo Color asociativo usando guardas.
Podemos superar este problema haciendo que si uni de los colores es usado para ser otro, combinandolo produce el color compuesto. Asi purpura mas rojo todavia es purpura. Podemos usar este enfoque para listar una lista con un gran numero de reglas de patrones comparando cada posibilidad. Pero esta solucion es demasiado larga. En su lugar, usaremos la caracteristicas de Haskell llamada **guardas**. Guards trabajan como el muestreo de patrones, pero te permiten hacer algunos calculos sobre los argumentos que vas a comparar. 
```hs
howMuch :: Int -> String
howMuch n | n > 10 = "una rama completa"
          | n > 0 = "no mucho"
          | otherwise = "Tenemos una deuda"
 ```
 Con un entendimiento de guards, podemos reescribir las instancias de Semigroup para Color asi adicionamos las leyes a la clase de tipo para semigroups
```hs
instance Semigroup Color where
   (<>) Red Blue = Purple
   (<>) Blue Red = Purple
   (<>) Yellow Blue = Green
   (<>) Blue Yellow = Green
   (<>) Yellow Red = Orange
   (<>) Red Yellow = Orange
   (<>) a b | a == b = a
            | all (`elem` [Red, Blue, Purple]) [a,b] = Purple
            | all (`elem` [Blue, Yellow, Green]) [a,b] = Green
            | all (`elem` [Red, Yellow, Green]) [a,b] = Orange
            | otherwise = Brown
-- Vemos como ya no hay problema
> (Green <> Blue) <> Yellow
Green
> Green <> (Blue <> Yellow)
Green
```
Las leyes de clases de tipos son importantes porque cualquier otro codigo que use una instancia de una clase de tipo asumira que estan soportados

En el mundo real, hay muchas formas de hacer una cusa nueva de 2 cosas del mismo tipo. Imagina las siguientes posibilidades para la composicion:
- Combinar 2 consultas SQL para hacer una nueva consulta SQL.
- Combinar 2 snippets de HTML para hacer un nuevo snippet de HTML
- Combinar 2 formas para hacer otra forma

## 17.3 Composicion con Identidad: Monoides
Otro clase de tipo que es similar a Semigroup es Monoid. La unica y mayor diferencia entre Semigroup y Monoid es que Monoid requiere un elemento Identidad para el tipo. Cualquier elemento identidad signfica que x <> id = x (y id <> x = x). Para la adicion de enteros, el elemento identidad es el 0 . Pero en la clase vista, El tipo Color no tiene un elemento identidad. Tener un elemento identidad deberia ser un pequeno detalle. Pero este incrementa el poder de un tipo para permitirnos usar la funcion fold para combinar listas del mismo tipo.

La clase de tipo monoide es tambien interesante porque demuestra un problema molesto en la evolucion de las clases de tipo de haskell. Logicamente, asumimos que la definicion de Monoid luce asi:
```hs
class Semigroup a => Monoid a where
   identity :: a
```
Despues de todo, Monoid deberia ser una subclase de Semigroup porque este es solo un Semigroup con identity. Pero Monoid precede  a Semigroup y no es oficialmente una subclase de Semigroup. En lugar de esto, La definicion de Monoid es desconcertante.
```hs
class Monoid a where
   mempty :: a
   mappend :: a -> a -> a
   mconcat :: [a] -> a
```
Porque mempty en lugar de identity? Porque mappened en lugar de <>? Estas disparidades en nombres ocurre porque la clase de tipo Monoid fue adicionada antes que Semigroup. El monoide mas comun es una lista. La lista vacia es la identidad para listas, ++ es el operador <> para listas, Los nombres extranos de los metodos de monoid son solo m (para Monoid) seguidos de nombres comunes para funciones de listas: empty, append, y concat. Aqui puedes comparar las tres formas de hacer la operacion identidad sobre una lista.
```hs
> [1,2,3] ++ []
[1,2,3]
> [1,2,3] <> []
[1,2,3]
> [1,2,3] `mappend` mempty
[1,2,3]
``` 
Note que mappend tiene el mismo tipo signatura que <>

### mconcat: Combinando multiples Monoides en uno
La forma facil de ver cuan poderosa es identity, es explorar el metodo final en la definicion de Monoid: mconcat. La unica definicion requerida en Monoid son mempty y mappend

Si implementas estos 2, obtendras mconcat gratis. Si el tipo de signatura de mconcat, tendremos una buena vista de lo que hacemos.
```hs
mconcat :: Monoid a => [a] -> a
```
El metodo mconcat toma una lista de Monoids y los combina, retornando un solo Monoid. La mejor forma de entender mconcat es tomando una lista de listas y ver que pasa si aplicamos mconcat. Para hacer las cosas mas faciles, usaremos strings porque son solo listas de Chars.
```hs
> mconcat ["does", " this", " make", " sense?"]
"does this make sense?"
```
La gran cosa sobre mconcat es que porque tu definiste mempty y mappend, Haskell automaticamente infiere mconcat! Esto es porque la definicion de mconcat depende solo de foldr, mappend, y mempty. Aqui la definicion de mconcat:
```hs
mconcat = foldr mappend mempty
```
Cualquier metodo de clase de tipo puede tener una implementacion por defecto, proveer la definicion necesita solo una definicion general.

### 17.3.2 Leyes de Monoid
Asi como en Semigroup, tambien hay leyes para la Clase de tipo Monoid. Son 4:

- La primera es que mappend mempty x es x. Recuerda que mappend es lo mismo que (++), y mempty es [] para listas, intuitivamente significa que:
```hs
[] ++ [1,2,3] = [1,2,3]
```
- La segunda es que el primero con el orden inverso: mappend x mempty es x. En forma de lista es:
```hs
[1,2,3] ++ [] = [1,2,3]
```
- El tercero es que mappend x (mappend y z) = mappend (mappend x y) z. Esto es solo asociatividad, y de nuevo para listas es bastante obvio.
```hs
[1] ++ ([2] ++ [3]) = ([1] ++ [2]) ++ [3]
```
Como este es una ley de Semigroup, entonces mappend es tambien implementada como <>, esta ley puede ser asumida porque es requerida por las leyes de Semigroup

- La cuarta es solo una definicion de mconcat
mconcat = foldr mappend mempty

Note  que la razon de que mconcat use foldr en lugar de foldl es debido a la forma en que foldr puede trabajar con listas infinitas, mientras que  foldl forza la evaluacion.