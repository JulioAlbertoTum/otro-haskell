Los tipos de datos algebraicos son cualquier tipo conformado por combinacion de otros. Se pueden combinar usando AND u OR. Los que se crean combinando otros tipos con and son llamados tipos producto. Losque son combinacion de conectores or son llamados tipos suma.

## 16.1 Tipos producto -- combinando tipos con "and"

Son creados por la combinacion de 2 o mas tipos existentes con and. Algunos ejemplos son:
- Una fraccion puede ser definido como un numerados y denominator (ambos enteros)
- Una direccion de calle tiene un numero (Int)  y un nombre de calle (String)
- Una direccion de correo deberia tener una direccion de calle y una ciudad (String) y un estado (String) ademas de un codigo zip (Int).

Esta es la forma mas comun de definir tipos en un lenguaje. El ejemplo mas simple es un struct de C.
```c
struct author_name {
	char *first_name;
	char *last_name;
};

struct book {
	author_name author;
	char *isbn;
	char *title;
	int year_published;
	double price;
};
```
En este ejemplo puedes ver que author_name es una combinacion de 2 strings. el tipo Book esta hecho de la combinacion de author_name, 2 Strings un Int, y un Double. 
En haskell tendriamos algo como:
```hs
data AuthorName = AuthorName String String
data Book = Author String String Int
```
es preferible usar sintaxis record, es mucho mas parecida a C.
```hs
data Book = Book {
	  author :: AuthorName
	, isbn   :: String
	, title  :: String
	, year   :: Int
	, price  :: Double }
}

Book y AuthorName son ejemplos de tipos producto y son analogos en lenguajes de programacion moderno. 

## 16.1.1 La maldicion de los tipos producto: jerarquia de diseno
Hacer nuevos tipos solo combinando tipos existentes trata de un interesante modelo de diseno de software. Porque la restriccion que podemos expandir una idea solo adicionando a este, estas restringido al diseno top down. comenzando con la representacion mas abstracta de un tipo que puedas imaginar. Esta es la base para el diseno de software en terminos de jerarquia de clases.

```java
public class Book {
	Author author;
	String isbn;
	String title;
	int yearPublished;
	double price;
}
```
Esto funciona bien hasta que quieres venter discos de vinyl en la tienda. La implementacion por defecto sera:
```hs
public class VinylRecord {
	String artist;
	String title;
	int yearPublished;
	double price;
}
```
VinylRecord es similar a Book. Esto causa un problema. Para comenzar no podemos reusar el tipo Author. porque no todos los artistas tienen nombre, algunas veces el artista es una banda en lugar de un individuo. Puedes usar el tipo Author para Elliot Smith pero no para The Smiths. en diseno jerarquico tradicional no hay una buena respuesta para estos problemas con respeto al Author  y artista. Otro problema es que vinyl records no tiene un ISBN number.

El gran problema es que quieres un solo tipo que representa ambos vinyl records y books para hacer un inventario buscable. Como puedes componer tipos solo con and, necesitas desarrollar una abstraccion que describa todos los records y books tengan en comun. Despues implementaremos solo las diferencias en las clases separadas. Esta es la idea fundamentar detras de la herencia. A continuacion creamos la clase StoreItem, que es una superclase de ambos 
```java
public class StoreItem {
	String title;
	int yearPublished;
	double price;
}

public class Book extends StoreItem {
	Author author;
	String isbn;
}

public class VinylRecord extends StoreItem {
	String artist;
}

La solucion trabaja bien. Ahora podemos escribir el restos de tu codigo que trabaje con StoreItems y entonces usar sentencias condicionales para manejar Book o VynilRecord. Pero supon que realizas  el ordenado de un rango de juguetes coleccionables para vender aqui la clase
```java
public class CollectibleToy {
	String name;
	String description;
	double price;
}
```
Para hacer que esto trabaje, tenemos que refactorar completamente el codig de nuevo. Ahora StoreItem  tendra solo el atributo price, porque este es un unico valor para todos los items que lo comparten en comun. Loas atributos enter VinylRecord y Book deben volver a estas clases. Alternativamente, puedes hacer una nueva clase que herede de StoreItem y es una superclase de VinylRecord y Book. Que pasa con el atributo name de CollectibleToy? Es que es diferente de title? Puede que tengas que hacer una interface para todos los items en su lugar. El punto es que incluso en casos relativamente simples, disenar en estrictamente tipos producto puede llegar a ser complejo.

En teoria, crear jerarquias de objetos  es elegante y captura una abstraccion sobre como todo en el mundo esta interrelacionado. En la practica, creando incluso jerarquias de objetos es  enigmatico con los cambios en el diseno. La raiz de todos estos cambios es que la unica forma de combinar tipos en la mayoria de los lenguajes es con and. Esto nos fuerza a comenzar desde la abstraccion extrema y moviendonos hacia abajo. Desafortunadamente, la vida real esta llena de casos extranos que hacen mucho mas complicado de lo que tipicamente se quiere.

## 16.2 Tipos suma - compinando tipos con "or"
Los tipos suma son sorpresivamente una herramienta poderosa, dado que ellos proveen solo la capacidad de combinar dos tipos con or. Aqui estan ejemplos de combinacion de tipos con or:
- Un dado es de 6 lados o de 20 lados o ....
- Un paper es autoria de una persona o un grupo de personas
- Una lista es o una lista vacia o un item adosado a otra lista.

El tipo suma mas simple es Bool.
```hs
data Book = False | True
```
Una instancia de Bool es o el constructor de datos False o el constructor de Datos True. Esto puede dar un error de impresion que los tipos suma son solo una forma haskell de crear tipos enumerados que existen en otros lenguajes. Pero has visto un ejemplo en que los tipos suma pueden ser usados para algo mas poderoso, en el tema 12 cuando definimos 2 tipos de nombres.
```hs
type FirstName = String
type LastName = String
type MiddleName = String

data Name = Name FirstName LastName
          | NameWithMiddle FirstName MiddleName LastName
```
En este ejemplo, puedes usar 2 tipos de constructores que pueden se o un tipo FirstName consistente de 2 strings o un NameWithMiddle consistente de 3 string. Aqui, usando or entre 2 tipos permite ser expresivo sobre el significado de los tipos. Adicionar or es una herramienta que permite hacer combinaciones con un mundo de posibilidades en Haskell que no estan disponibles en cualquier lenguaje de programacion sin tipos suma. Para ver cuan poderosos son los tipos suma, permitenos resolver algunos de los problemas vistos en la seccion previa.

Un lugar interesante para comenzar es la diferencia entre author y artista. En nuestro ejemplo, necesitamos 2 tipos porque asumimos que el nombre de cada libro puede ser representado como un nombre y un apellido, mientras que un artista hace records pueden ser representaddas coo un nomre de pesona o nombre de una banda. Resolver este problema con tipos producto es dificil. Pero con tipos suma, puedes resolver el problema facilmente. Podemos comenzar con un tipo Creator que es un Author  o un Artist
```hs
data Creator = AuthorCreator Author | ArtistCreator Artist
```
Hasta ahora teniamos un tipo Name, asi que podemos comenzar por definir Author como un nombre.
```hs
data Author = Author Name
```
Un artist es un poco mas dificil; como hemos mencionado, Artistas pueden ser un nombre de persona o nombre de una banda.
```hs
data Artist = Person Name | Band String
```
Esta es una buena solucion, pero que todavia tiene algunos puntos complicados que ocurre en la vida real todo el tiempo? Por ejemplo que del author como H.P. Lovecraft? Podrias forzarte a usar Howard Phillips Lovecraft, pero porque forzarte a restringir el modelo de datos? Este debe ser flexible. ESto puede hacerse facilmente adicionar otro constructor Name.
```hs 
data Name = Name FirstName LastName
          | NameWithMiddle FirstName MiddleName LastName
          | TwoInitialWithLast Char Char LastName
```
Nota que Artist, Author,  y como un resultado, Creator todo depende de la definicion de Name. Pero tienes que cambiar solo la definicion de Name mismo y no necesitas preocuparte sobre como otros tipos estan usando el Name Definido. Al mismo tiempo, todavia nos beneficiaremos del reuso del codigo, como Artist y Author se benefician de tener Name definido en una solo lugar.
```hs
hpLoveCraft :: Creator
hpLoveCraft = AuthorCreator (Author (TwoInitialsWithLast 'H' 'P' "LoveCraft"))
```
Aunque los constructores de datos en este ejemplo pueden se verbosos, en la practica es probable usar funciones que abstraen mucho de esto. Ahora piensa como esta solucion y como llegaria a ser cin un diseno jerarquico requerido por tipos producto. Desde el punto de vista de diseno jerarquico, necesitamos una superclase Name con solo el atributo last-name. Entonces necesitamos separar subclases para cada uno de los 3 constructores de datos que usamos. Pero incluso entonces nombres como Andrew W. K. rompen el modelo. Esto es muy facil con tipos suma.
```hs
data Name = Name FirstName LastName
          | NameWithMiddle FirstName MiddleName LastName
          | TwoInitialWithLast Char Char LastName
          | FirstNameWithTwoInits FirstName Char Char
```
La unica solucion para el punto de vista de tipos producto es crear una clase name con una lista crecientede campos que estaran sin uso.
```java
public class Name {
	String FirstName;
	String lastName;
	String middleName;
	char firstInitial;
	char middleInitial;
	char lastInitial;
}
```
Requerira mucho codigo extra asegurar que todo se comporta correctamente. Adicionalmente, no tenemos garantia sobre Name llega a ser un estado valido. Que pasa si todos estos atributos tienen valores? No hay ningun tipo de verificador en java que puede asegurar que un objeto nombre conoce todas las restricciones que hemos especificado para los nombres. En haskell, podemos conocer que solo los tipos explicitos que hemos definido pueden existir.

## 16.3 Poniendo todo junto en la tienda de libros.

Ahora permitenos revisar nuestro problema de la tienda de libros y ver como pensar como los tipos sumas nos pueden ayudar. con el tipo Creator a mano , podemos reescribir Book.
```hs
data Book = Book {
      author    :: Creator
    , isbn      :: String
    , bookTitle :: String
    , bookYear  :: Int
    , bookPrice :: Double
}

-- definimos el tipo  VinylRecord

data VinylRecord = VinylRecord {
	  artist         :: Creator
	, recordTitle    :: String
	, recordYear     :: Int
	, recordPrice    :: Double
}

-- creamos el tipo StoreItem

data StoreItem = BookItem Book | RecordItem VinylRecord
```
Pero de nuevo nos olvidamos de CollectibleToy. Dado el tipo suma, es facil adicionar este tipo de dato y extender nuestro tipo StoreItem.
```hs
data CollectibleToy = CollectibleToy {
	  name :: String
    , description :: String
    , toyPrice :: Double
}

-- adicionando a storeItem
data StoreItem = BookItem Book
  | RecordItem VinylRecord
  | ToyItem CollectibleToy
```
Finalmente, hemos demostrado como construir funciones que trabajan sobre todos estos tipos, podemos escribir una funcion price que obtenga el precio de cualquier item.
```hs
price :: StoreItem -> Double 
price (BookItem book) = bookPrice book
price (RecordItem record) = recordPrice record
price (ToyItem toy) = toyPrice toy
```
Tipos suma te permite dramaticamente ser mas expresivo con tus tipos mientras todavia provee convenientemente formas de crear grupos de tipos similares.




