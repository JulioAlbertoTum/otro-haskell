## 12.1 Usando tipos sinonimos 

En haskell podemos reemplazar [Char] con String. Tipos sinonimos son extremadamente utiles, porque hace que la signatura de tipos sea mas facil de leer. 
```hs
pacienteInfo :: String -> String -> Int -> Int -> String
pacienteInfo fname lnam age height = name ++ " " ++ ageHeight
	where name = lname ++ ", " ++ fname
	      ageHeight = "(" ++ show age ++ "yrs. " ++ show height ++ "in.)"
```
Si asumes que pacienteInfo es parte de una gran aplicacion. enconces el uso de todos los argumentos sera frecuente. signaturas de tipo son mas beneficiosas para el programador que para el compilador. Pero puedes enmascarar algunos de estos tipos.
Para crear nuevos tipos podemos usar **type**
```hs
type FirstName = String
type LastName = String
type Age = Int
type Height = Int

pacienteInfo :: FirstName -> LastName -> Age -> Height -> String
```
La creacion de typos sinonimos no esta limitado a renombrar uno a uno. Podemos guardar los nombres del paciente como una tupla. La tupla guardara el par del primer y segundo nombre.
```hs
type PatientName = (String, String)
```
Podemos crear funciones helpers para obtener el primer y segundo nombre
```hs
firstName :: PatientName => String
firstName patient = fst patient

lastName :: PatientName -> String
lastName patient = snd patient
```
## 12.2 Creacion de nuevos tipos
Si adicionalmente ponemos el sexo del paciente Puedes usar string para esto, usando la palabra literal male o female, o un entero o booleano. En muchos otros lenguajes de programacion, esta es la ruta que se toma. Pero ninguno de ellos es tan buena idea, es mas facil imaginar los errores que se generarian usando esta solucion. En haskell tenemos un sistema de tipos mas poderoso. Es mejor crear un nuevo tipo. Un tipo se crea con la palabra clave **data** 
```hs
data Sex = Male | Female
```
La palabra reservada data le dice a haskell que estamos definiento un nuevo tipo. La palabra Sex es el constructor del tipo. En este caso el constructor del tipo es el nombre del tipo, pero en siguientes lecciones veremos que los constructores de tipos pueden tener argumentos. Male y Female son ambos constructores de datos. Un constructor de datos es usado para crear una instancia concreta de un tipo. Para separar los constructores de datos usamos |.

Al igual que Sex Bool esta definido de la misma forma en haskell.
```hs
data Bool = True | False
```
Porque no solo usamos Bool como tipo sinonimo. Primer que debemos hacer mas legibles los constructores de datos. Esto hace cosas como el muestreo de patrones mas facil. 
```hs
sexInitial :: Sex -> Char
sexInitial Male = 'M'
sexInitial Female = 'F'
``` 
Lo mas importante es que el compilador pueda verificar y asegurar siempre el uso del tipo correcto. Cualquier  error potencial creado accidentalmente usando Bool de una forma incompatible con el tipo Sex.

Si deseamos modelar el tpo de sangre tenemos cuatro posibilidades A, B, AB , O. Esto hace referencia ha la familia de anticuerpos en la sangre. La parte positiva o negativa se refiere al grupo Rhesus de la persona, que indica la presencia y ausencia del antigeno en particular. Un mal encuentro entre anticuerpos y antigenos puede causar que las transfusiones de sangre provoquen una muerte.

Para modelar el tipo de sangre, Podemos replicar lo hecho con Sex. Pero en este caos tenemos dos tipos Rh de sangre para cada tipo de sangre ABO, entonces tenemos 8 posibilidades. Una mejor solucion comenzar modelando el Rh y ABO de forma separada. RhType luce como Sex.
```hs
data RhType = Pos | Neg

data ABOType = A | B | AB | O
```
Finalmente la definicion del tipo de sangre usa los dos anteriores.
```hs
data BloodType = BloodType ABOType RhType
```
En este caso los constructores de datos tienen el mismo nombre que el tipo constructor. Necesitamos este constructor de datos para combinar ABOType y RhType. Podemos leer el constructor de datos como " Un BloodType es una ABOType con un RhType"
```hs
patient1BT :: BloodType
patient1BT = BloodType A Pos

patient2BT :: BloodType
patient2BT = BloodType 0 Neg

patient3BT :: BloodType
patient3BT = BloodType AB Pos
```
Seria buen ser capaz de imprimir estos valores, veremos eso en la leccion 13 por ahora escribiremos 3 funciones y usaremos pattern matching para mostrar los valores.
```hs
showRh :: RhType -> String
showRh Pos = "+"
showRh Neg = "-"

showABO :: ABOType -> String
showABO A = "A"
showABO B = "B"
showABO AB = "AB"
showABO O = "O"

showBloodType :: BloodType -> String
showBloodType (BloodType abo rh) = showABO abo ++ showRh rh 
```

En este ultimo paso fuimos capaces de usar patter matching  en el ultimo paso para extraer los componentes ABOType y RhType  de BloodType.

En este ejemplo una pregunta importante es saber si un paciente puede donar a otro las reglas son las siguientes:
- A puede donar a A y AB
- B puede donar a B y AB
- AB puede donar solo a AB
- O puede donar a cualquiera
Realizamos la funcione canDonateTo para determinar si un tipo de sangre puede donar a otro.
```hs
canDonateTo :: BloodType -> BloodType -> Bool
canDonateTo (BloodType O _) _ = True -- donante universal
canDonateTo _ (BloodType AB _) = True -- receptor universal
canDonateTo (BloodType A _) (BloodType A _) = True
canDonateTo (BloodType B _) (BloodType B _) = True
canDonateTo _ _ = False -- en otro caso
```
En este punto es una buena idea refactorar tus nombres un poco. Otra gran caracteristica es ser capaz de modelar un nombre medio opcional. Tenemos un tipo sinonimo PatientName que es una tupla que solo llena el nombre y el apellido. Podemos combinar lo aprendido en el tipo Sex y BloodType para  crear un tipo nombre mas robusto. Adicionamos un tipo sinonimo para el segundo nombre y usamos este para construir tipos de nombres mas sofisticados.
```hs
type MiddleName = String
data Name = Name FirstName LastName
			| NameWithMiddle FirstName MiddleName LastName
```
Podemos leer esta definicion de Name como sigue: un nombre es o un nombre y un apellido, o un nombre uno segundo nombre y un apellido. usamos un showName para  trabajar con su constructor.
```hs
showName :: Name -> String
showName (Name f l) = f ++ " " ++ l
showName (NameWithMiddle f m l) = f ++ " " ++ m " " ++ l

name1 = Name "Jerome" "Valeska"
name2 = NameWithMiddle "Jean" "Marie" "Curie"

showName name1
"Jerome Valeska"
```
## 12.3 Usando sintaxis record
Al comenzar esta leccion pasamos 4 argumentos para la funcion patientInfo
```hs
patientInfo :: String -> String -> Int -> Int -> String
patientInfo fname lnam age height = name ++ " " ++ ageHeight
	where name = lname ++ ", " ++ fname
	      ageHeight = "(" ++ show age ++ "yrs. " ++ show height ++ "in.)"
```
Cuando tratamos de capturar en la definicion de esta funcion la idea era pasar una paciente. pero no teniamos las herramientas para modelar esta informacion de manera compacta en Haskell.
Ahora que sabemos sobre tipos seremos capaces de crear el tipo Patient que contiene toda esta informacion y mas. Pasar un gran numero de argumentos puede ser confuso.

El primer paso en modelar el tipo paciente sera listar una lista de caracteristicas que queremos guardar y que el tipo debe representar.
- Nombre: name
- Sexo: sex
- Age(Years): Int
- Height(inches): Int
- Weight(pounds): Int
- Blood Type: BloodType
Podemos usar **data** para crear el tipo nuevo.
```hs
data Patient = Patient Name Sex Int Int Int BloodType
```
Si creamos el primer ejemplo 
```hs
johnDoe :: Patient
johnDoe = Patient (Name "John" "Doe") Male 30 74 200 (BloodType AB Pos)
``
Crear datos de esta forma es genial, pero se siente definitivamente torpe para datos con muchas propiedades. Puedes resolver alguno de estos. Pero incluso si el tipo definido de Patient es mas facil de leer, Es facil imaginar mas valores que se pueden adicionar a la definicion de pacciente, que solo lo hace mas dificil.

Esta representacion de pacientes tiene mas de un molesto problema. Es razonablemente que cada valor del paciente individualmente.  Podemos usar pattern matching.
```hs
getName :: Patient -> Name
getName (Patient n _ _ _ _ _) = n
getAge :: Patient -> Int
getAge (Patient _ _ a _ _ _) = a
getBloodType :: Patient -> BloodType
getBloodType (Patient _ _ _ _ _ bt) = bt
``` 
Patrones de muestreo hace mas facil de escribir, pero tenemos que escribir seis argumentos mas que no usaremos. Si al final tubieramos 12 argumentos tendriamos que escribirlos todos para cada funcion. Afortunadamente, Haskell tiene una gran solucion para este problema. Podemos definir tipos de datos como Patient para usar **record syntax** Definimos un nuevo tipo de datos con esta sintaxis es mas facil de entender que los tipos representados con propiedades de tipos de datos.
```hs
data Patient = Patient { name :: Name
					   , sex :: Sex
					   , age :: Int
					   , height :: Int
					   , weight :: Int
					   , bloodType :: BloodType  }
```
La primera gran victoria de record syntax es que la definicion de tipos es mas facil de leer y entender ahora. Ademas ahora es mas vacil crear datos
```hs
jackieSmith :: Patient
jackieSmith = Patient {name = Name "Jackie" "Smith"
                      , age = 43
                      , sex = Female
                      , height = 62
                      , weight = 115 
                  	  , bloodType = BloodType O Neg }
```
Adicionalmente no tienes que escribir getters; cada campo en la sintaxis record crea automaticamente una funcion de acceso para cada valor.
```hs
height jackieSmith
62
showBloodType (bloodType jackieSmith)
"O-"
```
tambien podemos asignar valores en record syntax para pasar un nuevo valor entre llaves para tus datos. Si queremos actualizar la edad hariamos:
```hs
jackieSmithUpdated = jackieSmith { age = 44 }
```
Como estamos en un mundo puramente funcional, un nuevo tipo paciente sera creado y debe ser asignado a una nueva variable para ser util.
 



